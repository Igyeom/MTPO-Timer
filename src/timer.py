import easyocr
import eel
import dxcam
from PIL import Image
from time import sleep

reader = easyocr.Reader(['en'])

eel.init('web')

camera = dxcam.create()

@eel.expose
def screenshot():
    frame = camera.grab()
    sleep(0.2)
    try:
        im = Image.fromarray(frame).resize((960, 540))
    except AttributeError:
        return
    im.save("web/screenshot.png")

@eel.expose
def cropped_result(x, y, w, h):
    im = Image.open("web/screenshot.png").crop(tuple(map(int,(x, y, int(x)+int(w), int(y)+int(h)))))
    processed = Image.new('L', (int(w), int(h)))
    xpos = ypos = 0
    for i in im.convert('L').getdata():
        if i > 225:
            processed.putpixel((xpos, ypos), 255)
        else:
            processed.putpixel((xpos, ypos), 0)
        xpos += 1
        if xpos % int(w) == 0:
            xpos = 0
            ypos += 1
        
    processed.save("web/processed.png")
    
    if im.getdata()[0] == (20, 18, 167):
        return reader.readtext("web/processed.png", detail=0)[0].replace(' ', '').replace(',', '.')
    else:
        return ''


eel.start('main.html')