# Hunter Davis
# 3/18/2019

# Linear Congruential Method (non-recursive sequence)
def linear_congruential(a, seed, c, m):
    x = []
    x.append(seed) # x[0] is seed value
    # Base case, impossible to hit first run:
    result = m

    # Base increment, referencing x[0] first run, previous from then on
    i = 0
    # Loop until result == x[0]
    while result != seed:
        result = (a * x[i] + c) % m
        x.append(result)

        i += 1
    # Return sequence
    return x

def linear_congruence(a, seed, c, m, x):
    # Initializing the seed and result if needed
    if len(x) < 1:
        result = (a * seed + c) % m
        x.append(seed)

    if len(x) > 1 and x[-1] == seed:
        return x
    else:
        result = (a * linear_congruence(a, seed, c, m, x) + c) % m
        x.append(result)
        print(result)
        return result


'''
a is multiplier value
seed is seed value
x is sequence array of values generated, x[0] is seed
c is increment value
m is modulus value
'''

# Ex 3 in class
print(linear_congruential(7, 3, 4, 9))
x = []
y = []
#print(linear_congruence(7, 3, 4, 9, x))
#print(linear_initialize(7, 3, 4, 9, y))
