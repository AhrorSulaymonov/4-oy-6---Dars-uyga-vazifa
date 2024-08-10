from os import system
system("cls")
def hex_to_binary(HEX : str):
    hex_to_binar = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        '3' : '0011',
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        '7' : '0111',
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        'B' : '1011',
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        'F' : '1111'
    }
    binary = ""
    keylar = hex_to_binar.keys()
    for i in HEX:
        if i in keylar:
            binary += hex_to_binar[i]
        else:
            return "error"
    return binary
print(hex_to_binary("12DCEE"))
