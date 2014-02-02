using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SplitInversion
{
    public static class MergeSort
    {
        public static void Sort(ref int[] arr)
        {
            Sort(ref arr, 0, arr.Length - 1);
        }
        
        private static void Sort(ref int[] arr, int start, int end)
        {
            if (start < end)
            {
                // If two elements are left only
                if (start + 1 == end)
                {
                    // Swap them if needed
                    if (arr[start] > arr[end])
                    {
                        int temp = arr[end];
                        arr[end] = arr[start];
                        arr[start] = temp;
                    }
                }
                else
                {
                    // Devide
                    int middle = (start + end) / 2;
                    Sort(ref arr, start, middle);
                    Sort(ref arr, middle + 1, end);
                    // Conquer
                    Merge(ref arr, start, middle, end);
                }
            }
        }

        private static void Merge(ref int[] arr, int start, int middle, int end)
        {
            int leftLength = middle - start + 1;
            int rightLength = end - middle;

            int[] left = new int[leftLength + 1];
            int[] right = new int[rightLength + 1];
            int i = 0;
            int j = 0;

            for (i = 0; i < leftLength; i++)
                left[i] = arr[start + i];
            for (j = 0; j < rightLength; j++)
                right[j] = arr[middle + j + 1];

            left[leftLength] = Int32.MaxValue;
            right[rightLength] = Int32.MaxValue;

            i = 0;
            j = 0;

            for (int k = start; k <= end; k++)
            {
                if (left[i] <= right[j])
                {
                    arr[k] = left[i];
                    i++;
                }
                else
                {
                    arr[k] = right[j];
                    j++;
                }
            }
        }
    }
}
