using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace SCC
{
    public static class DFS
    {
        private static uint _time = 0; 
        private static Dictionary<uint, Vertex> _dict = new Dictionary<uint, Vertex>();
        private static Dictionary<uint, uint> _runningTimes = new Dictionary<uint, uint>();
        private static uint _s = 0;

        public static Dictionary<uint, uint> RunningTimes
        {
            get { return _runningTimes ; }
        }

        public static Dictionary<uint, Vertex> Dict
        {
            get { return _dict; }
        }

        public static void Search(Vertex[] vertices)
        {
            _time = 0;
            _dict = new Dictionary<uint, Vertex>();
            _runningTimes = new Dictionary<uint, uint>();
            
            var stackSize = 100000000;
            Thread newThread = new Thread(() => SearchInternal(vertices), stackSize);
            Trace.WriteLine("newThread started with stackSize = " + stackSize);
            newThread.Start();
            newThread.Join();
        }
        
        private static void SearchInternal(Vertex[] vertices)
        {
            // clear vertices fields
            for (int i = 0; i < vertices.Length; i++)
            {
                vertices[i].VisitColor = VColor.White;
                vertices[i].PredecessorNumber = 0;
                vertices[i].Order = 0;

                // initialize helper dictionary
                //Trace.WriteLine("adding: " + vertices[i]);
                _dict.Add(vertices[i].Number, vertices[i]);
            }

            Trace.WriteLine("search started. Vertices.Length = " + vertices.Length);
            // do the search
            foreach (Vertex u in vertices)
            {
                if (u.VisitColor == VColor.White)
                {
                    _s = u.Number;
                    SearchVisit(u, ref vertices);
                }
            }
        }

        private static void SearchVisit(Vertex u, ref Vertex[] vertices)
        {
            u.VisitColor = VColor.Gray;
            u.Leader = _s;

            if (_runningTimes.ContainsKey(u.Leader))
                _runningTimes[u.Leader] += 1;
            else
                _runningTimes.Add(u.Leader, 1);

            //Trace.WriteLine("u:Order = " + u.Number + ":" + u.Order);
            for (uint i = 0; i < u.AdjVerticesNumbers.Length; i++)
            {
                Vertex adjacent = _dict[u.AdjVerticesNumbers[i]];
                if (adjacent.VisitColor == VColor.White)
                {
                    adjacent.PredecessorNumber = u.Number;
                    SearchVisit(adjacent, ref vertices);
                }
            }

            _time++;
            u.Order = _time;
            u.VisitColor = VColor.Black;
        }
    }
}
