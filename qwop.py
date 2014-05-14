import tesseract
import time
from PIL import ImageGrab
import time
import win32api
import win32con

VK_CODE = {'q': 0x51, 'w': 0x57, 'o': 0x4f, 'p': 0x50}


def press(x):
	win32api.keybd_event(VK_CODE[x], 0, 0, 0)


def release(x):
	win32api.keybd_event(VK_CODE[x], 0, win32con.KEYEVENTF_KEYUP, 0)


def takeStep(leg, stepTime):
    if (leg == 'left'):
        press('w')
        press('o')

    if (leg=='right'):
        press('q')
        press('p')

    time.sleep(stepTime/2)

    release('q')
    release('w')
    release('o')
    release('p')


def play(downtime, waittime):
    gameover = getscore()
    while not gameover[0]:
        press('w')
        press('q')
        press('p')
        time.sleep(downtime)
        release('q')
        time.sleep(waittime)
        gameover = getscore()
    release('q')
    release('w')
    release('p')


def getscore():
    ''' Takes a screenshot and uses OCR to determine the distance ran.
        Returns a list. The first element is a boolean value indicating if the game is won
        The second is either None, the string 'won', or the r value of the pixel at 0,0 in the screenshot
        In the last case, there will be a 3rd and 4th element that are the g and b values, respectively.
    '''
    im = ImageGrab.grab([612,433,658,458])
    r, g, b = im.getpixel((0, 0))
    if r == 29 and g == 43 and b == 56:
        im.save('screenshot.png')

        api = tesseract.TessBaseAPI()
        api.Init(".","eng",tesseract.OEM_DEFAULT)
        mImgFile = 'screenshot.png'
        try:
            result = tesseract.ProcessPagesWrapper(mImgFile,api).strip()
        except AttributeError:
            result = None
        except ValueError:
            result = None
        return [True, result]
    elif r == 237 and g == 237 and b == 237:
        return [True, 'won']
    else:
        return [False, r, g, b]

        
time.sleep(1)

downtime = 0.2
waittime = 0.65

start = time.clock()
play(downtime, waittime)
end = time.clock()

f = open('records.txt', 'a+')
f.write('result: ' + str(getscore()[1]) + ', ' + 'TIME: ' + str(end-start) + ', downtime: ' + str(downtime) + ', waittime: ' + str(waittime) + '\n')
