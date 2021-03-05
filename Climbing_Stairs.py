from math import factorial


def climb_stairs(n: int) -> int:
    total_sum = 0
    for number_ones in range(n, -1, -2):
        number_twos = (n - number_ones) // 2
        total_sum += (factorial(number_ones + number_twos) // (factorial(number_ones) * factorial(number_twos)))
        # print(factorial(number_ones + number_twos), factorial(number_ones),  factorial(number_ones))
        print(number_ones, number_twos, total_sum)
    return total_sum


print(climb_stairs(4))
