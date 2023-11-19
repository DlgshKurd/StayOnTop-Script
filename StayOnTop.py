import pygetwindow as gw
import time
import win32gui
import win32con

def toggle_always_on_top(window):
    # Get the window style
    style = win32gui.GetWindowLong(window._hWnd, win32con.GWL_EXSTYLE)

    # Check if the window is currently set as always on top
    if style & win32con.WS_EX_TOPMOST:
        # If yes, remove the always on top style
        win32gui.SetWindowPos(window._hWnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f'Success! {window.title} is no longer always on top.')
    else:
        # If not, set the always on top style
        win32gui.SetWindowPos(window._hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f'Success! {window.title} is now always on top.')

if __name__ == "__main__":
    for i in range(3, 0, -1):
        print(f"Switch to the window you want to toggle. Countdown: {i}")
        time.sleep(1)

    focused_window = gw.getActiveWindow()
    toggle_always_on_top(focused_window)
