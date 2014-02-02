using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SplitInversion;

namespace Test
{
    [TestClass]
    public class InversionsCalculatorTest
    {
        [TestMethod]
        public void TesCount1()
        {
            int[] arr1 = new int[] { 2, 3, 6, 4, 5, 7 };
            Assert.AreEqual(2, InversionsCalculator.Count(arr1));
        }

        [TestMethod]
        public void TesCount2()
        {
            int[] arr1 = new int[] { 1, 3, 5, 2, 4, 6 };
            Assert.AreEqual(3, InversionsCalculator.Count(arr1));
        }


        [TestMethod]
        public void TesCount3()
        {
            int[] arr1 = new int[] { 1, 3, 5, 7, 2, 4, 6 };
            Assert.AreEqual(6, InversionsCalculator.Count(arr1));
        }
    }
}
