using System.Collections.Generic;
using System.Threading.Tasks;
using System.Threading;
using CsvHelper;
using CsvHelper.Configuration;
using System.Globalization;
using System.IO;
using System.Linq;

public static class CsvLoader 
{
    public static CsvConfiguration configuration = new(CultureInfo.InvariantCulture)
    {
        Delimiter = ";",
        HeaderValidated = null,
        HasHeaderRecord = false
    };

    public static void AppendData<T>(string file, IEnumerable<T> addedData) 
    {   
        using StreamWriter writer = new(File.Open($"wwwroot/DB/{file}", FileMode.Append));
        using CsvWriter csv = new(writer, configuration);

        csv.WriteRecords(addedData);
    }
    public static void AppendData<T>(string file, T addedData) 
    {   
        using StreamWriter writer = new(File.Open($"wwwroot/DB/{file}", FileMode.Append));
        using CsvWriter csv = new(writer, configuration);

        List<T> list = new();
        list.Add(addedData);

        csv.WriteRecords(list);
    }

    public static async Task<IEnumerable<T>> ReadData<T>(string file)
    {
        using var reader = new StreamReader($"wwwroot/DB/{file}");
        using var csv = new CsvReader(reader, configuration);

        List<T> records = new();

        await foreach (var record in csv.GetRecordsAsync<T>())
            records.Add(record);

        return records;
    }
}
