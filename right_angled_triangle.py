def calculate(lengtha, lengthb, include_islongest=False):
    if include_islongest == False:
        return (lengtha**2 + lengthb**2)**0.5
    elif lengtha != lengthb :
        longer = max(lengtha,lengthb)
        shorter = min(lengtha,lengthb)
        return (longer**2 + shorter**2)**0.5

if __name__ == '__main__':
    print(calculate(3, 4))
    print(calculate(5, 12))
    print(calculate(13, 12, True))