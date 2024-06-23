#Write a Python program that reads this file and 
#creates a dictionary where the keys are dates (in YYYY-MM-DD format)
#and the values are tuples containing the opening,
#closing, high, and 
#low stock prices for that day. 
#You can ignore the volume data.

fhand = open('/Users/mamduhhalawa/Desktop/repetition/test3.txt')
next(fhand)

stock_prices = dict()
for line in fhand:
    num_elements = len(line.strip().split())
    line.strip().split()
    date, open_price, close_price, high_price, low_price = line
    open_price = float(open_price)
    close_price = float(close_price)
    high_price = float(high_price)
    low_price = float(low_price)
    for month in stock_prices:
     stock_prices[date] = (open_price, close_price, high_price, low_price)

print(stock_prices)
    
    
    
    # num_elements = len(line.strip().split())
 #   if num_elements != 5:
  #      print(f"Error: Invalid line format: {line}")
  #      continue
  #  date, open_price, close_price, high_price, low_price = 