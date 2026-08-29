from enum import Enum
from pathlib import Path
import re

class ItemStatus(Enum):
    AVAILABLE = 1
    CHECKED_OUT = 2
    LOST = 3    

class LibraryItem:
    loan_days:int
    _status:ItemStatus
    id:int
    title:str

    def __init__(self, id:int, title:str, status:ItemStatus):
        self.id = id
        self.title = title
        self._status = ItemStatus[status]

    def __lt__(self, other:"LibraryItem"):
        return self.title < other.title

    @property
    def status(self) -> ItemStatus:
        return self._status
    
    @status.setter
    def status(self, new_status:ItemStatus):
        self._status = new_status

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
    def from_dict(cls, library:list["LibraryItem"]):
        file_path = Path(__file__).parent / "database.txt"
        with open(file_path, "r") as f:
            for line in f:
                if not line:
                    continue    
                words = [word.strip() for word in re.split(r'[|=]', line)]
                data = dict(zip(words[2::2], words[3::2]))
                data["id"] = len(library)
                if words[1] == "Book":
                    library.append(Book(**data))
                elif words[1] == "DVD":
                    library.append(DVD(**data))
                elif words[1] == "Magazine":
                    library.append(Magazine(**data))
                else:
                    raise TypeError("Library Item Type does not exist")

class Book(LibraryItem):
    loan_days = 21

    def __init__(self, id:int, title:str, author:str, isbn:str, status:ItemStatus):
        if not Book.validateISBN(isbn):
            raise ValueError("Invalid ISBN")
        super().__init__(id, title, status)
        self.isbn = isbn
        self.author = author

    def __repr__(self):
        return f"ID: #{self.id}, {self.title} (Book) - {self._status.name}"
    
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

    def __repr__(self):
        return f"ID: #{self.id}, {self.title} (DVD) - {self._status.name}"

class Magazine(LibraryItem):
    loan_days = 14

    def __init__(self, id, title, issue, status):
        super().__init__(id, title, status)
        self.issue = issue

    def __repr__(self):
        return f"ID: #{self.id}, {self.title} (Magazine) - {self._status.name}"

def main() -> None:
    library:LibraryItem = []
    LibraryItem.from_dict(library)
    while True:
        query = int(input("Query type (1/2/3/4): ").strip())
        if query == 4:
            for item in library:
                print(repr(item))
            continue
        item_id = int(input("Item ID: ").strip())
        if item_id >= len(library):
            raise("Item does not exist")
        if query == 1:
            library[item_id].checkout()
        elif query == 2:
            library[item_id].return_item()
        elif query == 3:
            library[item_id].mark_lost()
        else:
            raise ValueError("Invalid query type")

main()