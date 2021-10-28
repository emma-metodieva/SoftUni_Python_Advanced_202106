# Exam Preparation
# 20210214-03. Problem 3
# 18:49 - 18:59 = 10 min

def stock_availability(inventory, command, *args):
    if command == 'delivery':
        for a in args:
            inventory.append(a)
    elif command == 'sell':
        try:
            if str(args[0]).isdigit():
                n = args[0]
                for _ in range(n):
                    del inventory[0]
            else:
                for a in args:
                    inventory = [stock for stock in inventory if stock != a]
        except IndexError:
            del inventory[0]

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
