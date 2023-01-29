'''
"With great power comes great responsibility." M.S.
'''

import os
import random
from glob import glob
from .extracteur import ExtracteurDeJus
from playsound import playsound
from pathlib import Path
import time
directory = os.path.dirname(os.path.abspath(__file__))


class nectar(ExtracteurDeJus):

    def __init__(self, function):
        super().__init__(function)
        self.success_files = glob(os.path.join(directory, 'Sounds', 'Kaamelott', 'Succes', '*.wav'))
        self.failure_files = glob(os.path.join(directory, 'Sounds', 'Kaamelott', 'Echec', '*.wav'))

    def success(self):
        p = Path(random.choice(self.success_files), encoding=None)
        playsound(str(p), False)
        time.sleep(1)

    def failure(self):
        p = Path(random.choice(self.failure_files), encoding=None)
        playsound(str(p), False)
        time.sleep(1)
