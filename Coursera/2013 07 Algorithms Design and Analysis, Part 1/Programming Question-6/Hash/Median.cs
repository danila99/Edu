using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hash
{
    public static class Median
    {
        public static long CountMedianMod(long[] arr, int mod)
        {
            SortedList<long, byte> sorted = new SortedList<long, byte>();
            List<long> medians = new List<long>();

            foreach (long l in arr)
            {
                sorted.Add(l, 1);

                int medianIndex = sorted.Keys.Count % 2 == 0
                    ? sorted.Keys.Count / 2
                    : ((sorted.Keys.Count + 1) / 2);

                //Console.WriteLine(sorted.Keys[medianIndex - 1]);
                medians.Add(sorted.Keys[medianIndex - 1]);
            }

            return medians.Sum() % mod;
        }
    }
}
