using System;
using System.Collections.Generic;
using System.Linq;

using System.Text;

namespace RandContraction
{
	public static class RandContraction
	{
		private const int _totalRuns = 500;

		public static int CountMinCut(List<List<int>> ajListLocked)
		{
            Random r = new Random();
			int min = Int32.MaxValue;

            if (ajListLocked.Count < 2)
				throw new ArgumentException("ajList doesn't have enough elements"); // guard

			for (int i = 0; i < _totalRuns; i++)
			{
                List<List<int>> ajList = DeepCopy(ajListLocked);
                int nonEmptyCount = ajList.Count;

				while (nonEmptyCount > 2)
				{
					int v1ind = r.Next(0, nonEmptyCount);
					List<int> v1 = ajList.Where(v => v != null).ToList()[v1ind];
					v1ind = ajList.IndexOf(v1);

					int v2_in_v1_index = r.Next(0, v1.Count);
					List<int> v2 = ajList[v1[v2_in_v1_index]];
					int v2ind = ajList.IndexOf(v2);

					// cutting v2 vertex while preserving its edges
                    ajList.ForEach(v =>
						{
							if (v != null)
								for (int j = 0; j < v.Count; j++)
									if (v[j] == v2ind)
									{
										v[j] = v1ind;
										v1.Add(ajList.IndexOf(v));
									}
						});

					ajList[v1ind] = v1.Where(el => el != v1ind).ToList(); // removing self-references to v1
					ajList[v2ind] = null;

					nonEmptyCount--;
				}

				int minCandidate = ajList.FirstOrDefault(v => v != null).Count;
                if (min > minCandidate)
                {
                    min = minCandidate;
                    Console.WriteLine("{0} attempt: new min cut = {1}", i, min);
                }
			}

			return min;
		}

        private static List<List<int>> DeepCopy(List<List<int>> ajList)
        {
            List<List<int>> newList = new List<List<int>>();
            ajList.ForEach((internalList) =>
            {
                List<int> l2 = new List<int>();
                l2.AddRange(internalList.ToArray());
                newList.Add(l2);
            });

            return newList;
        }
	}
}
