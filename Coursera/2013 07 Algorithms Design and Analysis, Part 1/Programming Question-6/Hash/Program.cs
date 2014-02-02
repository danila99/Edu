using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hash
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CountSums();
            //CountMediansMod();
        }

        private static void CountSums()
        {
            var positive = ReadIntegers(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-6\algo1_programming_prob_2sum.txt", true);
            var negative = ReadIntegers(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-6\algo1_programming_prob_2sum.txt", false);

            Console.WriteLine(Sums.Count(positive, negative));
        }

        private static void CountMediansMod()
        {
            var positive = ReadIntegers(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-6\Median.txt", true);

            Console.WriteLine(Median.CountMedianMod(positive, 10000));
        }


        public static long[] ReadIntegers(string path, bool isPositive)
        {
            Console.WriteLine("reading longs from: " + path);
            List<long> result = new List<long>();
            
            using (StreamReader sr = new StreamReader(path))
            {
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    long i = Int64.Parse(line);
                    
                    if (isPositive && i > 0)
                        result.Add(i);
                    if (!isPositive && i < 0)
                        result.Add(i);
                }
            }

            Console.WriteLine("longs read: {0} ({1})", result.Count(), (isPositive ? "positives" : "negatives"));
            return result.ToArray();
        }
    }
}
