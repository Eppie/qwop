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

    time.sleep(stepTime/2)


def play():
    press('o')
    time.sleep(0.2)
    press('w')
    time.sleep(0.5)
    release('o')
    release('w')

    stepTime = 3.0
    for i in range(5):
        takeStep("left", stepTime)
        takeStep("right", stepTime)

time.sleep(3)
play()
