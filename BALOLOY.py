import os
import sys 
import importlib

os.system("git pull")

try:
    importlib.import_module("BALOLOYA").KAYATA() 
except Exception as e: 
    exit(str(e))
