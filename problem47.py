"""
Given a array of numbers representing the stock prices of a company in chronological order,
 write a function that calculates the maximum profit you could have made from buying and selling that stock once.
  You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
def max_stock_profit(stock_data):
    max_profit = 0
    for index, i in enumerate(stock_data):
        for elem in stock_data[index+1:]:
            profit = elem - i
            if profit > max_profit:
                selling_price = elem
                purchase_price = i
                max_profit = profit
    return purchase_price, selling_price, max_profit


if __name__ == "__main__":
    input_data = [9, 11, 8, 5, 7, 10]
    purchase_price, selling_price, max_profit = max_stock_profit(input_data)
    print('The max profit is : {}'.format(max_profit))
    print('Purchase price is : {}'.format(purchase_price))
    print('Selling price is : {}'.format(selling_price))