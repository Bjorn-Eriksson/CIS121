#Created by Bjorn Eriksson

#8.2 D redo:
'''
def total_sales(sales):
    item_values = sales.values()
    item_total = sum(item_values)
    return item_total
'''

#Take two on 8.2:

# Use sales.key() #Use the keys to fetch the values as well

def total_sales(sales):
    total_sold = 0
    #Iterate through keys in sales dict
    for product_name in sales.keys(): 
        #assigns the value of the key to 'units'
        units = sales[product_name]
        #adds that instance of 'units' to a counter.
        total_sold += units 
    return total_sold


print(total_sales({'Laptop': 5, 'Phone': 10, 'Tablet': 3}))
print(total_sales({'Shoes': 20, 'Hats': 15, 'Jackets': 10}))
print(total_sales({'Book': 1, 'Pen': 2, 'Notebook': 1}))










