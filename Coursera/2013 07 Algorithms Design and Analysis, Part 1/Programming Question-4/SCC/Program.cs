using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace SCC
{
    public class Program
    {
        private const string _path = @"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-4\SCC.txt";
        private readonly static Regex _isNumber = new Regex(@"\d+", RegexOptions.Compiled);

        static void Main(string[] args)
        {
            var vertices = Program.ReadVertices(_path);
            uint[] result = CC.Count(vertices);

            foreach (uint i in result)
                Console.Write(i + ",");

            Console.ReadKey();
        }

        public static Vertex[] ReadVertices(string path)
        {
            Dictionary<uint, List<uint>> verticesDict = new Dictionary<uint, List<uint>>();

            using (StreamReader sr = new StreamReader(path))
            {
                string line;

                while ((line = sr.ReadLine()) != null)
                {
                    var vals = line.Split(' ').Where(ch => _isNumber.IsMatch(ch)).ToArray();
                    if (vals.Count() == 0)
                        continue;

                    if (vals.Count() != 2)
                        throw new ApplicationException("Wrong line: " + line);

                    uint v = UInt32.Parse(vals[0]);
                    uint adj =  UInt32.Parse(vals[1]);

                    if (!verticesDict.ContainsKey(v))
                        verticesDict.Add(v, new List<uint>() { adj });
                    else
                        verticesDict[v].Add(adj);

                    if (!verticesDict.ContainsKey(adj))
                        verticesDict.Add(adj, new List<uint>());
                }
            }

            List<Vertex> vertices = new List<Vertex>();
            foreach (var v in verticesDict)
                vertices.Add(new Vertex() { Number = v.Key, AdjVerticesNumbers = v.Value.ToArray() });
            
            Trace.WriteLine("vertices.Length = " + vertices.Count);
            return vertices.ToArray();
        }
    }
}
