import pyautogui
import win32api, win32con
import win32gui

print pyautogui.size()
print pyautogui.position()

#Point(x=1893, y=686)
#pyautogui.moveTo(1893,686)
# for i in range(10):
#    pyautogui.dragTo(1893,686, button='left')


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

# from msvcrt import getch
# while True:
#     key = ord(getch())
#     for i in range(10):
#         click(1395,648)
#         break


 
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))




from msvcrt import getch
while True:
    key = ord(getch())
    if key == 27: #ESC
            exit()
    if key == 73: #page up
        for i in range(50):
            click(1394,143)
    if key == 81: #page down
        for i in range(50):
            click(1395,648)
    if key == 72: #Up arrow
        for i in range(10):
            click(1394,143)
    if key == 80: #Down arrow
        for i in range(10):
            click(1395,648)
 

    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "cmd.exe" in i[1].lower():
            print i
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break







