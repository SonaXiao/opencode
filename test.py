all_products = {}

def add_product(name, price):
    product = {}
    product['price'] = price
    product['sale_history'] = []
    product['feedback'] = []
    product['ratings'] = []
    all_products[name] = product

def sale(name, num):
    if name in all_products:
        all_products[name]['sale_history'].append(num)
        return 1, None
    else:
        return -1, 'No such product'

def cal_total(name):
    if name in all_products:
        total = 0
        for num in all_products[name]['sale_history']:
            total += num
        return total, None
    else:
        return -1, 'No such product'


def ProductSalesAnalysis():
    while True:
        print()
        choice = input("Enter choice ")

        if choice == '1':
            name = input("Enter product name: ")
            num = int(input("Enter sale num: "))
            sale(name, num)
