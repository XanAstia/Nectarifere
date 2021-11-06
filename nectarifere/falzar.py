'''
"With great power comes great responsibility." M.S.
'''

import os
import random
from glob import glob
from .extracteur import ExtracteurDeJus
from PIL import Image
from pathlib import Path
directory = os.path.dirname(os.path.abspath(__file__))


class falzar(ExtracteurDeJus):

    def __init__(self, function):
        super().__init__(function)
        self.success_files = glob(os.path.join(directory, 'Pictures', 'Succes', '*.jpg'))
        self.failure_files = glob(os.path.join(directory, 'Pictures', 'Echec', '*.jpg'))

    def success(self):
        with Image.open(Path(random.choice(self.success_files))) as img:
            img.show()

    def failure(self):
        with Image.open(Path(random.choice(self.failure_files))) as img:
            img.show()
