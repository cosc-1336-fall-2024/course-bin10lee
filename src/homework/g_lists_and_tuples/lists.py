#
def get_lowest_list_value(numbers):
    lowest=numbers[0]
    for number in numbers:
        if number<lowest:
            lowest=number
    return lowest

def get_highest_list_value(numbers):
    highest=numbers[0]
    for number in numbers:
        if number>highest:
            highest=number
    return highest