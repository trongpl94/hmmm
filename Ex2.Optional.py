prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3
}
stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15
}
menu = ["banana", "apple", "orange", "pear"]
total = 0
for i in menu:
    print(i)
    print("price:",prices[i])
    print("stock:",stock[i])
    money_i = prices[i] * stock[i]
    print(money_i)
    total += money_i
print("Your money is:",total)

