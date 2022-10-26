from asciimatics.screen import Screen
from PIL import Image
import time
import sys
import numpy as np
import cv2

def ascii_img(img, scale, reverse=False): 
    # Transform Image to Ascii text
    # img: PILLOW Image Object
    # scale: (height, width)

    gscale = "  .:-=+*#%@" 
    if reverse: gscale = gscale[::-1]

    h,w = scale
    img  = img.resize((w,h)).convert('L')
    arr_img =  np.array(img)

    max_ = np.max(arr_img)
    min_ = np.min(arr_img)

    values = np.linspace(min_, max_ ,len(gscale))

    ascii_img = []
    for fil in arr_img:
        a_fil = ''
        for col in fil:
            c = 0
            while col > values[c]:
                 c += 1
            a_fil += gscale[c]
        ascii_img.append(a_fil)

    return ascii_img


def update(screen, ascii_, out): 
    # Keyboard events handler 

    global reverse

    ev = screen.get_key()
    if ev  == ord('q'):
        return sys.exit()
    if ev == ord('r'):
        reverse = reverse != True
    if ev == ord('c'):
        with open(f'captures/capture_{out}.txt', 'w') as file:
            file.write('\n'.join(ascii_))
        out += 1
    return out

def demo(screen):
    start = time.time()
    frames = 0
    out = 0

    while True:

        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)

        ascii_ = ascii_img(img, screen.dimensions, reverse)

        for i in  range(len(ascii_)):
            for u in range(len(ascii_[i])):
                screen.print_at(ascii_[i][u], u, i)

        out = update(screen, ascii_, out)

        frames += 1
        elapsed = time.time() - start
        fps = int(frames / elapsed)
        screen.print_at(f'  {fps} FPS ', 0, 0)

        screen.refresh()

        if screen.has_resized():
            screen.clear()
            return new_screeen()

        time.sleep(0.0001)

def new_screeen():
    Screen.wrapper(demo)

reverse = False
if len(sys.argv) > 1:
    if sys.argv[1] == '-r':
        reverse = True

vid = cv2.VideoCapture(0)
new_screeen()


