
def binary_search(list, value):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (high + low)//2

        if list[mid] < value:
            low = mid + 1
        elif list[mid] > value:
            high = mid - 1
        else:
            return mid

    return -1

length = int(input("Enter the length of list: "))

list = []

print("Enter the values you want to add in the array")

i = 0

while i <= length:
    appendValue = int(input("Enter: "))
    if appendValue not in list:
        list.append(appendValue)
    else:
        print("Please donot duplicate the values")
    i += 1

print(list)

list.sort

value = int(input("Enter the value you want to search: "))

output = binary_search(list, value)

print(f"The number you are searching for is in {output + 1} place")