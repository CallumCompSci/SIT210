using System.ComponentModel.Design;
using MyProject;
using MyProject.Interfaces;
using Npgsql;
using security_api.Repos;
using MyProject.Models;



public class EmployeeRepository : IEmployee, IRepository
{
    private IRepository _repo => this;

    public List<Employee> GetEmployees()
    {
        var employees = _repo.ExecuteReader<Employee>("SELECT id, fname, lane, dob, createddeate, modifieddate, photo FROM employees");
        return employees;
    }

    public Employee GetEmployee(int id)
    {
        var sqlParams = new[]{ new NpgsqlParameter("id", id)};
        var employee = _repo.ExecuteReader<Employee>("SELECT id, fname, lane, dob, createddeate, modifieddate, photo FROM employees WHERE id=@id");
        return employee.SingleOrDefault();
    }

    public Employee AddEmployee(Employee newEmployee)
    {
        var sqlParams = new NpgsqlParameter[]{new("fname", newEmployee.Fname),new ("lname", newEmployee.Lname), new("dob", newEmployee.Dob), new("createddate", DateTime.Now), new("modifieddate", DateTime.Now), new("photo", newEmployee.Photo)};
        var result = _repo.ExecuteReader<Employee>( "INSERT INTO employees (fname, lname, dob, modifieddate, createddate, photo) VALUES (@fname, @lname, @dob, @createddate, @modifieddate, @photo) RETURNING id;", sqlParams).Single();
        return result;
    }

    public Employee UpdateEmployee(Employee updatedEmployee, int id)
    {
        var sqlParams = new NpgsqlParameter[]{new("id", id), new("fname", updatedEmployee.Fname), new ("lname", updatedEmployee.Lname), new("dob", updatedEmployee.Dob), new("createddate", DateTime.Now), new("modifieddate", DateTime.Now), new("photo", updatedEmployee.Photo)};
        var result = _repo.ExecuteReader<Employee>( "UPDATE employees SET fname=@fname, lname=@lname, dob=@dob, createddate=@createddate, modifieddate=@modifieddate, photo=@photo WHERE id=@id RETURNING *;", sqlParams).Single();
        return result;
    }

    public void DeleteEmployee(int id)
    {
        var sqlParams = new NpgsqlParameter[]{new("id", id)};
        _repo.NonQuery("DELETE FROM employees WHERE id = @id", sqlParams);  
    }

}