"""
Algorithm Explanation:
    Pick a pivot point, arbitrarily, but the median of the elements is preferred. Usually the end number is chosen. 
    Create a left pointer (first element), and a righter pointer (last element-1: if the last element was chosen 
    for pivot). These form the partition. Compare the left and right pointers. If the left is greater than pivot,
    and the right is less than the pivot, swap the elements. Keep incrementing the left pointer and decremeneting
    the right pointer until the left pointer is greater than the right pointer (in index). Once achieved, 
    choose a new pivot, and repeat the process recursively until each partition is sorted. 

"""


def swap(arr, l, r):
    temp = arr[l]

    arr[l] = arr[r]
    arr[r] = temp

def partition(arr, left, right):
    pivot = arr[int((left+right)/2)]
    l = left
    r = right

    print("Partition pivot = ", pivot)
    print("Partition l: ", l)
    print("Partition r: ", r)

    while l <= r: #once left is greater than right pointer, we have finished and can return

        while arr[l] < pivot: #here we are creating the left partition
            l += 1
            print("new l is now: ", l)

        while arr[r] > pivot: #here we are creating the right partition 
            r -= 1
            print("new r is now: ", r)

        if l <= r: #if the left pointer is larger than the pivot AND the right is less than pivot, swap elements.             
            swap(arr, l, r)
            print("swapping: ", arr[l], " & ", arr[r])
            print("Result:", arr)
            l += 1
            r -= 1

            print("post swapped l is now: ", l)
            print("post swapped r is now: ", r)

    return l #the leftmost pointer becomes the new pivot

def quicksort(arr, left, right):
    if len(arr) > 1:

        #find a pivot such that: 
        #elements smaller than it are on the left
        #and elements larger than it are on the right
        pivotIndex = partition(arr, left, right)
        print("pivotIndex: " , pivotIndex)

        if left < pivotIndex - 1:
            print("here1")
            print("left: ", left)
            quicksort(arr, left, pivotIndex - 1)
        
        if pivotIndex < right:
            print("here2")
            quicksort(arr, pivotIndex, right)
    
    return arr





if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    N = len(arr)
    quicksort(arr, 0, N-1)

   

    print("Sorted array:")
    for x in arr:
        print(x)

