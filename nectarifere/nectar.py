#With great power comes great responsibility.

from glob import glob
import os
import random
directory = os.path.dirname(os.path.abspath(__file__))

def Nectar(function):

    def new_fuction(*args, **kwargs):
        try:
            function(*args, **kwargs)
            files = glob(os.path.join(directory, 'Sounds/Kaamelott/Succes/*.wav'))
            file = random.choice(files)
            os.system('aplay ' + file)
        except:
            files = glob(os.path.join(directory ,'Sounds/Kaamelott/Echec/*.wav'))
            file = random.choice(files)
            os.system('aplay ' + file)

    return new_fuction