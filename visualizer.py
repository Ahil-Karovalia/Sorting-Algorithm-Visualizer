import random
import time

# Function to print the array as a "visualization"
def print_array(arr, message=""):
    # Print the array elements with an optional message for context
    print(message + " " + " ".join(f"{x:2}" for x in arr))

# Bubble Sort algorithm with step-by-step visualization
def bubble_sort(arr):
    """
    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if out of order
                print_array(arr, message="Swapping elements...")
                time.sleep(0.1)  # Pause to visualize the step

# Insertion Sort algorithm with step-by-step visualization
def insertion_sort(arr):
    """
    Insertion Sort builds the sorted array one item at a time.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print_array(arr, message=f"Inserting {key} in sorted part...")
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
            print_array(arr, message="Shifting element right...")
            time.sleep(0.1)
        arr[j + 1] = key  # Insert key at the correct position
        print_array(arr, message="Inserted element.")
        time.sleep(0.1)

# Selection Sort algorithm with step-by-step visualization
def selection_sort(arr):
    """
    Selection Sort repeatedly finds the minimum element from the unsorted part
    and moves it to the sorted part.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume current index as minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update minimum if found
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the minimum with the first unsorted element
        print_array(arr, message="Selecting minimum and swapping...")
        time.sleep(0.1)

# Merge Sort algorithm with step-by-step visualization
def merge_sort(arr):
    """
    Merge Sort is a divide-and-conquer algorithm that splits the list in half,
    sorts each half, and then merges the sorted halves.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        print_array(arr, message="Merging halves...")

        # Merge the sorted halves back into the main array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            print_array(arr, message="Merging...")

        # Add any leftover elements from the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            print_array(arr, message="Adding leftover from left half...")

        # Add any leftover elements from the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            print_array(arr, message="Adding leftover from right half...")

# Quick Sort algorithm with step-by-step visualization
def quick_sort(arr, low, high):
    """
    Quick Sort is a divide-and-conquer algorithm that uses a pivot to partition
    the array into two subarrays, then recursively sorts the subarrays.
    """
    if low < high:
        pi = partition(arr, low, high)  # Partition the array
        print_array(arr, message="Partitioning around pivot...")
        time.sleep(0.2)
        quick_sort(arr, low, pi - 1)  # Sort the left partition
        quick_sort(arr, pi + 1, high)  # Sort the right partition

def partition(arr, low, high):
    """
    Helper function to perform partitioning in Quick Sort.
    """
    pivot = arr[high]  # Set the pivot element
    i = low - 1  # Index of the smaller element
    print_array(arr, message=f"Choosing pivot {pivot}...")
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements if less than pivot
            print_array(arr, message="Swapping elements...")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    print_array(arr, message="Placing pivot in correct position.")
    return i + 1

# Binary Search function to illustrate searching
def binary_search(arr, target):
    """
    Binary Search repeatedly divides a sorted list in half to locate a target
    value. This function assumes the list is sorted.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Checking index {mid}: {arr[mid]}")
        time.sleep(0.5)
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"{target} not found")
    return -1

# Main function to demonstrate sorting algorithms
def main():
    arr = [random.randint(1, 20) for _ in range(8)]  # Generate a random array
    print("Original Array:")
    print_array(arr)

    print("\nBubble Sort Visualization:")
    bubble_sort(arr.copy())

    print("\nInsertion Sort Visualization:")
    insertion_sort(arr.copy())

    print("\nSelection Sort Visualization:")
    selection_sort(arr.copy())

    print("\nMerge Sort Visualization:")
    merge_sort(arr.copy())

    print("\nQuick Sort Visualization:")
    quick_sort(arr.copy(), 0, len(arr) - 1)

    # Demonstrate Binary Search on a sorted array
    sorted_arr = sorted(arr)
    print("\nSorted Array for Binary Search:")
    print_array(sorted_arr)
    target = random.choice(sorted_arr)  # Pick a random element to search for
    print(f"\nBinary Search for {target}:")
    binary_search(sorted_arr, target)

if __name__ == "__main__":
    main()
