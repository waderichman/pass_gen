
# I took this from the class lecture/discussion slides and coded it in python
def heapify(key_list, length, i):
    maximum = i  # Initialize maximum as root
    left = 2 * i + 1  # left = 2 * i + 1
    right = 2 * i + 2  # right = 2 * i + 2

    # if left exists and is greater than current maximum then left is the new maximum
    if left < length and key_list[i] < key_list[left]:
        maximum = left

    # if right exists and is greater than current maximum then right is the new maximum
    if right < length and key_list[maximum] < key_list[right]:
        maximum = right

    # if maximum doesn't equal curr index then swap
    if maximum != i:
        key_list[i], key_list[maximum] = key_list[maximum], key_list[i]

        # recursively heapify the root.
        heapify(key_list, length, maximum)


# The main function to sort an array of given size
def heap_sort(key_list):
    length = len(key_list)

    # Build heap(rearrange array)
    # same as for (int i = n / 2 - 1; i >= 0; i--)
    for i in range(length // 2 - 1, -1, -1):
        heapify(key_list, length, i)

    # iterate through to extract elements
    for i in range(length - 1, 0, -1):
        key_list[i], key_list[0] = key_list[0], key_list[i]  # swap - position current root to end
        heapify(key_list, i, 0)  # max heapify on the reduced heap
