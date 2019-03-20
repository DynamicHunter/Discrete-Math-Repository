def truthValues(p, q):

    if p == "T" and q == "T":
        print("\nConjunction: True \n"
              "Disjunction: True\n"
              "Exclusive or: False \n"
              "Conditional: True \n"
              "Biconditional: True")
        return

    if p == "T" and q == "F":
        print("\nConjunction: False\n"
              "Disjunction: True\n"
              "Exclusive or: True \n"
              "Conditional: False \n"
              "Biconditional: False")
        return

    if p == "F" and q == "T":
        print("\nConjunction: False \n "
              "Disjunction: True \n"
              "Exclusive or: True \n"
              "Conditional: True \n"
              "Biconditional: False")

    if p == "F" and q == "F":
        print("\nConjunction: False \n"
              "Disjunction: False \n"
              "Exclusive or: False \n"
              "Conditional: True \n"
              "Biconditional: True")


def bitwiseValues(s, t):

    #Bitwise AND
    bitwiseString = ""
    for i in range(len(s)):
        if (s[i] == "1" and s[i] == t[i]):
            bitwiseString += "1"
        else:
            bitwiseString += "0"
    print("Bitwise AND: " + bitwiseString)
    

    #Bitwise OR
    bitwiseString = ""
    for j in range(len(s)):
        if (s[j] == "1" or t[j] == "1"):
            bitwiseString += "1"
        else:
            bitwiseString += "0"
    print("Bitwise OR: " + bitwiseString)
    

    #Bitwise XOR
    bitwiseString = ""
    for k in range(len(s)):
        if ((s[k] == "1" or t[k] == "1") and s[k] != t[k]) :
            bitwiseString += "1"
        else:
            bitwiseString += "0"
    print("Bitwise XOR: " + bitwiseString)
    

def main():
    p = input(str("Enter T for True and F for False: "))
    q = input(str("Enter T for True and F for False: "))
     
    s = input("Enter a bit: ")
    t = input("Enter another bit: ")
    
    truthValues(p, q)
    bitwiseValues(s, t)

main()
