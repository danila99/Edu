using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hash
{
    public static class Sums
    {
        public static ushort Count(long[] positive, long[] negative)
        {
            Dictionary<long, byte> negatives = new Dictionary<long, byte>();
            positive = positive.Distinct().ToArray();

            ushort result = 0;

            foreach (long i in negative)
                if (!negatives.ContainsKey(i))
                    negatives.Add(i, 1);

            int total = 20000 + 1;
            int c = 0;

            foreach (long t in Enumerable.Range(-10000, total))
            {
                c++;
                if (c % (total / 100) == 0)
                    Console.WriteLine("iteration: {0}, result so far: {1}", c, result);

                if (CheckRange(positive, negatives, t))
                    result++;
            }

            return result;
        }

        private static bool CheckRange(long[] positive, Dictionary<long, byte> negatives, long t)
        {
            foreach (long x in positive)
            {
                // x+y=t
                if (negatives.ContainsKey(t - x))
                    return true;
            }

            return false;
        }
    }
}
