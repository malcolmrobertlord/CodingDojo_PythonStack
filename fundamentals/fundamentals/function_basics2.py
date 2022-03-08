# 1 Countdown
def countdown(start):
    count = []
    for x in range(start,-1,-1):
        count.append(x)
    return count

print(countdown(5))

# 2 Print and Return
def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]

print_and_return([1,2])

# 3 First Plus Length
def first_plus_length(a_list):
    sum = a_list[0]+len(a_list)
    return sum

print(first_plus_length([1,2,3,4,5]))

# 4 Values Greater than Second
def values_greater_than_second(A_list):
    greater=[]
    if len(A_list) < 2:
        return False
    else:
        for x in range(0,len(A_list)):
            if A_list[x]>A_list[1]:
                greater.append(A_list[x])
    print(len(greater))
    return greater

print(values_greater_than_second([5,2,3,2,1,4]))

# 5 This Length, That Value
def length_and_value(size,value):
    array=[]
    for x in range(0,size):
        array.append(value)
    return array

print(length_and_value(6,2))