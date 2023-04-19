Given a non-empty unsorted array taken from a range of 1 to n. Due to some data error, one of the numbers is duplicated, which results in another number missing. Create a function that returns the corrupt pair (missing, duplicated).

def find_corrupt_pair(nums):
    # Initialize missing and duplicated
    missing = None
    duplicated = None

    # Function for swapping
    def swap(arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]
    # Apply cyclic sort on the array

    i = 0
    # Traversing the whole array
    while i < len(nums):
        # Determining what position the specific element should be at
        correct = nums[i] - 1
        # Check if the number is at wrong position
        if nums[i] != nums[correct]:
            # Swapping the number to it's correct position
            swap(nums, i, correct)
        else:
            i += 1

    # Finding the corrupt pair(missing, duplicated)

    for j in range(len(nums)):
        if nums[j] != j + 1:
            duplicated = nums[j]
            missing = j + 1
    return missing, duplicated