# O(n)
def find_sum(array):
    total = 0
    for i in array:
        total += i
    return total

# exact measurement of time to execute depends on OS, etc.
# define instead how it scales with # of inputs
# linear - O(n), constant - O(1), quadratic - O(n^2)
# look at highest-order term in analysis
# e.g. T = cn^2 + dn + e

# O(1)
def do_nothing(array):
    return 0

def find_another_sum(two_d_array):
    total = 0 # O(1)
    for row in two_d_array: # *n
        for i in row:       # *n
            total += i      # O(1)
    return total # O(1)
# O(1) + O(1)*O(n)*O(n) + O(1) => O(n^2)
# but what if it's not a square?? discuss dimensionality (n*m instead of n*n)

# what about log(n) complexity?
# CS, default is log base 2, not 10
# 3 ^ x = 9 => log_3(9) = x 
# to what power must we raise 3 to get 9?
# log_10(100) = 2
# log_2(8) = 3
# logs base 2 - how many times must we halve a number to get 1?
# connects to binary search
# NOTE: an array must be sorted for binary search to work
# check middle val, bigger or smaller? throw out extra, rinse&repeat
# has log_2(n) time complexity