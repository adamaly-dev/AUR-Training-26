from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path
import re

class ItemStatus(Enum):
    AVAILABLE = 1
    CHECKED_OUT = 2
    LOST = 3    

class Library:

    def __init__(self):
        self.database = Database()
        self.items:list[LibraryItem] = []

    def input_file(self):
        data_list = self.database.from_dict()
        for data in data_list:
            data["id"] = len(self.items)
            self.items.append(Library.create_item(data))

    def checkout(self, item_id:int):
        if item_id >= len(self.items) or item_id < 0:
            raise ValueError("Item does not exist")
        self.items[item_id].checkout()
        
    def return_item(self, item_id:int):
        if item_id >= len(self.items) or item_id < 0:
            raise ValueError("Item does not exist")
        self.items[item_id].return_item()

    def mark_lost(self, item_id:int):
        if item_id >= len(self.items) or item_id < 0:
            raise ValueError("Item does not exist")
        self.items[item_id].mark_lost()

    def find_by_title(self, title:str):
        for item in self.items:
            if item.title.lower() == title.lower():
                return str(item)
        return "There is no item with this title"

    @classmethod
    def create_item(cls, data:dict):
        return LibraryItem.from_dict(data)

    def add_item(self, data:dict):
        data["id"] = len(self.items)
        data["status"] = ItemStatus.AVAILABLE
        self.items.append(Library.create_item(data))

    def file_output(self):
        self.database.to_dict(self.items)

    def list_available(self):
        for item in sorted(self.items):
            if item.status == ItemStatus.AVAILABLE:
                print(str(item))

class Database:

    def __init__(self):
        self.file_path = Path(__file__).parent / "database.txt"
    
    def from_dict(self):
        data_list:dict[str] = []
        if not self.file_path.exists():
            return data_list
        with open(self.file_path, "r") as f:
            for line in f:
                if not line:
                    continue    
                words = [word.strip() for word in re.split(r'[|=]', line)]
                data = dict(zip(words[0::2], words[1::2]))
                data_list.append(data)
        return data_list

    def to_dict(self, items):
        with open(self.file_path, "w") as f:
            for item in items:
                f.write(repr(item)+"\n")

class LibraryItem(ABC):
    loan_days:int
    _registry = {}

    def __init__(self, id:int, title:str, status:ItemStatus):
        id = int(id)
        self.id = id
        self.title = title
        if isinstance(status, str):
            self._status = ItemStatus[status]
        else:
            self._status = status

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._registry[cls.__name__] = cls

    def __lt__(self, other:"LibraryItem"):
        return self.title < other.title

    @property
    def status(self) -> ItemStatus:
        return self._status

    def checkout(self):
        if self._status != ItemStatus.AVAILABLE:
            raise ValueError("Item isn't available")
        self._status = ItemStatus.CHECKED_OUT
        print(f"Checkout of item {self.id} has been successful")

    def return_item(self):
        if self._status == ItemStatus.AVAILABLE:
            raise ValueError("Item is in the library")
        self._status = ItemStatus.AVAILABLE
        print(f"Return of item {self.id} has been successful")

    def mark_lost(self):
        self._status = ItemStatus.LOST
        print(f"Item {self.id} is lost")

    @classmethod
    def from_dict(cls, data:dict):
        return cls._registry[data["type"]].from_dict(data)

class Book(LibraryItem):
    loan_days = 21

    def __init__(self, id:int, title:str, author:str, isbn:str, status:ItemStatus):
        if not Book.validateISBN(isbn):
            raise ValueError("Invalid ISBN")
        super().__init__(id, title, status)
        self.isbn = isbn
        self.author = author

    def __str__(self):
        return f"ID: #{self.id}, {self.title} (Book) - {self._status.name}"

    def __repr__(self):
        return f"type=Book|title={self.title}|author={self.author}|isbn={self.isbn}|status={self.status.name}"

    @classmethod
    def from_dict(cls, data):
        return Book(data["id"], data["title"], data["author"], data["isbn"], data["status"])
    
    @staticmethod
    def validateISBN(isbn:str):
        if len(isbn) != 13 or not isbn.isdigit():
            return False
        sum = 0
        for i in range(0, 13):
            sum += (int(isbn[i])-int('0'))*(i%2*2+1)
        sum %= 10
        return (sum == 0)

class DVD(LibraryItem):
    loan_days = 5

    def __init__(self, id:int, title:str, director:str, status:ItemStatus):
        super().__init__(id, title, status)
        self.director = director

    def __str__(self):
        return f"ID: #{self.id}, {self.title} (DVD) - {self._status.name}"

    def __repr__(self):
        return f"type=DVD|title={self.title}|director={self.director}|status={self.status.name}"

    @classmethod
    def from_dict(cls, data):
        return DVD(data["id"], data["title"], data["director"], data["status"])

class Magazine(LibraryItem):
    loan_days = 14

    def __init__(self, id, title, issue, status):
        super().__init__(id, title, status)
        self.issue = issue

    def __str__(self):
        return f"ID: #{self.id}, {self.title} (Magazine) - {self._status.name}"
    
    def __repr__(self):
        return f"type=Magazine|title={self.title}|issue={self.issue}|status={self.status.name}"

    @classmethod
    def from_dict(cls, data):
        return Magazine(data["id"], data["title"], data["issue"], data["status"])

def main() -> None:
    library = Library()
    library.input_file()
    while True:
        query = int(input("Query type (1/2/3/4/5/6/7): ").strip())
        if query <= 3:
            item_id = int(input("Item ID: ").strip())
            if query == 1:                              #Checkout item
                library.checkout(item_id)
            elif query == 2:                            #Return item
                library.return_item(item_id)
            elif query == 3:                            #Mark lost
                library.mark_lost(item_id)
        elif query == 4:                                #List all available items
            library.list_available()
        elif query == 5:                                #Find library item by title
            title = input("Library item title: ").strip()
            print(library.find_by_title(title))
        elif query == 6:                                #Add item
            line = input("Library item data: ").strip()
            words = [word.strip() for word in re.split(r'[|=]', line)]
            data = dict(zip(words[0::2], words[1::2]))
            library.add_item(data)
        elif query == 7:                                #Output items into file
            library.file_output()
        else:
            raise ValueError("Invalid query type")

main()