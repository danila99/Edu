using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SCC;

namespace TestProject
{
    [TestClass]
    public class TestCC
    {
        public void TestFile(string path, uint[] expected)
        {
            var vertices = Program.ReadVertices(path);

            Assert.IsNotNull(vertices);
            Assert.IsFalse(vertices.Length == 0);

            uint[] result = CC.Count(vertices);

            for (uint i = 0; i < expected.Length; i++)
                if (expected[i] != 0)
                    Assert.AreEqual(expected[i], result[i]);
        }

        [TestMethod]
        public void TestOnSmallFile1()
        {
            TestFile(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-4\SCC-small1.txt", new uint[] { 3, 2, 2, 2, 1 });
        }

        [TestMethod]
        public void TestOnSmallFile2()
        {
            TestFile(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-4\SCC-small2.txt", new uint[] { 3, 3, 2, 0, 0 });
        }

        [TestMethod]
        public void TestOnSmallFile3()
        {
            TestFile(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-4\SCC-small3.txt", new uint[] { 6, 3, 2, 1, 0 });
        }
    }
}
