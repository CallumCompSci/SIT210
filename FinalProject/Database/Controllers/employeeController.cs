using MyProject.Models;
using MyProject.Repos;
using MyProject.Interfaces;
using MyProject.Controllers;
using Microsoft.AspNetCore.Authorization;


using Microsoft.AspNetCore.Mvc;

namespace MyProject.Controllers;


[Route("api/Employees")]
[ApiController]

public class EmployeeController : ControllerBase
{
    private readonly IEmployee _EmployeeRepo;
    public EmployeeController(IEmployee EmployeeRepo)
    {
        _EmployeeRepo = EmployeeRepo;
    }

    [AllowAnonymous]
    [HttpGet()]
    public ActionResult<IEnumerable<Employee>> GetEmployees()
    {
        List<Employee> employees = new List<Employee>();
        employees = _EmployeeRepo.GetEmployees();
        employees.Sort((e1, e2) => e1.Id.CompareTo(e2.Id));
        return Ok(employees);
    }

    [AllowAnonymous]
    [HttpGet("{id}", Name = "GetEmployee")]
    public IActionResult GetEmployeeId(int id)
    {
        var employee = _EmployeeRepo.GetEmployee(id);
        if (employee == null) { return NotFound("No employee with matching id found"); }
        return Ok(employee);
    }

    [Authorize(Policy = "AdminOnly")]
    [HttpPost("AddEmployee")]
    public IActionResult AddEmployee(Employee employee)
    {
        if (employee == null) { return BadRequest("Employee cannot be null"); }
        if (employee.Id < 0) { return BadRequest("Id must be greater than 1"); }

        employee.Createddate = DateTime.Now;
        employee.Modifieddate = DateTime.Now;


        try
        {
            _EmployeeRepo.AddEmployee(employee);
            return CreatedAtRoute("GetEmployee", new { id = employee.Id }, employee);
        }
        catch (Exception ex)
        {
            return BadRequest($"Exception: {ex}");
        }

    }

    [Authorize(Policy = "AdminOnly")]
    [HttpPut("{id}")]
    public IActionResult UpdateEmployee(Employee updatedEmployee, int id)
    {
        if (updatedEmployee == null) { return BadRequest("Employee cannot be null"); }
        if (updatedEmployee.Id < 0) { return BadRequest("Id must be greater than 1"); }
        var _employee = _EmployeeRepo.GetEmployee(id);
        if (_employee == null) { return BadRequest($"No employee with the id: {id} exists"); }
        try
        {
            _EmployeeRepo.UpdateEmployee(updatedEmployee, id);
            return NoContent();
        }
        catch (Exception ex)
        {
            return BadRequest($"Exception: {ex}");
        }
    }

    [Authorize(Policy = "AdminOnly")]
    [HttpDelete("{id}")]
    public IActionResult DeleteEmployee(int id)
    {
        if (id < 0) { return BadRequest("Id must be greater than 1"); }
        var _employee = _EmployeeRepo.GetEmployee(id);
        if (_employee == null) { return BadRequest($"No employee with the id: {id} exists"); }
        try
        {
            _EmployeeRepo.DeleteEmployee(id);
            return NoContent();
        }
        catch (Exception ex)
        {
            return BadRequest($"Exception: {ex}");
        }
    }






}