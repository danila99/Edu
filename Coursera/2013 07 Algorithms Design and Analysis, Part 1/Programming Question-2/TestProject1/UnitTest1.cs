using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using C1QuickSort;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace TestProject1
{
	[TestClass]
	public class UnitTest1
	{
		[TestMethod]
		public void TestMethodSmallAndFirst()
		{
			var reference = new int[] {1, 2, 4, 6};
			var arr1 = new int[] {2, 4, 1, 6};
			var comparisions = QuickSort.Sort(arr1);

			for (int i =0; i < reference.Length; i++)
			{
				Assert.AreEqual(reference[i], arr1[i]);
			}
		}

		[TestMethod]
		public void TestMethodFirst()
		{
			TestMethod(PivotLogic.First);
		}

		[TestMethod]
		public void TestMethodLast()
		{
			TestMethod(PivotLogic.Last);
		}

		[TestMethod]
		public void TestMethodMedian()
		{
			TestMethod(PivotLogic.Median);
		}

		public void TestMethod(PivotLogic logic)
		{
			const int arrLength = 100;
			Random rnd = new Random();
			var reference = Enumerable.Range(0, arrLength - 1).ToArray();

			QuickSort.PivotLogic = logic;
			var arr1 = Enumerable.Range(0, arrLength - 1).OrderBy(r => rnd.Next()).ToArray();
			QuickSort.Sort(arr1);
			for (int i = 0; i < reference.Length; i++)
				Assert.AreEqual(reference[i], arr1[i]);
		}

		//[TestMethod]
		//public void TestPivot()
		//{
		//    //Assert.AreEqual(1, QuickSort.ChoosePivot(Enumerable.Range(0, 3).ToArray(), 0, 3));
		//    //Assert.AreEqual(2, QuickSort.ChoosePivot(Enumerable.Range(0, 4).ToArray(), 0, 4));
		//    //Assert.AreEqual(4, QuickSort.ChoosePivot(Enumerable.Range(0, 9).ToArray(), 0, 9));

		//    QuickSort.PivotLogic = PivotLogic.Median;
		//    var arr = new int[] {8, 2, 4, 5, 7, 1};
		//    Assert.AreEqual(2, QuickSort.ChoosePivot(arr, 0, 5));
		//}

	}
}
