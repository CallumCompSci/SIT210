namespace MyProject.Models;


public class Combined
{
    public int Id { get; set; }

    public int SysId { get; set; }
    public bool Isadmin { get; set; }

    public string Fname { get; set; } = null!;

    public string Lname { get; set; } = null!;

    public DateOnly Dob { get; set; }

    public DateTime Createddate { get; set; }

    public DateTime Modifieddate { get; set; }
    public DateTime SysCreateddate { get; set; }

    public DateTime SysModifieddate { get; set; }

    public byte[]? Photo { get; set; }


    public Combined(int Id, int SysId, bool IsAdmin, string Fname, string Lname, DateOnly Dob, DateTime Createddate, DateTime Modifieddate, DateTime SysCreateddate, DateTime SysModifieddate, byte[]? Photo)
    {
        this.Id = Id;
        this.SysId = SysId;
        this.Isadmin = IsAdmin;
        this.Fname = Fname;
        this.Lname = Lname;
        this.Dob = Dob;
        this.Createddate = Createddate;
        this.Modifieddate = Modifieddate;
        this.SysModifieddate = SysModifieddate;
        this.SysCreateddate = SysCreateddate;
        this.Photo = Photo;
    }
    

}