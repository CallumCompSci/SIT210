using System;
using MyProject.Models;
using MyProject.Interfaces;
using MyProject.Contexts;

namespace MyProject.Repos;

public class EmployeeEF : IEmployee
{
    private readonly DatabaseContext _context;

    public EmployeeEF(DatabaseContext context)
    {
        _context = context;
    }


    public List<Employee> GetEmployees()
    {
        return _context.Employees.ToList();
    }

    public Employee GetEmployee(int _id)
    {
        return _context.Employees.Where(Employees => Employees.Id == _id).FirstOrDefault();
    }

    public Employee AddEmployee(Employee employee)
    {
        _context.Employees.Add(employee);
        _context.SaveChanges();
        return employee;
    }

    public Employee UpdateEmployee(Employee updatedEmployee, int _id)
    {
        var _employee = _context.Employees.First(m => m.Id == _id);
        _employee.Fname = updatedEmployee.Fname;
        _employee.Lname = updatedEmployee.Lname;
        _employee.Dob = updatedEmployee.Dob;
        _employee.Modifieddate = DateTime.Now;
        _employee.Photo = updatedEmployee.Photo;

        _context.SaveChanges();
        
        return updatedEmployee;
    }

    public void DeleteEmployee(int _id)
    {
        var _employee = _context.Employees.First(m => m.Id == _id);
        _context.Employees.Remove(_employee);
        _context.SaveChanges();
    }
    
}
