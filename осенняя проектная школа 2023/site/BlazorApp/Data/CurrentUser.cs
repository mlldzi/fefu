using Microsoft.Extensions.DependencyInjection;

namespace Services
{
    public class AppData
    {
        public User CurrentUser { get; set; }
        
        public AppData() =>
            CurrentUser = new User();
    }
}