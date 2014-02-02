using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;

namespace C1QuickSort
{
	public enum PivotLogic
	{
		None = 0,
		First = 1,
		Last = 2,
		Median = 3
	}

	public static class QuickSort
	{
		public static PivotLogic PivotLogic = PivotLogic.First;
		
		public static int Sort(int[] arr)
		{
			return Sort(arr, 0, arr.Length - 1);
		}

		private static int Sort(int[] arr, int start, int end)
		{
			if (start >= end)
				return 0; // guard
			
			int pivotIndex = Partition(arr, start, end);

			int c1 = Sort(arr, start, pivotIndex - 1);
			int c2 = Sort(arr, pivotIndex + 1, end);

			return c1 + c2 + (end - start);
		}

		private static int Partition(int[] arr, int start, int end)
		{
			int newPivotIndex = SwapPivot(arr, start, end);

			if (newPivotIndex == start)
				return PartitionAtStart(arr, start, end);
			if (newPivotIndex == end)
				return PartitionAtEnd(arr, start, end);

			throw new ApplicationException("newPivotIndex is wrong: " + newPivotIndex);
		}

		private static int PartitionAtEnd(int[] arr, int start, int end)
		{
			int x = arr[end];
			int i = start - 1;

			for (int j = start; j < end; j++)
			{
				if (arr[j] <= x)
				{
					i++;
					SwapValue(arr, i, j);
				}
			}

			SwapValue(arr, i + 1, end);
			return i + 1;
		}

		private static int PartitionAtStart(int[] arr, int start, int end)
		{
			int x = arr[start];
			int i = start;

			for (int j = start + 1; j <= end; j++)
			{
				if (arr[j] <= x)
				{
					i++;
					SwapValue(arr, i, j);
				}
			}

			SwapValue(arr, i, start);
			return i;
		}

		private static int SwapPivot(int[] arr, int start, int end)
		{
			int pivotIndex;// = ChoosePivot(arr, start, end);
			int newPivotIndex;

			switch (PivotLogic)
			{
				case PivotLogic.First:
					pivotIndex = start;
					newPivotIndex = start; 
					break;
				case PivotLogic.Last:
					pivotIndex = end;
					newPivotIndex = start;
					break;
				case PivotLogic.Median:
					int length = end - start + 1;
					int median = start + (length/2) + (length%2 == 0 ? -1 : 0);
					pivotIndex = (new[] {start, median, end}).OrderBy(i => arr[i]).Skip(1).First();
					newPivotIndex = start;
					break;
				default:
					throw new InvalidEnumArgumentException("PivotLogic.None is not allowed");
			}

			SwapValue(arr, newPivotIndex, pivotIndex);
			return newPivotIndex;
		}

		private static void SwapValue(int[] arr, int i1, int i2)
		{
			int temp = arr[i1];
			arr[i1] = arr[i2];
			arr[i2] = temp;
		}
	}
}
