from abc import ABC, abstractmethod
from Book import Book
class IRepository(ABC):

    @abstractmethod
    def Add(self, book: Book):
        pass
    @abstractmethod
    def RemoveAt(self, id: int):
        pass
    @abstractmethod
    def GetAt(self, id: int):
        pass
    @abstractmethod
    def GetAll(self):
        pass
    @abstractmethod
    def FindBy(self, word: str):
        pass
    @abstractmethod
    def Update(self):
        pass