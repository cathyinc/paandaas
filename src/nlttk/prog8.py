def display8():
    code = '''class Client:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def place_order(self, order):
        print(f"Order placed by {self.name}: {order}")

class Worker:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def take_order(self, client, order):
        print(f"Order taken by {self.name} (ID: {self.id}) from {client.name}: {order}")


class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ${self.price}")

client1 = Client("John Doe", "123 Main St", "123-456-7890")
worker1 = Worker("Alice", "WORK1")
food1 = FoodItem("Pizza", 10.99)
client1.place_order("2 pizzas and 1 coke")
worker1.take_order(client1, "2 pizzas and 1 coke")
food1.display()'''
    print(code)
