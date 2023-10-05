def calculateSum(input):
    count = 0
    for i in input:
        count = count + i

    return count


def calculateProduct(input):
    count = 1
    for i in input:
        count = count * i

    return count

def average(input):
    if len(input) == 0:
        return None
    total = 0

    for number in input:
        total += number
    return total / len(input)

def median(input):
    if not input:
        return None
    sorted_input = sorted(input)
    middle = len(sorted_input) // 2
    return (sorted_input[middle - 1] + sorted_input[middle]) / 2 if len(sorted_input) % 2 == 0 else sorted_input[middle]



def mode(input):
    if not input:
        return None
    count = {}
    most_freq, most_freq_count = None, 0
    for number in input:
        count[number] = count.get(number, 0) + 1
        if count[number] > most_freq_count:
            most_freq, most_freq_count = number, count[number]
    return most_freq


if __name__ == '__main__':
    # Sum
    print(calculateSum([]) == 0)
    print(calculateSum([2, 4, 6, 8, 10]) == 30)
    print(calculateSum([1, 3, 5, 7, 9]) == 25)

    # Product
    print(calculateProduct([]) == 1)
    print(calculateProduct([2, 4, 6, 8, 10]) == 3840)

    # average
    print(average([1, 2, 3]) == 2)
    print(average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2)
    print(average([12, 20, 37]) == 23)
    print(average([0, 0, 0, 0, 0]) == 0)

    # median
    print(median([]) is None)
    print(median([1, 2, 3]) == 2)
    print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5)
    print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6)

    # mode
    print(mode([]) is None)
    print(mode([1, 2, 3, 4, 4]) == 4)
    print(mode([1, 1, 2, 3, 4]) == 1)

#%%
