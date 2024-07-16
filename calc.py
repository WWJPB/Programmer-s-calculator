import math
import colorama
import sys
import os

colorama.init(autoreset = True)

class Programmer:
    def binary(self):
        total_8 = 0
        total_10 = 0
        total_16 = 0
        binary_list = []
        binary_code = input("Wprowadź kod binarny: ")
        for i in binary_code:
            if i == '0' or i == '1':
                binary_list.append(int(i))
            else:
                print("Nieprawidłowa wartość")
        for index in range(len(binary_list)):
            x = len(binary_list) - 1 - index
            element = binary_list[index]
            number = element*math.pow(2, x)
            total_10+=number
        for i in binary_code:
            if i == '0' or i == '1':
                decimal_number = int(binary_code, 2)
                oct_number = oct(decimal_number)
                hex_number = hex(decimal_number)
                total_8 = oct_number[2:]
                total_16 = hex_number[2:]
            else:
                print("Nieprawidłowa wartość")
        print("+-------+-------------+------+-------------+")
        print(f"System ósemkowy: , {colorama.Fore.CYAN}{total_8}")
        print(f"System dziesiętny: , {colorama.Fore.CYAN}{total_10}")
        print(f"System szesnastkowy: , {colorama.Fore.CYAN}{total_16}")
        print("+-------+-------------+------+-------------+")
    def decimal(self):
        total_2 = 0
        total_8 = 0
        total_16 = 0
        binary_list = []
        decimal_code = int(input("Wprowadź kod dziesiętny: "))
        total_8 = oct(decimal_code)[2:]
        total_16 = hex(decimal_code)[2:]
        if(decimal_code <= 0):
            print("Nieprawidłowa wartość")
        else:
            while decimal_code > 0:
                binary = decimal_code%2
                binary_list.append(binary)
                decimal_code = decimal_code // 2
            binary_list.reverse()
            total_2 = int(''.join(map(str, binary_list)))
        print("+-------+-------------+------+-------------+")
        print(f"System binarny: , {colorama.Fore.CYAN}{total_2}")
        print(f"System ósemkowy: , {colorama.Fore.CYAN}{total_8}")
        print(f"System szesnastkowy: , {colorama.Fore.CYAN}{total_16}")
        print("+-------+-------------+------+-------------+")
    def octal(self):
        total_2 = 0
        total_10 = 0
        total_16 = 0
        oct_code = int(input("Wprowadź kod ósemkowy: "), 8)
        if(oct_code <= 0):
            print("Nieprawidłowa wartość")
        else:
            binary = bin(oct_code)
            total_2 = binary[2:]
            total_10 = int(total_2, 2)
            hexadecimal = hex(total_10)
            total_16 = hexadecimal[2:]
        print("+-------+-------------+------+-------------+")
        print(f"System binarny: , {colorama.Fore.CYAN}{total_2}")
        print(f"System dziesiętny: , {colorama.Fore.CYAN}{total_10}")
        print(f"System szesnastkowy: , {colorama.Fore.CYAN}{total_16}")
        print("+-------+-------------+------+-------------+")
    def hexadecimal(self):
        total_2 = 0
        total_8 = 0
        total_10 = 0
        hex_code = input("Wprowadź kod szesnastkowy: ")
        if not all(c in "0123456789ABCDEF" for c in hex_code.upper()):
            print("Nieprawidłowa wartość")
        else:
            for i, digit in enumerate(reversed(hex_code.upper())):
                if digit.isdigit():
                    value = int(digit)
                else:
                    value = ord(digit) - ord('A') + 10
                total_10 += value * 16**i
            total_8 = oct(total_10)[2:]
            total_2 = bin(total_10)[2:]
        print("+-------+-------------+------+-------------+")
        print(f"System binarny: , {colorama.Fore.CYAN}{total_2}")
        print(f"System ósemkowy: , {colorama.Fore.CYAN}{total_8}")
        print(f"System dziesiętny: , {colorama.Fore.CYAN}{total_10}")
        print("+-------+-------------+------+-------------+")


class Binary(Programmer):
    pass
class Decimal(Programmer):
    pass
class Octal(Programmer):
    pass
class Hexadecimal(Programmer):
    pass

def exit():
    sys.Exit(0)

def clear():
    os.system('cls')

def menu():
    print(f"{colorama.Fore.YELLOW}+-------+-------------+------+-------------+\n")
    print("binary - przelicza z systemu binarnego")
    print("octal - przelicza z systemu ósemkowego")
    print("decimal - przelicza z systemu dziesiętnego")
    print("hexadecimal - przelicza z systemu szesnastkowego")
    print("exit - zamyka program")
    print("clear - czysci konsole")
    print("help - otwiera menu pomocy\n")
    print(f"{colorama.Fore.YELLOW}+-------+-------------+------+-------------+\n")

BINARY = Binary()
DECIMAL = Decimal()
OCTAL = Octal()
HEXADECIMAL = Hexadecimal()

print("Type help to open help menu\n")

while True:
    user = input(f"{colorama.Fore.MAGENTA}${colorama.Fore.WHITE}")
    match user:
        case 'binary':
            BINARY.binary()
        case 'octal':
            OCTAL.octal()
        case 'decimal':
            DECIMAL.decimal()
        case 'hexadecimal':
            HEXADECIMAL.hexadecimal()
        case 'exit':
            exit()
        case 'clear':
            clear()
        case 'help':
            menu()
        case _:
            print("Wprowadzona komenda nie istnieje")