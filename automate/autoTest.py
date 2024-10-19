import pyautogui as py
import time as t

py.hotkey('win', 'd')
py.press('win')
py.write('calculator')
py.press('enter')
t.sleep(1)

imageSeven = py.locateCenterOnScreen('7.png')
imageTwo = py.locateCenterOnScreen('2.png')
imageX = py.locateCenterOnScreen('x.png')

# imageOne = py.locateCenterOnScreen('1.png')
# imageThree = py.locateCenterOnScreen('3.png')
# imageFour= py.locateCenterOnScreen('4.png')
# imageFive = py.locateCenterOnScreen('5.png')
# imageSix = py.locateCenterOnScreen('6.png')
# imageSeven = py.locateCenterOnScreen('7.png')
# imageEight = py.locateCenterOnScreen('8.png')
# imageNine = py.locateCenterOnScreen('9.png')
# imageZero = py.locateCenterOnScreen('zero.png')
# imagePlus = py.locateCenterOnScreen('plus.png')


# if(imageSeven and imageTwo):
# while imageSeven and imageTwo:
click = 0
while imageSeven:
    # print('see them')
    py.click(imageSeven)
    click += 1
    # py.click(imageTwo)
    if(click == 10):
        print('click 10 times')
        break
py.click(imageTwo)
# py.click(imagePlus)
# py.click(imageTwo)
# print('already click them')

# print('i click seven')


# click_Count = 0
# while click_Count < 10:
#     py.click()
    # py.click(py.locateCenterOnScreen('plus.png'))
    # py.click(py.locateCenterOnScreen('2.png'))
    # py.click(py.locateCenterOnScreen('7.png'))
    # py.click(py.locateCenterOnScreen('plus.png'))
    # py.click(py.locateCenterOnScreen('2.png'))
# py.press('enter')
