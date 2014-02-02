using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SCC
{
    public enum VColor
    {
        None = 0,

        /// <summary>
        /// Not visited
        /// </summary>
        White = 1,
        /// <summary>
        /// Visited
        /// </summary>
        Gray = 2,
        /// <summary>
        /// Fully Explored
        /// </summary>
        Black = 3,
    }

    public class Vertex
    {
        public uint[] AdjVerticesNumbers = new uint[] { };
        public VColor VisitColor = VColor.None;
        public uint PredecessorNumber = 0;
        public uint Order = 0;
        public uint Number = 0;
        public uint Leader = 0;

        public override string ToString()
        {
            return Number.ToString() + " [leader =" + Leader + "] adj length = " + AdjVerticesNumbers.Length;
        }
    }
}
