using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SplitInversion
{
    class Program
    {
        private static readonly string _file = @"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-1\IntegerArray.txt";
        
        static void Main(string[] args)
        {
            List<int> arr = new List<int>();
            using (StreamReader sr = new StreamReader(_file))
            {
                String line;
                while ((line = sr.ReadLine()) != null)
                {
                    int num = 0;
                    if (Int32.TryParse(line, out num))
                        arr.Add(num);
                }
            }

            Console.WriteLine("Total numbers: " + arr.Count());
            Console.WriteLine("Inversions: " + InversionsCalculator.Count(arr.ToArray()));
            Console.ReadKey();
        }


    }
}
