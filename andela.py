def digit_count(N):
    nums = [ len(str(n)) for n in range(1, N+1) ]
    max_digit = max(nums)
    def ans(multiplier, arr):
        sum_dig = str(sum([digit*multiplier for digit in arr]))
        return sum([ int(dig) for dig in sum_dig])

    if max_digit % 2 != 0 :
        return ans(2, nums)
    elif max_digit % 2 == 0 and max_digit % 4 == 0 :
        return ans(4, nums)
    elif max_digit % 2 == 0 and max_digit % 4 != 0:
        return ans(3, nums)

print(digit_count(6))
print(digit_count(16))
print(digit_count(56))
