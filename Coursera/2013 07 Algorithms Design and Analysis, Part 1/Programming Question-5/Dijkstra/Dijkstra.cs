using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dijkstra
{
    public static class Dijkstra
    {
        private static Dictionary<uint, Vertex> _dict = new Dictionary<uint, Vertex>();
        public static readonly uint MaxTotalPathLength = 1000000;
        
        public static void FindShortestPath(List<Vertex> vertices, uint source)
        {
            List<Vertex> Q = new List<Vertex>(vertices);
            
            // initialize reference dict
            Q.ForEach(v => v.TotalPathLength = MaxTotalPathLength);
            Q.ForEach(v => _dict.Add(v.Number, v));

            // INITIALIZE-SINGLE-SOURCE
            Vertex s = vertices.FirstOrDefault(v => v.Number == source);
            s.TotalPathLength = 0;

            while (Q.Count != 0)
            {
                // Extract-Min(Q)
                Vertex u = Q.OrderBy(v => v.TotalPathLength).First();
                Trace.WriteLine("u: " + u);
                Q.Remove(u);

                if (u.TotalPathLength == MaxTotalPathLength)
                    continue;

                foreach (var numVal in u.AdjVertices)
                { 
                    // Relax
                    Vertex v = _dict[numVal.Key];
                    ushort weight = numVal.Value;
                    if (v.TotalPathLength > u.TotalPathLength + weight)
                        v.TotalPathLength = u.TotalPathLength + weight;
                }
            }
        }
    }
}
