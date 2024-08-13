from os import system
system("cls")
class Notebook:
    def __init__(self, firmasi ,model,CPU,DDR,price) -> None:
        self.firmasi = firmasi
        self.model = model
        self.CPU = CPU
        self.DDR = DDR
        self.price = price
    def info_notebook(self):
        print(f"""
                firmasi - {self.firmasi}
                model - {self.model}
                CPU - {self.CPU}
                DDR - {self.DDR}
                price - {self.price}$
        """)
notebook = Notebook("hp", "victus", "Core i5 11 - avlod", "bilmiman", 700)
notebook.info_notebook()