using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Dijkstra;

namespace Test
{
    [TestClass]
    public class UnitTest1
    {
        const string path1 = @"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-5\dijkstra1.txt";
        const string path2 = @"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-5\dijkstra2.txt";
        
        [TestMethod]
        public void TestReadVertices()
        {
            var vertices = Program.ReadVertices(path1);
            Assert.AreEqual(4, vertices.Count);
            Assert.AreEqual(2, vertices[1].AdjVertices.Count);
            Assert.AreEqual(10, vertices[1].AdjVertices[4]);
            Assert.AreEqual(5, vertices[1].AdjVertices[1]);

            vertices = Program.ReadVertices(path2);
            Assert.AreEqual(6, vertices.Count);
            Assert.AreEqual(2, vertices[1].AdjVertices.Count);
            Assert.AreEqual(3, vertices[1].AdjVertices[4]);
            Assert.AreEqual(10, vertices[1].AdjVertices[5]);
        }

        [TestMethod]
        public void TestDijkstra1()
        {
            var vertices = Program.ReadVertices(path1);
            Dijkstra.Dijkstra.FindShortestPath(vertices, 1);

            var vertex = vertices.Find(v => v.Number == 4);
            Assert.AreEqual((uint)2, vertex.TotalPathLength);
        }

        [TestMethod]
        public void TestDijkstra2()
        {
            var vertices = Program.ReadVertices(path2);
            Dijkstra.Dijkstra.FindShortestPath(vertices, 1);

            var vertex = vertices.Find(v => v.Number == 7);
            Assert.AreEqual((uint)5, vertex.TotalPathLength);
        }

    }

}
