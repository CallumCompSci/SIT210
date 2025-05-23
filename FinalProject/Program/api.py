from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from flask import Flask, request, jsonify
import threading
import socket


class FlaskThread(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self, daemon=True)
        self.app = app
        self.server = None
        self._stop_event = threading.Event()
        
    def run(self):
        try:
            self.app.run(host='0.0.0.0', port=5001, debug=False, use_reloader=False)
        except Exception as e:
            print(f"Flask error: {str(e)}")
            
    def stop(self):
        self._stop_event.set()
        # Try to shut down Flask by connecting to it
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 5001))
            sock.close()
        except:
            pass
    
    
    
class Api(QThread):
    
    image_received = Signal(str, bytes)
    result_received = Signal(str)
    empImage_received = Signal(bytes)
    
    def __init__(self):
        super().__init__()
        self.app = Flask(__name__)
        
        @self.app.route('/photo', methods=['POST'])
        def send_photo():
            if 'image' not in request.files:
                return jsonify("No image in request")
            
            file = request.files['image']
            
            
            id_number = request.form['id']  # Get the integer from form data
            id = str(id_number)
            
            
            img = file.read()
            self.image_received.emit(id, img)
                
            return jsonify({"message": "Success"}), 200
        
        @self.app.route('/result', methods=['POST'])
        def getResult():
            if 'result' not in request.form:
                return jsonify("No result")
            
            result = request.form['result']
            _result = str(result)
            print(f"Result: {_result}")
            self.result_received.emit(_result)
            return jsonify({"message": "Success"}), 200
        
        @self.app.route('/empPhoto', methods=['POST'])
        def send_empPhoto():
            if 'image' not in request.files:
                return jsonify("No image in request")
            
            file = request.files['image']

            img = file.read()
            self.empImage_received.emit(img)
                
            return jsonify({"message": "Success"}), 200
        
        
        @self.app.route('/shutdown')
        def shutdown():
            self.shutdown_server()
            return 'Server shutting down...'
        
        self.flaskThread = FlaskThread(self.app)
        
        
    def run(self):
        self.flaskThread.start()
        
        
    def shutdown_server(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        
    def stop(self):
        self.flaskThread.stop()

