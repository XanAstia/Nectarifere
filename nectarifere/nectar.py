#"With great power comes great responsibility." M.S.

from glob import glob
import os
import random
from play_sounds import play_file

directory = os.path.dirname(os.path.abspath(__file__))

def Nectar(function):

    success_files = glob(os.path.join(directory, 'Sounds/Kaamelott/Succes/*.wav'))
    fail_files = glob(os.path.join(directory, 'Sounds/Kaamelott/Echec/*.wav'))

    def new_function(*args, **kwargs):

        try:
            function(*args, **kwargs)
            file = random.choice(success_files)

        except Exception as e:
            print(e)
            file = random.choice(fail_files)

        finally:
            play_file(file)

    return new_function