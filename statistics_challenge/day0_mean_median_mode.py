
# ------------------------------------------------------------------------------------------------------------
# In this challenge, we practice calculating the mean, median, and mode.
# Given an array of integers, calculate and print the respective mean, median, and mode on separate lines.
# If your array contains more than one modal value, choose the numerically smallest one.
# ------------------------------------------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT

array_length = int(input())
numbers = input()

num_split = numbers.split(" ")

numbers_list = []
for num in num_split:
    numbers_list.append(int(num))


def mean(array):
    """
    Sum all elements in list and divides by length of list
    :param array: list
    :return: double
    """
    return sum(array) / len(array)


def median(array):
    """
    Sort the elements of the list in ascending order.
    Finds the middle number, or average the two middle numbers.
    :param array: list
    :return: double
    """
    array_sorted = sorted(array)
    if len(array) % 2 == 0:
        first = int(len(array) / 2) - 1
        second = int(len(array) / 2)
        median_value = (array_sorted[first] + array_sorted[second]) / 2
    else:
        median_value = array_sorted[int(len(array) / 2)]
    return median_value


def mode(array):
    """
    Find the number of occurrences of each number.
    returns most frequent number. If more than one, returns smaller number
    :param array: list of numbers
    :return: int
    """
    element_count = {}
    for element in array:
        count = array.count(element)
        element_count[element] = count
    max_value = max(element_count.values())
    result = [number for number, occur in element_count.items() if occur == max_value]
    if len(result) > 1:
        return min(result)
    return result


print("{:.1f}".format(mean(numbers_list)))
print("{:.1f}".format(median(numbers_list)))
print("{:.1f}".format(mode(numbers_list)))