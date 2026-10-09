from abc import ABC, abstractmethod


class ExtracteurDeJus(ABC):

    def __init__(self, function):
        self.function = function

    @abstractmethod
    def success(self):
        pass

    @abstractmethod
    def failure(self):
        pass

    def __call__(self, *args, **kwargs):


        caught_exception = None
        res = None

        try:

            res = self.function(*args, **kwargs)
            self.success()

        except Exception as e:

            caught_exception = e
            self.failure()

        finally:

            if caught_exception is not None:
                raise caught_exception

            return res
