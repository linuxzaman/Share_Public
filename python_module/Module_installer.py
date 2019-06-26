##Python program to check weather packages are installed or not
#date and time : 7:59 PM 25-Jun-19
def module_check():
    try:
        import subprocess
        import requests as pd
        print(pd)
        
    except ImportError as e:
        import os
        mod = str(e)
        mod = list(mod.split())
        cmd = 'pip3 install '+mod[-1]+';'+'pip install '+mod[-1]
        os.system(cmd)
        module_check()
        
module_check()