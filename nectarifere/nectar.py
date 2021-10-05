#"With great power comes great responsibility." M.S.

from glob import glob
import os
import random

from play_sounds import play_file
from pathlib import Path
directory = os.path.dirname(os.path.abspath(__file__))


def nectar(function):

    success_files = glob(os.path.join(directory, 'Sounds', 'Kaamelott', 'Succes', '*.wav'))
    fail_files = glob(os.path.join(directory, 'Sounds', 'Kaamelott', 'Echec', '*.wav'))

    def new_function(*args, **kwargs):

        file = None

        try:
            function(*args, **kwargs)
            file = Path(random.choice(success_files), encoding=None)

        except Exception as e:
            print(e)
            file = Path(random.choice(fail_files), encoding=None)

        finally:
            play_file(file)

    return new_function
