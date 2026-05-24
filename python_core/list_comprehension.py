#squares

squares = [x**2 for x in range(1,11)]
print(squares)

#calculate the price after tax for a list of transactions

def calculate_price_after_tax(price):
    return int(price + (price * tax_rate))    
transactions = [100, 200, 300, 400, 500]
print("Prices before tax:", transactions)
tax_rate = 0.1
prices_after_tax=[calculate_price_after_tax(x) for x in transactions]
print("Prices after tax:", prices_after_tax)


#filters out any characters in sentence that aren’t vowels.
sentence = "This is a sample sentence to demonstrate list comprehensions."
result = sorted({char for char in sentence if char.lower() in 'aeiou'}, reverse=True)
print('Vowels in the sentence are: ' ,result)

#dictionary comprehention
sentence = "This is a sample sentence to demonstrate list comprehensions."
result = {char: sentence.count(char) for char in sentence if char.lower() in 'aeiou'}
print('dictionary comprehention:Vowels in the sentence are: ' ,sorted(result.items()))


