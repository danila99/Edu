using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Dijkstra
{
    public class Program
    {
        private const string _path = @"D:\Danila\Edu\Coursera\2013 07 Algorithms Design and Analysis, Part 1\Programming Question-5\dijkstraData.txt";
        private readonly static Regex _isNumber = new Regex(@"\d+", RegexOptions.Compiled);

        static void Main(string[] args)
        {
            var vertices = ReadVertices(_path);
            Dijkstra.FindShortestPath(vertices, 1);

            uint[] lookAt = new uint[] { 7, 37, 59, 82, 99, 115, 133, 165, 188, 197 };
            List<uint> pathesLength = new List<uint>();

            foreach (uint i in lookAt)
                pathesLength.Add(vertices.FirstOrDefault(v => v.Number == i).TotalPathLength);

            Console.WriteLine(pathesLength.Select(p => p.ToString()).Aggregate((agreagte, s) => agreagte + "," + s));
        }

        public static List<Vertex> ReadVertices(string path)
        {
            List<Vertex> vertices = new List<Vertex>();

            using (StreamReader sr = new StreamReader(path))
            {
                string line;
                uint i = 0;

                while ((line = sr.ReadLine()) != null)
                {
                    Dictionary<uint, ushort> adjVertices = new Dictionary<uint,ushort>();
                    
                    i++;
                    var pairs = line.Split('\t'); 
                    foreach(var pair in pairs)
                    {
                        if (String.IsNullOrWhiteSpace(pair))
                            continue;
                        
                        var split = pair.Split(','); 
                        if (split.Count() != 2)
                            throw new ApplicationException("Wrong line: " + line);

                        uint v = UInt32.Parse(split[0]);
                        ushort weight = UInt16.Parse(split[1]);
                        adjVertices.Add(v, weight);
                    }

                    vertices.Add(new Vertex() { Number = i, AdjVertices = adjVertices });
                }
            }

            return vertices;
        }
    }
}
