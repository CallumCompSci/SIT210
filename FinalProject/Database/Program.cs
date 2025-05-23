using Microsoft.OpenApi.Models;
using MyProject.Contexts;
using System.Reflection;
using Microsoft.EntityFrameworkCore;
using MyProject.Interfaces;
using MyProject.Models;
using MyProject.Repos;
using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;  


var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenApi();

builder.Services.AddControllers();

builder.Services.AddEndpointsApiExplorer();


var connectionString =
    builder.Configuration.GetConnectionString("DefaultConnection")
        ?? throw new InvalidOperationException("Connection string"
        + "'DefaultConnection' not found.");

builder.Services.AddDbContext<DatabaseContext>(options =>
    options.UseNpgsql(connectionString));

builder.Services.AddScoped<IEmployee, EmployeeEF>();
builder.Services.AddScoped<ISystemUser, SysUserEF>();
builder.Services.AddScoped<IEntry, EntryEF>();


//* Needs to be in the place of localhost, this explains why the Pi couldnt reach the api
builder.WebHost.UseUrls("http://*:5143", "https://*:5144");

builder.Services.AddAuthentication("BasicAuthentication").AddScheme<AuthenticationSchemeOptions, BasicAuthenticationHandler>("BasicAuthentication", default);

builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("AdminOnly", policy =>
    policy.RequireClaim(ClaimTypes.Role, "Admin"));
    options.AddPolicy("UserOnly", policy =>
    policy.RequireClaim(ClaimTypes.Role, "Admin", "User"));
});



var app = builder.Build();



app.MapControllers();

app.UseAuthentication();
app.UseAuthorization();


app.UseHttpsRedirection();


app.Run();
