letter = input("Write your letter?")
del_space = letter.replace(" ","")
str = del_space
List = list(str)
List.sort()
for key in List:
    print (key, str.count(key))