from os import system
system("cls")
class Texnika:
    def __init__(self, brand : str, model : str, type : str) -> None:
        self.brand = brand
        self.model = model
        self.type = type
    def more_info(self) -> str:
        return f"""
brand = {self.brand}
model = {self.model}
type = {self.type}"""
class Notebooks(Texnika):
    def __init__(self, brand : str, model : str, type : str, video_card : str, ram : int, display : str) -> None:
        super().__init__(brand, model, type)
        self.video_card = video_card
        self.ram = ram
        self.display = display
    def more_info(self):
        return super().more_info() +f"""
video_card = {self.video_card}
ram = {self.ram}
display = {self.display}
"""
class Televisions(Texnika):
    def __init__(self,  brand : str, model : str, type : str, size: str, display: str) -> None:
        super().__init__(brand, model, type)
        self.size = size
        self.display = display
    def more_info(self):
        return super().more_info() + f"""
size = {self.size}
display = {self.display}
"""
class Smartphones(Texnika):
    def __init__(self, brand: str, model: str, type: str, size: str, sim_count : int) -> None:
        super().__init__(brand, model, type)
        self.size = size
        self.sim_count = sim_count
    def more_info(self) -> str:
        return super().more_info()  + f"""
size = {self.size}
sim_count = {self.sim_count}
"""
redmi = Smartphones("Redmi", "Redmi 8", "buzuq", "bilmiman dyum", 2)
print(redmi.more_info())