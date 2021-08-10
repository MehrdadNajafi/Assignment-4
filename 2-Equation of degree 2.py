from math import sqrt
import colorama
from colorama import Fore
colorama.init(autoreset=True)

a = int(input(f"pls enter a ({Fore.RED + 'a'}{Fore.RESET}x^2+bx+c=0): "))

while a == 0:
    print('ax^2 can not be 0 , pls enter another number')
    a = int(input(f"pls enter a ({Fore.RED + 'a'}{Fore.RESET}x^2+bx+c=0): "))

b = int(input(f"pls enter b (ax^2+{Fore.RED + 'b'}{Fore.RESET}x+c=0): "))
c = int(input(f"pls enter c (ax^2+bx+{Fore.RED + 'c'}{Fore.RESET}=0): "))

delta = (b**2) - (4*a*c)

if delta > 0:
    x1 = (-b + sqrt(delta) ) / (2*a)
    x2 = (-b - sqrt(delta) ) / (2*a)
    print(f'x1 = {x1}\nx2 = {x2}')

elif delta == 0:
    x = (-b) / (2*a)
    print(f'x: {x}')

elif delta < 0:
    print('x has not root')