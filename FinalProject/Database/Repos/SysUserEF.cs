using System;
using Microsoft.AspNetCore.Identity;
using MyProject.Contexts;
using MyProject.Interfaces;
using MyProject.Models;

namespace MyProject.Repos;

public class SysUserEF : ISystemUser
{
    private readonly DatabaseContext _context;

    public SysUserEF(DatabaseContext context)
    {
        _context = context;
    }

    public List<Systemuser> GetUsers()
    {
        return _context.Systemusers.ToList();
    }

    public Systemuser GetUser(int id)
    {
        return _context.Systemusers.Where(systemuser => systemuser.SysId == id).FirstOrDefault();
    }

    public Combined GetFullUser(int id)
    {
        var user = _context.Systemusers.Where(systemuser => systemuser.SysId == id).FirstOrDefault();
        var employee = _context.Employees.Where(employee => employee.Id == id).FirstOrDefault();

        Combined FullUser = new Combined(employee.Id, user.SysId, user.Isadmin, employee.Fname, employee.Lname, employee.Dob, employee.Createddate, employee.Modifieddate, user.Createddate, user.Modifieddate, employee.Photo);
        return FullUser;
    }



    public Systemuser AddSystemUser(Systemuser newUser)
    {
        //Always set new user to NOT be an admin, must manually change later
        newUser.Isadmin = false;
        //Hash the password, otherwise passwordhash will be the unhashed password
        var password = newUser.Passwordhash;
        var hasher = new PasswordHasher<Systemuser>();
        var pwHash = hasher.HashPassword(newUser, password);
        var pwVerificationResult = hasher.VerifyHashedPassword(newUser, pwHash, password);
        newUser.Passwordhash = pwHash;

        newUser.Createddate = DateTime.Now;
        newUser.Createddate = DateTime.Now;
        _context.Systemusers.Add(newUser);
        _context.SaveChanges();
        return newUser;
    }

    public void ChangeUserAdmin(int _id)
    {
        var _user = _context.Systemusers.First(m => m.SysId == _id);
        _user.Isadmin = !_user.Isadmin;
        _user.Modifieddate = DateTime.Now;

        _context.SaveChanges();

    }

    public void PatchSysUser(string password, int _id)
    {
        var _user = _context.Systemusers.First(m => m.SysId == _id);

        var hasher = new PasswordHasher<Systemuser>();
        var pwHash = hasher.HashPassword(_user, password);
        var pwVerificationResult = hasher.VerifyHashedPassword(_user, pwHash, password);

        password = pwHash;
        _user.Passwordhash = password;

        _context.SaveChanges();
    }

    public void DeleteSystemUser(int _id)
    {
        var _user = _context.Systemusers.First(m => m.SysId == _id);
        _context.Systemusers.Remove(_user);
        _context.SaveChanges();
    }

    public bool VerifyUser(int id, string password)
    {
        var _user = _context.Systemusers.First(m => m.SysId == id);
        var hasher = new PasswordHasher<Systemuser>();
        var pwVerificationResult = hasher.VerifyHashedPassword(_user, _user.Passwordhash, password);
        if (pwVerificationResult == PasswordVerificationResult.Success) { return true; }
        else { return false; }

    }



}
