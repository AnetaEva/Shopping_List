class ItemToPurchase:
    # attributes: item_name, item_price and Item_quantity
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # actions
    def get_item_name(self):
        return self.item_name

    def get_item_price(self):
        return self.item_price

    def get_item_quantity(self):
        return self.item_quantity

    def get_item_cost(self):
        return self.item_price * self.item_quantity


class Customer:
    # attributes name, date, shopping cart which is a list
    def __init__(self, cust_name, shop_date):
        self.cust_name = cust_name
        self.shop_date = shop_date
        self.shopping_cart_list = []

    # actions add item, remove item, checkout
    def add_item(self):
        # get name, price and quantity
        item_name = input('Item Name:')
        item_price = float(input('Item Price:'))
        item_quantity = int(input('Item Quantity:'))
        # create an object of name, price & quantity
        item = ItemToPurchase(item_name, item_price, item_quantity)
        self.shopping_cart_list.append(item)

    # def remove_item(self):
    # get_item_name, search shopping cart to look for item which user entered
    def remove_item(self):
        remove_item_name = input('Item name for removing:')
        for item in self.shopping_cart_list:
            if item.get_item_name() == remove_item_name:
                self.shopping_cart_list.remove(item)
                print(remove_item_name, 'has been removed from shopping cart.')

    def checkout(self):
        # display customer name and date
        print()
        print('>>>>CHECKING OUT<<<<')
        print()
        print(self.cust_name)
        print(self.shop_date)
        print()
        total = 0
        for item in self.shopping_cart_list:
            print('Item Name:', item.get_item_name())  # repeat this price & quantity
            print('Item Price: $', item.get_item_price())
            print('Item Quantity:', item.get_item_quantity())
            total = total + item.get_item_cost()
        print('Total Cost: $', total)


def main():
    name = input('Enter Customer Name:')
    date = input('Enter Shopping Date:')
    # create an object of Customer class
    customer = Customer(name, date)

    # ask num_item: / "HOW MANY ITEMS DO YOU HAVE"
    num_item = int(input('How many items does the customer want add into shopping cart?'))
    for i in range(num_item):
        print('Item#', i + 1)
        customer.add_item()

    remove_item_num = int(input('How many items does the customer want to remove?'))
    for i in range(remove_item_num):
        customer.remove_item()

    customer.checkout()


main()

