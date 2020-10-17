import pyautogui
import time

word = open("word", 'r')
time.sleep(10)

for words in word:
    pyautogui.typewrite(words)
    pyautogui.press('enter')
    time.sleep(5)