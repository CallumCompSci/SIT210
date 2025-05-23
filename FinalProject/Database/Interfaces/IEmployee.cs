using MyProject.Models;

namespace MyProject.Interfaces;

public interface IEmployee
{
    List<Employee> GetEmployees();
    Employee GetEmployee(int _id);
    Employee AddEmployee(Employee employee);
    Employee UpdateEmployee(Employee updatedEmployee, int _id);
    void DeleteEmployee(int Id);
}