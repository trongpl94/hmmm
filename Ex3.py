numbers = [1,6,8,1,2,1,5,6]
print("THIS IS MY NUMBERS:",*numbers, sep=" ")
nb = int(input("ENTER A NUMBER?"))
nb_count = {}
strs= str(numbers)
format_1 = strs.replace("[","")
format_2 = format_1.replace("]","")
format_3 = format_2.replace(",","")
format_4 = format_3.replace(" ","")
if nb in numbers:
    for i in format_4:
        nb_count[i] = nb_count.get(i,0) + 1
    print(nb, "appear", nb_count[str(nb)],"times in my list")
else:
    print("This is not my numbers, i'm angry!!!:", nb)

