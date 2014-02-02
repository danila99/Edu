using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SCC;
using System.Diagnostics;

namespace TestProject
{
    [TestClass]
    public class TestDFS
    {
        [TestInitialize]
        public void Initialize()
        {
            TextWriterTraceListener writer = new TextWriterTraceListener(System.Console.Out);
            Debug.Listeners.Add(writer);        
        }

        [TestMethod]
        public void TestOnSmallFile1()
        {
            TestDFSOnFile(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-4\graph1.txt");
        }

        [TestMethod]
        public void TestOnSmallFile2()
        {
            TestDFSOnFile(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-4\graph2.txt");
        }

        [TestMethod]
        public void TestOnHugeFile()
        {
            TestDFSOnFile(@"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-4\SCC.txt");
        }

        [TestMethod]
        public void TestReadOfHugeFile()
        {
            var path = @"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-4\SCC.txt";
            var vertices = Program.ReadVertices(path);

            Assert.IsFalse(vertices.Length == 0);
        }

        private static void TestDFSOnFile(string path)
        {
            var vertices = Program.ReadVertices(path);

            Assert.IsNotNull(vertices);
            Assert.IsFalse(vertices.Length == 0);

            DFS.Search(vertices);

            uint maxOrder = 0;
            foreach (var v in vertices)
            {
                Assert.IsTrue(v.VisitColor == VColor.Black);
                Assert.IsFalse(v.Number == 0);

                if (v.Order > maxOrder)
                    maxOrder = v.Order;
            }

            Assert.IsTrue(maxOrder == vertices.Length);
        }
    }
}
