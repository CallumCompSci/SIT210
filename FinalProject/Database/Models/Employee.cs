using System;
using System.Collections.Generic;

namespace MyProject.Models;

public partial class Employee
{
    public int Id { get; set; }

    public string Fname { get; set; } = null!;

    public string Lname { get; set; } = null!;

    public DateOnly Dob { get; set; }

    public DateTime Createddate { get; set; }

    public DateTime Modifieddate { get; set; }

    public byte[]? Photo { get; set; }
}
