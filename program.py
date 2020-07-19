#This is an example program.
#It's purpose is that when a stock reaches a certain value
#the program will automatically sell the stock.
#But if the stock decreases by a cerain amount, the program
#will also sell the stock, making an indefinite amount of loss or 
#gain. Even if the company goes out of buisness, your money 
#will be safe. Because the program will have taken it out 
#when it reaches the max low you specified.

account_value = 400
initial_stock_price = 100
target_stock_price = initial_stock_price + 50
low_stock_price = initial_stock_price - 50

def target_sell_stock():
	add_money_back = account_value + target_stock_price
    print(add_money_back)

def low_sell_stock():
    AddMoneyBack = account_value + low_stock_price
    print(AddMoneyBack)

if (initial_stock_price == target_stock_price):
    command = target_sell_stock

elif (initial_stock_price == low_stock_price):
	command = low_stock_price

else:
	print("Wait it out")
