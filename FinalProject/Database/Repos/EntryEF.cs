using System;
using MyProject.Models;
using MyProject.Interfaces;
using MyProject.Contexts;

namespace MyProject.Repos;

public class EntryEF : IEntry
{
    private readonly DatabaseContext _context;

    public EntryEF(DatabaseContext context)
    {
        _context = context;
    }


    public List<Entry> GetEntries()
    {
        return _context.Entries.ToList();
    }

    public Entry GetEntry(int _id)
    {
        return _context.Entries.Where(Entries => Entries.Entrynum == _id).FirstOrDefault();
    }

    public List<Entry> GetCertainEntries(int id)
    {
        if (id == 0)
        {
            return _context.Entries.ToList();
        }
        if (id == -1)
        {
            return _context.Entries.Where(Entries => Entries.Employeeid == id).ToList();
        }
        if (id == -2)
        {
            return _context.Entries.Where(Entries => Entries.Manualentry == true).ToList();
        }
        else
        {
            return _context.Entries.Where(Entries => Entries.Employeeid == id).ToList();
        }
        
    }

    public Entry AddEntry(Entry entry)
    {
        entry.Entrytime = DateTime.Now;
        if (entry.Manualentry != true)
        {
            entry.Manualentry = false;
        }
        _context.Entries.Add(entry);
        _context.SaveChanges();
        return entry;
    }

    public void patchEntry(int _id, bool manualEntry, string comment, int sysId)
    {
        var _entry = _context.Entries.First(m => m.Entrynum == _id);
        _entry.Manualentry = manualEntry;
        _entry.Comment = comment;
        _entry.Sysuserid = sysId;

        _context.SaveChanges();
    }

    public void deleteEntry(int _id)
    {
        var _entry = _context.Entries.First(m => m.Entrynum == _id);
        _context.Entries.Remove(_entry);
        _context.SaveChanges();
    }
    
}
