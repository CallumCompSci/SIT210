using MyProject.Models;
using MyProject.Repos;
using MyProject.Interfaces;
using MyProject.Controllers;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Authorization;

namespace MyProject.Controllers
{
    [Route("api/SysUser")]
    [ApiController]
    public class SystemUserController : ControllerBase
    {
        private readonly ISystemUser _UserRepo;
        private readonly IEmployee _EmployeeRepo;
        public SystemUserController(ISystemUser UserRepo, IEmployee EmployeeRepo)
        {
            _UserRepo = UserRepo;
            _EmployeeRepo = EmployeeRepo;
        }


        [Authorize(Policy = "AdminOnly")]
        [HttpGet()]
        public ActionResult<IEnumerable<Systemuser>> GetUsers()
        {
            List<Systemuser> users = new List<Systemuser>();
            users = _UserRepo.GetUsers();
            users.Sort((e1, e2) => e1.SysId.CompareTo(e2.SysId));
            return Ok(users);
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpGet("{id}", Name = "GetUser")]
        public IActionResult GetUser(int id)
        {
            var user = _UserRepo.GetUser(id);
            if (user == null) { return NotFound("No user with matching id found"); }
            return Ok(user);
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpGet("FullUser/{id}")]
        public ActionResult<IEnumerable<Systemuser>> GetFullUser(int id)
        {
            var user = _UserRepo.GetUser(id);
            if (user == null) { return NotFound("No SysUser with matching ID found"); }

            var employee = _EmployeeRepo.GetEmployee(id);
            if (employee == null) { return NotFound("No employee with that ID found"); }

            Combined FullUser = _UserRepo.GetFullUser(id);

            return Ok(FullUser);
        }


        [Authorize(Policy = "AdminOnly")]
        [HttpPost("")]
        public IActionResult AddUser(Systemuser user)
        {
            if (user == null) { return BadRequest("User cannot be null"); }
            if (user.SysId < 0) { return BadRequest("SysID cannot be negative"); }
            var _user = _UserRepo.GetUser(user.SysId);
            if (_user != null) { return BadRequest("User with matching id already exists"); }

            user.Createddate = DateTime.Now;
            user.Modifieddate = DateTime.Now;

            try
            {
                _UserRepo.AddSystemUser(user);
                return CreatedAtRoute("GetUser", new { id = user.SysId }, user);

            }
            catch (Exception ex)
            {
                return BadRequest($"Exception: {ex}");
            }

        }

        [Authorize(Policy = "AdminOnly")]
        [HttpPatch("ChangeAdmin/{id}")]
        public IActionResult ChangeUserAdmin(int id)
        {
            var user = _UserRepo.GetUser(id);
            if (user == null) { return NotFound("No user with matching ID found"); }

            _UserRepo.ChangeUserAdmin(id);

            return NoContent();

        }


        [Authorize(Policy = "AdminOnly")]
        [HttpPatch("PatchUserPassword")]
        public IActionResult PatchSysUser(string password, int id)
        {
            var user = _UserRepo.GetUser(id);
            if (user == null) { return NotFound("No user with matching ID found"); }

            _UserRepo.PatchSysUser(password, id);

            return NoContent();
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpDelete()]
        public IActionResult DeleteUser(int id)
        {
            var user = _UserRepo.GetUser(id);
            if (user == null) { return NotFound("No user with matching ID found"); }

            _UserRepo.DeleteSystemUser(id);

            return NoContent();

        }

        [AllowAnonymous]
        [HttpPost("Verify")]
        public IActionResult VerifyUser([FromBody] Login login )
        {
            var user = _UserRepo.GetUser(login.id);
            if (user == null) { return NotFound("No user with matching ID found"); }
            bool result = _UserRepo.VerifyUser(login.id, login.password);
            return Ok(result);

        }















    }

}
