using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace RandContraction
{
	class Program
	{
        private const string _path = @"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-3\kargerMinCut.txt";
		
		static void Main(string[] args)
		{
			List<List<int>> ajList = new List<List<int>>();

			using (StreamReader sr = new StreamReader(_path))
			{
				string line;

				while ((line = sr.ReadLine()) != null)
				{
					List<int> list = new List<int>();
					var vals = line.Split('\t').Skip(1);
					int i;

					foreach (string s in vals)
						if (Int32.TryParse(s, out i))
							list.Add(i - 1);

					if (list.Count() != 0)
						ajList.Add(list);
				}
			}

			int c = RandContraction.CountMinCut(ajList);

			Console.WriteLine("Done. Min cut = " + c);
		}
	}
}
