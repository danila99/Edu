using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dijkstra
{
    public class Vertex
    {
        public Dictionary<uint, ushort> AdjVertices = new Dictionary<uint, ushort>();
        public uint TotalPathLength = 0;
        public uint Number = 0;

        public override string ToString()
        {
            string adj = AdjVertices
                .Select(pair => pair.Key + ":" + pair.Value)
                .Aggregate((agreagte, s) => agreagte + ", " + s);

            return Number.ToString() + " [AdjVertices = " + adj + "] path length = " + TotalPathLength;
        }

        public override int GetHashCode()
        {
            return (int)Number;
        }
    }
}
