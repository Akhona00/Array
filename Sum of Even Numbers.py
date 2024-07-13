def sum_even_num(a):
    total = 0
    for num in a:
        if num % 2 == 0:
            total += num
    return total

array = [1,2,3,4,5,6,7,8,9,10]
print(sum_even_num(array))