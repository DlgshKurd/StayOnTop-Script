import pygetwindow as gw
import time
import win32gui
import win32con

def make_always_on_top(window):

    win32gui.SetWindowPos(window._hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    print(f'Success! {window.title} is now always on top.')

if __name__ == "__main__":
   
    time.sleep(3)
    
    focused_window = gw.getActiveWindow()
    
    make_always_on_top(focused_window)
