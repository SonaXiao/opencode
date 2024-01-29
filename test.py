all_products = {}

def add_product(name, price):
    product = {}
    product['price'] = price
    product['sale_history'] = []
    product['feedback'] = []
    product['rating'] = []
    all_products[name] = product

def add_sale(name, num):
    if name in all_products:
        all_products[name]['sale_history'].append(num)
        print('add sale success')
    else:
        print('No such product')

def add_feedback(name, feedback, rating):
    if name in all_products:
        all_products[name]['feedback'].append(feedback)
        all_products[name]['rating'].append(rating)
        print('add feedback success')
    else:
        print('No such product')

def cal_total_sale(name):
    if name in all_products:
        total = 0
        for num in all_products[name]['sale_history']:
            total += num
        print("total sales for {}: {}".format(name, total))
    else:
        print('No such product')

def bast_selling():
    max_sale_num = 0
    max_sale_name = None
    for name,product in all_products.items():
        total = 0
        for num in product['sale_history']:
            total += num
        if total > max_sale_num:
            max_sale_num = total
            max_sale_name = name
    print("bast_selling product is {}, total sales is {}".format(max_sale_name, max_sale_num))

def cal_avg_rating(name):
    if name in all_products:
        if len(all_products[name]['rating']) == 0:
            print('Product without feedback')
        rating = sum(all_products[name]['rating']) / len(all_products[name]['rating'])
        print("average rating for {}: {}".format(name, rating))
    else:
        print('No such product')

def ProductSalesAnalysis():
    while True:
        print('\n')
        print('#' * 50)
        print("Product Sales Analysis System")
        print("1. Add Sale Transactions")
        print("2. Add Customer Feedback")
        print("3. Calculating Total Sales")
        print("4. Identifying the Best-selling Product")
        print("5. Displaying Product Average Rating")
        print("6. Exit")
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter product name: ")
            num = int(input("Enter sale num: "))
            add_sale(name, num)
        elif choice == '2':
            name = input("Enter product name: ")
            feedback = input("Enter feedback: ")
            rating = int(input("Enter rating (0 ~ 5): "))
            add_feedback(name, feedback, rating)
        elif choice == '3':
            name = input("Enter product name: ")
            cal_total_sale(name)
        elif choice == '4':
            bast_selling()
        elif choice == '5':
            name = input("Enter product name: ")
            cal_avg_rating(name)
        elif choice == '6':
            print("Exiting Product Sales Analysis System.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__=="__main__":
    add_product('phone', 600)
    add_product('watch', 120)
    add_product('computer', 980)
    add_sale('phone', 1)
    add_sale('phone', 2)
    add_sale('watch', 2)
    add_sale('watch', 3)
    add_sale('watch', 1)
    add_sale('computer', 1)
    add_feedback('phone', 'useful', 4)
    add_feedback('phone', 'pretty', 5)
    add_feedback('watch', 'watch', 1)
    ProductSalesAnalysis()
