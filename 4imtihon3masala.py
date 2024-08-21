from os import system
system("cls")
class Market:
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.products = {}
        self.balance = 0
    def add_product(self, product: str, price: float, quantity: int) -> None:
        self.products[product] = {"price" : price,"quantity" : quantity}
    def get_products_info(self) -> str:
        natija = "Bozorda mavjud mahsulotlar:\n"
        productlar = list(self.products.keys())
        for i in range(len(productlar)):
            natija += f"{productlar[i]} - {self.products[productlar[i]]["price"]} so'm, {self.products[productlar[i]]["quantity"]} dona\n"
        return natija
    def remove_product(self, product: str) -> None: # Agar mahsulot bor bolsa ochiradi.
        productlar = list(self.products.keys())
        if product in productlar:
            self.products.pop(product)
    def add_money(self, amount: float) -> None:  # Balansga pul qo'shadi.
        self.balance += amount

    def sell(self, product: str, quantity: int) -> None: #- mahsulot va soni beriladi, narxini hisoblab, add_money() orqali balansga o'sha pulni qo'shib qo'yadi.
        self.balance += quantity * self.products[product]["price"]
        self.products[product]["quantity"] -= quantity 

# Klassdan foydalanish

bozor = Market(name="Supermarket", address="Toshkent, O'zbekiston")
# Yangi bozor yaratildi, boshlang'ich mahsulotlar va balans yo'q.
# Bozor nomi: Supermarket
# Bozor manzili: Toshkent, O'zbekiston

bozor.add_product(product="Olma", price=5000, quantity=10)
# 10 dona Olma mahsuloti qo'shildi.
# Mahsulotlar: {'Olma': {'price': 5000, 'quantity': 10}}

bozor.add_product(product="Banan", price=7000, quantity=5)
# 5 dona Banan mahsuloti qo'shildi.
# Mahsulotlar: {'Olma': {'price': 5000, 'quantity': 10}, 'Banan': {'price': 7000, 'quantity': 5}}

print(bozor.get_products_info())
# Bozorda mavjud mahsulotlar:
# Olma - 5000 so'm, 10 dona
# Banan - 7000 so'm, 5 dona

bozor.sell(product="Olma", quantity=3)
# 3 dona Olma mahsuloti sotildi. Jami: 15000 so'm
# Hisobga 15000 so'm qo'shildi. Joriy balans: 15000 so'm
# Mahsulotlar: {'Olma': {'price': 5000, 'quantity': 7}, 'Banan': {'price': 7000, 'quantity': 5}}

print(bozor.get_products_info())
# Bozorda mavjud mahsulotlar:
# Olma - 5000 so'm, 7 dona
# Banan - 7000 so'm, 5 dona

bozor.remove_product(product="Banan")
# Banan mahsuloti o'chirildi.
# Mahsulotlar: {'Olma': {'price': 5000, 'quantity': 7}}

print(bozor.get_products_info())
# Bozorda mavjud mahsulotlar:
# Olma - 5000 so'm, 7 dona
bozor.add_money(100000)
print(bozor.balance)