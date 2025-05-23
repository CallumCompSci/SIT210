using Npgsql;
using FastMember;


namespace security_api.Repos;

public interface IRepository
{
    const string CONNECTION_STRING = "Host=localhost;Username=postgres;Password=HelloSIT331;Database=postgres";
    public List<T> ExecuteReader<T>(string sqlCommand, NpgsqlParameter[]dbParams = null) where T : class, new()
    {
        var entities = new List<T>();
        
        using var conn = new NpgsqlConnection(CONNECTION_STRING);
        conn.Open();
        using var cmd = new NpgsqlCommand(sqlCommand, conn);

        if (dbParams is not null)
        {
            cmd.Parameters.AddRange(dbParams.Where(x => x.Value is not null).ToArray());
        }
        using var dr = cmd.ExecuteReader();

        while (dr.Read())
        {
            var entity = new T();
            dr.MapTo(entity);
            entities.Add(entity);
        }

        return entities;
    }

    public void NonQuery(string sqlCommand, NpgsqlParameter[]dbParams = null)
    {
        using var conn = new NpgsqlConnection(CONNECTION_STRING);
        conn.Open();
        using var cmd = new NpgsqlCommand(sqlCommand, conn);

        if (dbParams is not null)
        {
            cmd.Parameters.AddRange(dbParams.Where(x => x.Value is not null).ToArray());
        }
        using var dr = cmd.ExecuteReader();

        cmd.ExecuteNonQuery();
    }
}

