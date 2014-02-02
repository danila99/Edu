using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SplitInversion;
using System.Linq;

namespace Test
{
    [TestClass]
    public class MergeTest
    {
        [TestMethod]
        public void TestMethod1()
        {
            Run(new int[] { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 });
        }

        [TestMethod]
        public void TestMethod2()
        {
            Run(new int[] { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 });
        }

        [TestMethod]
        public void TestMethod3()
        {
            Random rand = new Random();
            Run(Enumerable.Repeat(0, 99).Select(i => rand.Next()).ToArray());
        }

        [TestMethod]
        public void TestMethod4()
        {
            Random rand = new Random();
            Run(Enumerable.Repeat(0, 100).Select(i => rand.Next()).ToArray());
        }

        public void Run(int[] arr)
        {
            int[] res = (int[])arr.Clone();
            Array.Sort<int>(res);

            MergeSort.Sort(ref arr);
            for (int i = 0; i < arr.Length - 1; i++)
            {
                Assert.AreEqual(arr[i], res[i]);
            }
        }
    }
}
