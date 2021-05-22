import pyfiglet
import random
import time 
import termcolor
from datetime import datetime
from pyfiglet import Figlet
font="digital"
F=Figlet().renderText("b o s s")
print(F)
print("\033[1;32;40m  boss \033[0m 1;32;40m            \033[0;32;47m kishan     \033[0m 0;32;47m               \033[0;37;43m modi     \033[0m 0;37;43m")

fig=Figlet(font)
print(fig.renderText("b o s s"))
print(termcolor.colored(("maker of tool is -- kishan"),"red"))
a = pyfiglet.figlet_format("K i s h a n")
print(a)
print(termcolor.colored(("-" * 40),'green'))
print()
print("\033[1;32;40m year-month-date", datetime.now(), "milliseconds")
print(termcolor.colored(("-" * 40),"blue"))
b = pyfiglet.figlet_format(
    str(input("enter name of festival and. \ngive space in each letter -: ")))
print("lets celebrate -: ;) ")
for m in range(10, 0, -1):
  time.sleep(1)
  print(termcolor.colored((m),"green"))
print(b, "\n enjoy")
print(termcolor.colored((
    " now if you  want to play game  \n press one and press enter \n if not want to play press 2 -:"),"yellow"))
i = int(input())
if i == 1:
	print(termcolor.colored(("chlo head toss ka game khilata hu 😂","red")))
	coin = ("head","tail")
	kishan=random.choice(coin)
	
	s = input( "head or tail enter your choice and press entr --:")
	if s==kishan :
	  print (termcolor.colored(("you win ▄︻̷┻═━一")))
	else:
	  print ("failed!!")
	  print ()
else:
	print("good bye ")
