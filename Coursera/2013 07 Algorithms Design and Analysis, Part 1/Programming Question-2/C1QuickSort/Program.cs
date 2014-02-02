using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace C1QuickSort
{
	class Program
	{
		private const string _path = @"C:\Work\VM\C1QuickSort\QuickSort.txt";
		//private const string _path = @"C:\Work\VM\C1QuickSort\100-1.txt";
		
		static void Main(string[] args)
		{
			List<int> arr = new List<int>();

			using (StreamReader sr = new StreamReader(_path))
			{
				string line;
				int num;

				while ((line = sr.ReadLine()) != null)
				{
					if (Int32.TryParse(line, out num))
						arr.Add(num);
				}
			}

			QuickSort.PivotLogic = PivotLogic.First;
			int comparisions = QuickSort.Sort(arr.ToArray());
			Console.WriteLine("PivotLogic.First: " + comparisions);

			QuickSort.PivotLogic = PivotLogic.Last;
			comparisions = QuickSort.Sort(arr.ToArray());
			Console.WriteLine("PivotLogic.Last: " + comparisions);

			QuickSort.PivotLogic = PivotLogic.Median;
			comparisions = QuickSort.Sort(arr.ToArray());
			Console.WriteLine("PivotLogic.Median: " + comparisions);
		}
	}
}
