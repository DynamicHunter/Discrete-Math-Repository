# Hunter Davis
# Tanner Mindrum

import math

#Question 1:
def modulus (base, exponent, divisor):
    #Convert base to Binary
    binary_digits = []
    mod_output = []
    final_output = []
    while exponent > 0:
        binary_digits.append(exponent % 2)
        exponent = exponent // 2
        #print("Exponent:",exponent)
    #binary_digits.reverse()
    #print(binary_digits)

    for i in range(len(binary_digits)):
        #print(i) # exponent value
        temp = base ** (2 ** i) % divisor
        #print(temp)
        mod_output.append(temp)
    #print(mod_output)

    for j in range(len(binary_digits)):
        if binary_digits[j] == 1:
            final_output.append(mod_output[j])
    print(base, "^", exponent, "mod", divisor, "=", final_output, "mod", divisor)
    print(final_output)
    # Now match up with Binary 1's

    output = []
    # Output in List data type
#Question 2:
def relativelyPrime(ints):
    is_pairwise_prime = "is Pairwise Relatively Prime"
    not_pairwise_prime = "is not Pairwise Relatively Prime"
    #Nested for loop
    prime_bools = []
    for i in range(len(ints) - 1):
        for j in range(i + 1, len(ints)):
            #print(ints[i])
            #print(ints[j])
            #print("gcd:",math.gcd(ints[i], ints[j]))
            prime_bools.append(math.gcd(ints[i], ints[j]))
            
        
    
    for k in range(len(prime_bools)):
        one_counts = prime_bools.count(1)
    if one_counts == len(prime_bools):
        print(ints, "\n", is_pairwise_prime)
    else:
        print(ints, "\n", not_pairwise_prime)
    


modulus(11, 644, 645)
relativelyPrime([32, 11, 29])
relativelyPrime([32, 11, 29, 44, 8, 1])
relativelyPrime([5, 8])
relativelyPrime([5, 8, 5])
relativelyPrime([-2, 4])
relativelyPrime([-2, 4, 3])

