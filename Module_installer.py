def module_check():
    try:
        import subprocess
        import requests as pd
        print("I am BACK:::::::::::::")
        print(pd)
        print(1/0)
    except ImportError as e:
        import os
        mod = str(e)
        mod = list(mod.split())
        cmd = 'pip3 install '+mod[-1]+';'+'pip install '+mod[-1]
        print(cmd)
        os.system(cmd)
        print("Hello world again")
        module_check()
        
module_check()