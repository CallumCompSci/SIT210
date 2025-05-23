
using System.Text.Encodings.Web;
using Microsoft.Extensions.Options;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authorization;
using System.Text;

using Microsoft.AspNetCore.Identity;
using System.Security.Claims;
using MyProject.Models;
using MyProject.Interfaces;



public class BasicAuthenticationHandler : AuthenticationHandler<AuthenticationSchemeOptions>
{
    private readonly ISystemUser _userRepo;

    public BasicAuthenticationHandler(IOptionsMonitor<AuthenticationSchemeOptions> options, ILoggerFactory logger, UrlEncoder encoder, ISystemClock clock, ISystemUser userRepo) : base(options, logger, encoder, clock)
    {
        _userRepo = userRepo;
    }

    protected override Task<AuthenticateResult> HandleAuthenticateAsync()
    {
        var endpoint = Context.GetEndpoint();

        if (endpoint?.Metadata.GetMetadata<AllowAnonymousAttribute>() != null)
        {
            return Task.FromResult(AuthenticateResult.NoResult()); 
        }

        

        base.Response.Headers.Add("WWW-Authenticate", @"Basic realm=""Access to the API.""");
        var authHeader = base.Request.Headers["Authorization"].ToString();
        // Authentication logic will be here.
        string authHeaderNoBasic = null;
        if (authHeader.StartsWith("Basic ", StringComparison.OrdinalIgnoreCase) && authHeader.Length > 6)
        {
            authHeaderNoBasic = authHeader.Substring(6).Trim();
        }
        else
        {
            Response.StatusCode = 401;
            return Task.FromResult(AuthenticateResult.Fail($"Authentication failed."));
        }
        Console.WriteLine(authHeader);

        string utf8AuthHeader;
        byte[] bytes;
        try
        {
            bytes = Convert.FromBase64String(authHeaderNoBasic);
            utf8AuthHeader = Encoding.UTF8.GetString(bytes);
        }
        catch (FormatException)
        {
            return Task.FromResult(AuthenticateResult.Fail("Invalid base64 encoding"));
        }

        Console.WriteLine(utf8AuthHeader);
        
        
        //Get login creds from header
        int id = -1;
        string password = null;
        int colonIndex = utf8AuthHeader.IndexOf(':');
        if (colonIndex >= 0)
        {
            if (int.TryParse(utf8AuthHeader.Substring(0, colonIndex), out int parsedId))
            {
                id = parsedId;
            }
            password = utf8AuthHeader.Substring(colonIndex + 1);
        }
        else
        {
            // Handle missing separator
            return Task.FromResult(AuthenticateResult.Fail("Invalid credentials format"));
        }
        

        //Get user based on email
        
        Systemuser user = _userRepo.GetUser(id);
        if (user == null) 
        {
            Response.StatusCode = 401;
            return Task.FromResult(AuthenticateResult.Fail($"Authentication failed, no user found"));
        }

        Console.WriteLine(id);
        Console.WriteLine(password);
        Console.WriteLine(user.Passwordhash);

        
        var hasher = new PasswordHasher<Systemuser>();
        var pwVerificationResult = hasher.VerifyHashedPassword(user, user.Passwordhash, password);

        if (pwVerificationResult == PasswordVerificationResult.Success)
        {
            var claims = new[]
            {
                new Claim("id", $"{user.SysId}"),
                new Claim(ClaimTypes.Role, user.Isadmin ? "Admin" : "User")
            };
            

            var identity = new ClaimsIdentity(claims, "basic");
            var claimsPrincipal = new ClaimsPrincipal(identity);
            var authTicket = new AuthenticationTicket(claimsPrincipal, Scheme.Name);
            return Task.FromResult(AuthenticateResult.Success(authTicket));
        }
        else
        {
            return Task.FromResult(AuthenticateResult.Fail("Authentication failed, incorrect email or password"));

        }

    }
}
