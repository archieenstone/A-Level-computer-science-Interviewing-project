# Source - https://stackoverflow.com/a/65175024
# Posted by Simon Flückiger, modified by community. See post 'Timeline' for change history
# Retrieved 2026-08-05, License - CC BY-SA 4.0

import win32api
import win32gui

WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

hwnd_active = win32gui.GetForegroundWindow()
win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)

