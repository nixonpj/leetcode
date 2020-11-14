class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        length = len(str(x))
        if length == 1:
            return x
        else:
            leading_digit, remaining_num = divmod(x, 10 ** (length - 1))
            zero_pad_power = length - len(str(remaining_num))
            res = (self.reverse(remaining_num) * 10**zero_pad_power) + leading_digit
            if res > (2 ** 31 - 1):
                return 0
            return sign * res

