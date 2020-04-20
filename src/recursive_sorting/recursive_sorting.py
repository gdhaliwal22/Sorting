# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    merged_arr = arrA + arrB
    return merged_arr

# Merge_Sort Function
    # If there's an array greater than 1 (need more than one otherwise there's no point in doing this sort, and should just return the array)
    # Split the left side of the array from index 0 to the midddle
    # Split the right side of the array from the middle to the end of the array
    # Continue to split the left and right sides recursively
    # Now use the MERGE FUNCTION to merge the array in the correct order (Passing in left and right sides to be arrays a and b).
    # Code already has a way to create an array with zeros based on the length of the arrays passed in.
    # Start at the index of 0 for the left and right sides.
    # Loop through the length of the elements
    # Goal is to look for smallest element between the two arrays, and assign it in the merged_arr
    # Need to set up what to do in certain situations
    # If left is already merged, then move on to right (When left index is greater than the length of the left array)
    # Add in the number on the right's index into the merged_arr[i]
    # Increase the counter for the right_index
    # If the right is already merged, then do the same as above but to the left.
    # If the number at the left's index is smaller than the number on the right's index
    # Then add the left number at merged_arr[i]
    # Increase left counter
    # If the number in the right is smaller than the number in the left
    # Then add the right number at merged_arr[i], and increase right counter.
    # Return the newly sorted array

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # if length of list is greater than 1
    if len(arr) > 1:
        # find the middle, split the list into 2 halves
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        # use recursion for the 2 halves
        merge_sort(left)
        merge_sort(right)

        # set variables to 0
        a = 0
        b = 0
        c = 0

        # while 0 is less than both halves
        while a < len(left) and b < len(right):
            # if the left index is less than the right index
            if left[a] < right[b]:
                # assign left index
                arr[c] = left[a]
                # increment left
                a += 1
            else:
                # else assign right index
                arr[c] = right[b]
                # increment right
                b += 1
            # increment through list
            c += 1

        # while a is less than length of left half, increment
        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1

        # while b is less than length of right half, increment
        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
