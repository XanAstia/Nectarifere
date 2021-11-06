#"With great power comes great responsibility." M.S.

from glob import glob
import os
import random

from PIL import Image
from pathlib import Path
directory = os.path.dirname(os.path.abspath(__file__))


def falzar(function):

    success_files = glob(os.path.join(directory, 'Pictures', 'Succes', '*.jpg'))
    fail_files = glob(os.path.join(directory, 'Pictures', 'Echec', '*.jpg'))

    def new_function(*args, **kwargs):

        file = None
        caught_exception = None

        try:
            function(*args, **kwargs)
            file = Path(random.choice(success_files), encoding=None)

        except Exception as e:

            caught_exception = e
            file = Path(random.choice(fail_files), encoding=None)

        finally:
            with Image.open(file) as img:
                img.show()
            if caught_exception is not None:
                raise caught_exception

    return new_function
