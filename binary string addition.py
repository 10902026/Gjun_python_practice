a=input()
b=input()
print(f"a={int(a,2)},b={int(b,2)}")
c = int(a,2) + int(b,2)
binary_string = ""
while c > 0:
    remainder = c % 2
    c = c // 2
    binary_string = str(remainder) + binary_string
    # print(f"remainder={remainder},c={c},binary_string={binary_string}")
print(binary_string)
