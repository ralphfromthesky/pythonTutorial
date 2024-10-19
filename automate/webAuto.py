import pyautogui as py

# imagebtn = py.locateCenterOnScreen('btn.png')
# print('see')
# py.click(imagebtn)

imageball = py.locateCenterOnScreen('ball.png')
imageblck = py.locateCenterOnScreen('block.png')
imagefav = py.locateCenterOnScreen('fav.png')
imagepes = py.locateCenterOnScreen('pes.png')
imagerec = py.locateCenterOnScreen('rec.png')
imagepop = py.locateCenterOnScreen('pop.png')
image777 = py.locateCenterOnScreen('777.png')

imagecont = [imageball, imageblck, imagefav, imagepes, imagerec, imagepop,image777]
for image in imagecont:
    py.click(image)