Given m number of sorted lists in ascending order and an integer k , find the k th smallest number among all the given lists.

Constraints:
If k is greater than the total number of elements in the input lists, return the greatest element from all the lists.
If there are no elements in the input lists, return 0.



from heapq import *
def k_smallest_number(lists, k):
    # storing the length of lists to use it in a loop later
    list_length = len(lists)
    # declaring a min-heap to keep track of smallest elements
    kth_smallest = []
    # to check if input lists are empty
    empty_list = []

    for index in range(list_length):
        # if there are no elements in the input lists, return []
        if lists[index] == empty_list:
            continue;
        else:
            # placing the first element of each list in the min-heap
            heappush(kth_smallest, (lists[index][0], 0, lists[index]))

    # set a counter to match if our kth element
    # equals to that counter, return that number
    numbers_checked, smallest_number = 0, 0
    while kth_smallest:  # iterating over the elements pushed in our min-heap
        # get the smallest number from top of heap and its corresponding list
        smallest_number, index, top_num_list = heappop(kth_smallest)
        numbers_checked += 1

        if numbers_checked == k:
            break

        # if there are more elements in list of the top element,
        # add the next element of that list to the min-heap
        if index + 1 < len(top_num_list):
            heappush(
                kth_smallest, (top_num_list[index + 1], index + 1, top_num_list))

    # return the Kth number found in input lists
    return smallest_number