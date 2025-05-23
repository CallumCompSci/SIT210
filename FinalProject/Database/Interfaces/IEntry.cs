using MyProject.Models;

namespace MyProject.Interfaces;

public interface IEntry
{
    List<Entry> GetEntries();
    List<Entry> GetCertainEntries(int id);
    Entry GetEntry(int id);
    Entry AddEntry(Entry entry);
    void patchEntry(int id, bool manualEntry, string comment, int sysID);
    void deleteEntry(int id);
}