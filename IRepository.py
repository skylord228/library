from abc import ABC, abstractmethod
from Book import Book
class IRepository(ABC):

    phoneNumber: str
    emailAdress: str

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
    def FindBy(self):
        pass