using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace SCC
{
    public class CC
    {
        public static uint[] Count(Vertex[] vertices)
        {
            var stackSize = 100000000;
            uint[] result = new uint[] {};
            Thread newThread = new Thread(() => CountInternal(vertices, out result), stackSize);
            Trace.WriteLine("newThread started with stackSize = " + stackSize);
            newThread.Start();
            newThread.Join();
            return result;
        }

        private static void CountInternal(Vertex[] vertices, out uint[] biggest)
        {
            // 1
            Trace.WriteLine("DFS on vertices");
            DFS.Search(vertices);
            GC.Collect(); // may increase performance

            // 2
            Trace.WriteLine("Creating reversed vertices array");
            var dict = DFS.Dict;
            Dictionary<uint, List<uint>> reversedDict = new Dictionary<uint, List<uint>>();
            uint i;
            for (i = 0; i < vertices.Length; i++)
            {
                Vertex v = vertices[i];
                if (!reversedDict.ContainsKey(v.Number))
                    reversedDict.Add(v.Number, new List<uint>());

                uint j;
                for (j = 0; j < v.AdjVerticesNumbers.Length; j++)
                {
                    var adj = v.AdjVerticesNumbers[j];
                    if (!reversedDict.ContainsKey(adj))
                        reversedDict.Add(adj, new List<uint>() { v.Number });
                    else
                        reversedDict[adj].Add(v.Number);
                }
            }

            for (i = 0; i < vertices.Length; i++)
                vertices[i].AdjVerticesNumbers = reversedDict[vertices[i].Number].ToArray();

            reversedDict = null; // may increase performance
            Trace.WriteLine("Sorting reversed vertices by times (descending)");
            vertices = vertices.OrderByDescending(v => v.Order).ToArray();

            // 3
            Trace.WriteLine("DFS on reversed vertices");
            DFS.Search(vertices);

            // 4
            biggest = DFS.RunningTimes.Values.OrderByDescending(n => n).Take(5).ToArray();
            Trace.Write("Result: ");
            Array.ForEach(biggest, b => Trace.Write(b + " "));
            Trace.WriteLine("");
        }
    }
}
