nb = int(input("Enter ur number?"))
def prime(nb):
    if nb < 2:
        return False
    for i in range(2, int(nb/2)):
        if not nb % i:
            return False
    return  True
if prime(nb) == True:
        print("This is prime")
else:
        print("This is not prime")


