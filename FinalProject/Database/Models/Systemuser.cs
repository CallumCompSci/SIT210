using System;
using System.Collections.Generic;

namespace MyProject.Models;

public partial class Systemuser
{
    public int SysId { get; set; }

    public bool Isadmin { get; set; }

    public string Passwordhash { get; set; } = null!;

    public DateTime Createddate { get; set; }

    public DateTime Modifieddate { get; set; }
}
