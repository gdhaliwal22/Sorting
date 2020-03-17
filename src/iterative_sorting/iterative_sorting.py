arr1 = [2, 6, 9, 5, 3, 10, 7, 1, 4, 8]
# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # What does selection sort do? It repeatedly finds the smallest
    # element in the list, then it moves it to the front
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        minIndex = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # swap
            if minIndex != i:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


print(selection_sort(arr1))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    lst = len(arr)
    # loop through array
    for num1 in range(lst):
        for num2 in range(lst - num1 - 1):
            if arr[num1] < arr[num2]:
                arr[num1], arr[num2] = arr[num2], arr[num1]

    return arr


print(bubble_sort(arr1))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
