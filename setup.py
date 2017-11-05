import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os", "pygame"],
                     "include_files": ["classes", "constants.py", "images", "levels"]
                     }


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "MacGyverMaze",
      version = "0.1",
      description = "The Project No. 3 labyrinth escape game",
      options = {"build.exe": build_exe_options},
      executables = [Executable("MacGyverMaze.py", base=base)])
