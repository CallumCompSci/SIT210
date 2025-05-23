using System;
using System.Collections.Generic;

namespace MyProject.Models;

public partial class Entry
{
    public int Entrynum { get; set; }

    public int Employeeid { get; set; }

    public DateTime? Entrytime { get; set; }

    public bool Manualentry { get; set; }

    public string? Comment { get; set; }

    public int? Sysuserid { get; set; }
}
