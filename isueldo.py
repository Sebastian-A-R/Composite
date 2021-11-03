from abc import ABCMeta,abstractmethod

class ISueldo:
    __metaclass__=ABCMeta

    @abstractmethod
    def getSueldo(self):
        pass