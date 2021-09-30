#"With great power comes great responsibility." M.S.

from glob import glob
import os
import random
from playsound import playsound
directory = os.path.dirname(os.path.abspath(__file__))

def Nectar(function):

    def new_function(*args, **kwargs):
        try:
            function(*args, **kwargs)
            files = glob(os.path.join(directory, 'Sounds', 'Kaamelott', 'Succes', '*.wav'))
            file = random.choice(files)
            playsound(file)
        except:
            files = glob(os.path.join(directory, 'Sounds', 'Kaamelott', 'Echec', '*.wav'))
            file = random.choice(files)
            playsound(file)

    return new_function