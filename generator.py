list_a = range(1,101)
list_a2_plus = [num**2 for num in list_a ]
print(list_a2_plus)
for index, num in enumerate(list_a2_plus):
    if index == 0 :
        list_a2_plus[index] = num
    else :
        list_a2_plus[index] = (num +list_a2_plus[index-1])
print(list_a2_plus)
