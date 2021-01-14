import pyautogui, time
time.sleep(4)
k=0
a=1
for i in range(100):
    if(a == 1):
        pyautogui.click()
        pyautogui.typewrite('@xristis1 @xristis2 @xristis3')
        pyautogui.press("enter")
        k=k+1
        a=2
    elif(a == 2):
        pyautogui.click()
        pyautogui.typewrite('@xristis1 @xristis2 @xristis3')
        pyautogui.press("enter")
        k=k+1
        a=3
    else:
        pyautogui.click()
        pyautogui.typewrite('@xristis1 @xristis2 @xristis3')
        pyautogui.press("enter")
        k=k+1
        a=1
print(k)