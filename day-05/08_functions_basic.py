def order(item):
    print(f' order placed: your order is {item}')

def calculate_total(item):
    base_price = 78.00
    VAT = 0.15
    total_price = (base_price + len(item))*1.15
    return total_price
    
def get_order():
    print("preparing order")
    msg = "Order Ready"
    return msg



myorder = input('What would you like: ')
order(myorder)
print(get_order())
order_total = calculate_total(myorder)

print(f'Your order costs: R{order_total:.2f}')
