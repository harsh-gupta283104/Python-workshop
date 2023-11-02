import pyautogui as pt
import time

l=int(input("enter no of time"))
m=input("enter text")

time.sleep(4)

i=0
while i<=l:
    pt.typewrite(m)
    pt.press("enter")
    i=i+1
    
#learn complete concepts of pyautogui 