# Sorting-Algorithm-Visualizer

This Python program visualizes various common sorting algorithms, allowing you to see each step of the sorting process directly in the terminal. The program includes implementations of Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, and Quick Sort. Additionally, it provides a visualization of the Binary Search algorithm to demonstrate searching in a sorted array.

# Features
  - Sorting Algorithms: Includes step-by-step visualizations for:
    - Bubble Sort
    - Insertion Sort
    - Selection Sort
    - Merge Sort
    - Quick Sort
  - Binary Search: Demonstrates searching for an element in a sorted array.
  - Progressive Step Messages: Each step of sorting and searching displays helpful messages,       such as "Swapping elements...", "Inserting...", "Merging halves...", or "Checking              index...," to make the process easier to follow.
  - Randomized Input: Generates a random array of integers between 1 and 20 for each sorting       run.
  - Commented Code: Includes comments that briefly explain each sorting algorithm and the          binary search technique.

# Algorithms Explained

1. Bubble Sort
  - Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them      if they are in the wrong order.
  - This process continues until the list is sorted.
  - Complexity: O(n²)
2. Insertion Sort
  - Insertion Sort builds the sorted array one item at a time by comparing the current element     to its previous elements, shifting larger elements to the right.
  - Complexity: O(n²) but more efficient than Bubble Sort for nearly sorted arrays.
3. Selection Sort
  - Selection Sort finds the minimum element from the unsorted part of the list and moves it       to the beginning of the unsorted part.
  - This process continues until the list is sorted.
  - Complexity: O(n²)
4. Merge Sort
  - Merge Sort is a divide-and-conquer algorithm that splits the list in half, recursively         sorts each half, and then merges the sorted halves.
  - Complexity: O(n log n)
5. Quick Sort
  - Quick Sort is another divide-and-conquer algorithm that selects a pivot element,               partitions the array around the pivot, and then recursively sorts the partitions.
  - Complexity: O(n log n) on average but can be O(n²) in the worst case.
6. Binary Search
  - Binary Search finds a target element in a sorted array by repeatedly dividing the array in     half until the target is found or the list cannot be divided further.
  - Complexity: O(log n)

# Running the Program
1. Prerequisites: Ensure Python 3 is installed.
2. Clone or Download this repository.
3. Run the Program:

python sorting_visualizer.py

# Example Output
Each sorting algorithm will print steps such as "Swapping elements..." or "Inserting..." to show its progress in the terminal. Similarly, Binary Search will display steps like "Checking index..." to indicate each comparison it makes while searching for the target value.

# Code Structure
  - print_array: Helper function to display the array with a message.
  - bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort: Sorting algorithms        with step-by-step output.
  - binary_search: A search function for finding a target in a sorted array.
  - main: Initializes a random array and calls each sorting algorithm and Binary Search with       visualizations.

# Future Enhancements
Consider adding more sorting algorithms or interactive input for user-specified arrays and target values.
