import pygetwindow as gw
import time
import win32gui
import win32con

def make_always_on_top(window):
    win32gui.SetWindowPos(window._hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    print(f'Success! {window.title} is now always on top.')

if __name__ == "__main__":
    for i in range(3, 0, -1):
        print(f"Switch to the window you want to stay on top. Countdown: {i}")
        time.sleep(1)

    focused_window = gw.getActiveWindow()
    make_always_on_top(focused_window)
