import threading
import requests
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import requests
from flask import Flask, request, jsonify
from PySide6.QtCore import *
import base64
import json
from requests.exceptions import Timeout, RequestException


class Entry:
    def __init__(self, entryNum, employeeID, entryTime, manualEntry, comment, sysUserID):
        self.entryNum = entryNum
        self.employeeID = employeeID
        self.entryTime = entryTime
        self.manualEntry = manualEntry
        self.comment = comment
        self.sysUserID = sysUserID


class apiCalls(QThread):
    HomeImageSignal = Signal(bytes)
    HomeDetailsSignal = Signal(str, str, str, str, str, str)
    DatabaseImageSignal = Signal(bytes)
    DatabaseDetailsSignal = Signal(str, str, str, str, str, str)
    AddUserDetailsSignal = Signal(str, str, str, str, str, str)
    NotFoundSignal = Signal(str)
    ManualImageSignal = Signal(bytes)
    
    
    def __init__(self):
        super().__init__()
        
    def start(self, id, page):
        thread = threading.Thread(target=self.GetPhoto, args=(id, page, ), daemon=True)
        thread.start()
        return thread
    
    
    def GetEntries(self, amount, id):
        try:
            apiUrl = f"http://192.168.0.110:5143/api/Entries/GetXEntries/{amount}/{id}"
            response = requests.get(apiUrl, verify = False, timeout=2)
            entryList = []
            print(response)
            if response.status_code == 200:
                _entryList = response.json()
                print(_entryList)
                for entryItem in _entryList:
                    item = Entry(
                        str(entryItem.get('entrynum', '')),
                        str(entryItem.get('employeeid', '')),
                        str(entryItem.get('entrytime', '')),
                        str(entryItem.get('manualentry', '')),
                        entryItem.get('comment', 'N/A'),
                        str(entryItem.get('sysuserid', 'N/A')),
                    )
                    entryList.append(item)
                    
                
                
                return entryList
        except Exception as ex:
            print(f"API Entry error: {ex}")
                
    def AddEntry(self, id, comment, sysID):
        apiUrl = f"http://192.168.0.110:5143/api/Entries/AddEntry"
        
        
        data = json.dumps({"employeeid": id, "manualentry": True, "comment": comment, "sysuserid": sysID})

        response = requests.request("POST", apiUrl, headers={'Content-Type': 'application/json'}, data=data, verify=False)
            
        if response.status_code == 400:
            self.display("Entry Upload failed")
        
        
    def OpenGate(self):
        apiUrl = "http://192.168.0.31/open"
        try:
            response = requests.request("GET", apiUrl, timeout=2)
        except Exception as ex:
            print(f"Error with gate opening: {ex}")
        
    def SendLogin(self, id, password):
        url = "https://localhost:5144/api/SysUser/Verify"
        payload = json.dumps({"id": id,"password": password})
        headers = {  'Content-Type': 'application/json'}
        try:
            response = requests.request("POST", url, headers=headers, data=payload, verify=False, timeout=4)
            print(response.text)
            if response.text == "true":
                return True, None
            if response.text == "false":
                return False, None
        except Timeout:
            self.display("Timeout, employee database may be down")
            return False, "Timeout"
        except RequestException as ex:
            return False, f"Error: {ex}"
            self.display(f"Error connecting to employee database....Is it down? Please contact System Admin")    
            return
    
    def AddEmployee(self, fname, lname, dob, photo, id, password):
        url = "https://localhost:5144/api/Employees/AddEmployee"

        data = json.dumps({"Fname": fname, "Lname": lname, "Dob": dob, "photo": photo})
        
        try:
            response = requests.request("POST", url, auth=(id, password), headers={'Content-Type': 'application/json'}, data=data, verify=False)
            print(f"Code: {response.status_code}")
            if response.status_code == 401:
                return False, "Authorisation failed!!!! ID or password may have been incorrect"            
            
            if response.status_code == 201:
                return True, ""
            
        except Exception as ex:
            return False, f"{ex}"
            

    def GetPhoto(self, id, page):
        image = None
        try:
            apiUrl = f"http://192.168.0.110:5143/api/Employees/{id}"
            response = requests.get(apiUrl, verify = False, timeout=10)
            
            if response.status_code == 404:
                message = f"No user with id {id} found"
                self.NotFoundSignal.emit(message)
                return
           
            if response.status_code == 200:
                print(page)
                employee = response.json()
                
                id = employee['id']
                _id = str(id)
                id = f"ID number: {_id}"
                
                fname = employee['fname']
                _fname = str(fname)
                fname = f"\nFirst Name: {_fname}"
                
                lname = employee['lname']
                _lname = str(lname)
                lname = f"\nLast Name: {_lname}"
                
                dob = employee['dob']
                _dob = str(dob)
                dob = f"\nDate of birth: {_dob}"
                
                date = employee['createddate']
                _date = str(date)
                date = f"\nEmployee since: {_date}"
                
                date2 = employee['modifieddate']
                _date2 = str(date2)
                date2 = f"\nEmployee information last modified: {_date2}"
                
                try:
                    img = employee['photo']
                    image = base64.b64decode(img)
                except:
                    image = None
                if page == "home":
                    self.HomeImageSignal.emit(image)
                    self.HomeDetailsSignal.emit(id, fname, lname, dob, date, date2)
                if page == "database":
                    self.DatabaseImageSignal.emit(image)
                    self.DatabaseDetailsSignal.emit(id, fname, lname, dob, date, date2)
                if page == "addUser":
                    self.AddUserDetailsSignal.emit(id, fname, lname, dob, date, date2)
                if page == "manual":
                    self.ManualImageSignal.emit(image)
            else:
                print(f"Could not get employee. Status code: {response.status_code}")
                print(f"Response: {response.text}")
        except Exception as ex:
            print(f"API Get photo error: {ex}")
            if page == "home":
                self.HomeImageSignal.emit(image)
            if page == "datbase":
                self.DatabaseImageSignal.emit(image)
            print("s")
            return None
    
    