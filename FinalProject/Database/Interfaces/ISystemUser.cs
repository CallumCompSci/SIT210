using MyProject.Models;

namespace MyProject.Interfaces;

public interface ISystemUser
{
    List<Systemuser> GetUsers();
    Systemuser GetUser(int _id);
    Combined GetFullUser(int _id);
    Systemuser AddSystemUser(Systemuser user);
    void ChangeUserAdmin(int _id);
    void PatchSysUser(string password, int _id);
    void DeleteSystemUser(int _id);
    bool VerifyUser(int id, string password);
}