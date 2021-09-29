#With great power comes great responsibility.

from glob import glob
import os
import random

def Nectar(function):

    def new_fuction(*args, **kwargs):
        try:
            function(*args, **kwargs)
            files = glob('Sounds/Kaamelott/Succes/*.wav')
            file = random.choice(files)
            os.system('aplay ' + file)
        except:
            files = glob('Sounds/Kaamelott/Echec/*.wav')
            file = random.choice(files)
            os.system('aplay ' + file)

    return new_fuction