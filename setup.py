import sys
from cx_Freeze import setup, Executable

base = None
copyDependentFiles = True
silent = True
base = None
packages = ['pyautogui']
includes = ['random', 'os', 'pandas']
excludes = []

if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "jiggler",
version = "1.0",
options = {"build_exe": {"includes":includes, "excludes":excludes, "packages": packages}},
executables = [Executable("jiggler.py", base=base)])