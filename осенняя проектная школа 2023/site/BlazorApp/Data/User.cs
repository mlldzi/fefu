using System.Collections.Generic;
using System.Threading.Tasks;
using System.Threading;
using System;
using CsvHelper;
using CsvHelper.TypeConversion;
using CsvHelper.Configuration;
using System.Globalization;
using System.IO;
using System.Linq;


public class User 
{
    public string Login { get; set; }
    public string Password { get; set; }
    public string Name { get; set; }
    public string Gender { get; set; }
    public int Age { get; set; }
    public string Location { get; set; }
    public string Telegram { get; set; }
    public string MainHobbies { get; set; }

    public IEnumerable<Hobby> GetMainHobbies()
    {
        if (string.IsNullOrEmpty(MainHobbies))
            return Enumerable.Empty<Hobby>();

        return MainHobbies.Split(',')
                          .Select(s => (Hobby)Enum.Parse(typeof(Hobby), s.Trim(), ignoreCase: true));
    }

}

public enum Hobby {
    Football = 1,
    Hockey,
    Snowboarding,
    Anime,
    GuitarPlaying,
    Startups,
    Cooking,
    Fishing,
    BoardGames,
    DungeonsAndDragons,
    Cars,
    HandAndCrafts,
    Dancing,
    Hunting,
    Tourism,
    Drawing,
    Music,
    HobbyHorsing,
    Blogging,
    Shows,
    Movies,
    Reading,
    GraphicDesign,
    Photography,
    ElectronicsAndRobotics,
    Alcohol,
    Parkour,
    Fencing,
    Yoga,
    HorseRiding
}