"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

filename = 'task5.csv'
stocks = []

File = open(filename, 'r')
    
lines = File.readlines() #doesn't work with .read only .readlines

for row in lines:
    #.strip is my saviour
    x = row.strip().split(',')
    if len(x) >= 2:  
        symbol = x[0].strip()#thank you google
        name = x[1].strip()  #thank you google
        stocks.append((symbol, name))

search_symbol = input("Enter stock symbol: ").strip()

matches = [name for symbol, name in stocks if symbol == search_symbol]

if len(matches) == 0:
    print("No match found")
elif len(matches) == 1:
    print(matches[0])
else:
    print(f"There are {len(matches)} stocks with that symbol")