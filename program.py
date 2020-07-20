#This is an example program.
#It's purpose is that when a stock reaches a certain value
#the program will automatically sell the stock.
#But if the stock decreases by a cerain amount, the program
#will also sell the stock, making an indefinite amount of loss or 
#gain.

def target_sell_stock():
	add_money_back = account_value + 50
    	print(add_money_back)

def low_sell_stock():
    	AddMoneyBack = account_value - 50
    	print(AddMoneyBack)

account_value = 400
current_stock_price = 50
target_stock_price = 150
low_stock_price = 50

while current_stock_price:

	if (current_stock_price == target_stock_price):
    		command = target_sell_stock()

	elif (current_stock_price == low_stock_price):
		command = low_sell_stock()
		
	else:
		print("Wait it out")
