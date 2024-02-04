#python setup.py build
import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "build_exe": "samuQueue_EXE",
    "packages": ["os", "customtkinter", "win32com.client", "tkinter", "pyautogui", "time", "threading"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "samuQueue",
    version = 1.0,
    description = None,
    options = {"build_exe": build_exe_options},
    executables = [Executable("samuQueue.py", base=base, icon="favicon.ico")]
)


