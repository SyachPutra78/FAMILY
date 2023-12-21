import os, sys
os.system("git pull")
try:
    __import__("FAMILY").FAMILY()
except Exception as e:
    exit(str(e))
