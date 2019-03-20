# Hunter Davis
# Tanner Mindrum


from math import gcd


def relativelyPrime(L):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if gcd(L[i], L[j]) != 1:
                return "Not Pairwise Relatively Prime"
    return "Pairwise Relatively Prime"

def chinese_remainder_theorem(a_list, m_list):
    if(len(a_list) != len(m_list)):
        print("Lists are not equal, exiting")
        exit(1)
    if(relativelyPrime(m_list) != "Pairwise Relatively Prime"):
        print("Cannot Proceed, mList input is not Pairwise relatively Prime")
        exit(1)
    #print("a:", a_list)
    #print("m:", m_list)
    # Finding little m and big m
    little_m = 1
    big_m = []
    for i in range(0, len(m_list)):
        little_m *= m_list[i]
    for i in range(0, len(m_list)):
        big_m.append(little_m // m_list[i])
    #print("Little m:", little_m)
    #print("Big m:", big_m)

    # Finding the inverse
    inverse_y = []
    multiplier = 1
    for i in range(0, len(big_m)):
        while (big_m[i] * multiplier % m_list[i]) != 1:
            multiplier += 1
        #inverse_y.append(big_m[i] % m_list[i])
        inverse_y.append(multiplier)
    #print("Inverse y:", inverse_y)

    chinese_remainder_sol = 0
    for i in range(0, len(big_m)):
        chinese_remainder_sol += (a_list[i] * big_m[i] * inverse_y[i])
        chinese_remainder_sol %= little_m
    print(chinese_remainder_sol)
    print()



chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
chinese_remainder_theorem([1, 2, 3, 4], [5, 7, 9, 11])
chinese_remainder_theorem([1, 2, 3, 4, 8], [5, 7, 9, 11, 22])
