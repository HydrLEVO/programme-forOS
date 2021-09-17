import pygame
import time
import os
import game
import platform


print(***
                                              🇼​​​​​🇪​​​​​🇱​​​​​🇨​​​​​🇴​​​​​🇲​​​​​🇪​​​​​ 🇹​​​​​🇴​​​​​ 🇹​​​​​🇭​​​​​🇪​​​​​ 
                                                       🇷​​​​​🇪​​​​​🇦​​​​​🇱​​​​​🇲​​​​​
***)
print("""

[a] start Realm

[Q] quit
""")

select = input("[?]: ")


if select == 'a':
  print("starting Realm...")
    os.startfile("Realm.py")
    input()
    
if select == 'Q':
  print("are you sure you want to quit?  [y/n]")
   if select == 'y':
    os.startfile("DESKTOP")
   if select == 'n':
