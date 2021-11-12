from abc import ABC, abstractmethod


class ExtracteurDeJus(ABC):
    """
    Abstract class for creating success/failure patterns with arbitrary actions
    """

    def __init__(self, function):
        self._function = function

    @abstractmethod
    def success(self):
        '''
        Abstract method called when the decorated function succeeds
        '''
        pass

    @abstractmethod
    def failure(self):
        '''
        Abstract method called when the decorated function fails
        '''
        pass

    def __call__(self, *args, **kwargs):
        '''
        Decorating the function call
        '''
        caught_exception = None
        res = None

        try:

            res = self._function(*args, **kwargs)
            self.success()

        except Exception as e:

            caught_exception = e
            self.failure()

        finally:

            if caught_exception is not None:
                raise caught_exception

            return res
