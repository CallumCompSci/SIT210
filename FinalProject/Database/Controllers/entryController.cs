using MyProject.Models;
using MyProject.Repos;
using MyProject.Interfaces;
using MyProject.Controllers;
using Microsoft.AspNetCore.Authorization;


using Microsoft.AspNetCore.Mvc;

namespace MyProject.Controllers;


[Route("api/Entries")]
[ApiController]

public class EntryController : ControllerBase
{
    private readonly IEntry _EntryRepo;
    public EntryController(IEntry EntryRepo)
    {
        _EntryRepo = EntryRepo;
    }


    [HttpGet()]
    public ActionResult<IEnumerable<Entry>> GetEntries()
    {
        List<Entry> entries = new List<Entry>();
        entries = _EntryRepo.GetEntries();
        entries.Sort((e2, e1) => e1.Entrynum.CompareTo(e2.Entrynum));
        return Ok(entries);
    }
    
    [AllowAnonymous]
    [HttpGet("GetXEntries/{amount}/{id}")]
    public ActionResult<IEnumerable<Entry>> GetXEntries(int amount, int id)
    {
        List<Entry> entries = new List<Entry>();
        entries = _EntryRepo.GetCertainEntries(id);
        entries.Sort((e2, e1) => e1.Entrynum.CompareTo(e2.Entrynum));
        if (entries.Count > amount)
        {
            entries.RemoveRange(amount, entries.Count - amount);
        }
        return Ok(entries);
    }


    [AllowAnonymous]
    [HttpGet("{id}", Name = "GetEntry")]
    public IActionResult GetEntry(int id)
    {
        var entry = _EntryRepo.GetEntry(id);
        if (entry == null) { return NotFound("No entry with matching id found"); }
        return Ok(entry);
    }

    [HttpGet("GetManualEntries")]
    public ActionResult<IEnumerable<Entry>> GetManualEntries()
    {
        List<Entry> entries = new List<Entry>();
        entries = _EntryRepo.GetCertainEntries(-2);
        entries.Sort((e1, e2) => e1.Entrynum.CompareTo(e2.Entrynum));
        return Ok(entries);
    }

    [AllowAnonymous]
    [HttpPost("AddEntry")]
    public IActionResult AddEntry(Entry entry)
    {
        Console.WriteLine(entry.Entrytime);
        Console.WriteLine(entry.Entrynum);
        Console.WriteLine(entry.Employeeid);
        if (entry == null) { return BadRequest("Entry cannot be null"); }
        if (entry.Sysuserid <= 0) { return BadRequest("Sys Id must be higher than 1"); }

        try
        {
            _EntryRepo.AddEntry(entry);
            return CreatedAtRoute("GetEntry", new { id = entry.Entrynum }, entry);
        }
        catch (Exception ex)
        {
            return BadRequest($"Exception: {ex}");
        }

    }

    [Authorize(Policy = "AdminOnly")]
    [HttpPatch("{id}")]
    public IActionResult patchEntry(int id, bool manualEntry, string comment, int sysID)
    {
        if (comment == null) { return BadRequest("Comment cannot be null"); }
        if (sysID < 0) { return BadRequest("Id must be greater than 1"); }
        var _entry = _EntryRepo.GetEntry(id);
        if (_entry == null) { return BadRequest($"No entry with the id: {id} exists"); }
        try
        {
            _EntryRepo.patchEntry(id, manualEntry, comment, sysID);
            return NoContent();
        }
        catch (Exception ex)
        {
            return BadRequest($"Exception: {ex}");
        }
    }

    [Authorize(Policy = "AdminOnly")]
    [HttpDelete("{id}")]
    public IActionResult DeleteEntry(int id)
    {
        if (id < 0) { return BadRequest("Id must be greater than 1"); }
        var _entry = _EntryRepo.GetEntry(id);
        if (_entry == null) { return BadRequest($"No entry with the id: {id} exists"); }
        try
        {
            _EntryRepo.deleteEntry(id);
            return NoContent();
        }
        catch (Exception ex)
        {
            return BadRequest($"Exception: {ex}");
        }
    }






}