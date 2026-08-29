from enum import Enum

class ItemStatus(Enum):
    AVAILABLE = 1
    CHECKED_OUT = 2
    LOST = 3    

class LibraryItem:
    loan_days:int
    _status:ItemStatus
    id:int
    name:str

    def __init__(self, name, id):
        self._status = ItemStatus.AVAILABLE
        self.id = id
        self.name = name

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self):
        raise NotImplementedError()

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
        if self._status != ItemStatus.CHECKED_OUT:
            raise ValueError("Item is in library or is already reported lost")
        self._status = ItemStatus.LOST
        print(f"Item {self.id} is lost")

class Book(LibraryItem):
    loan_days = 21

class DVD(LibraryItem):
    loan_days = 5

class Magazine(LibraryItem):
    loan_days = 14

def main() -> None:
    library:LibraryItem = [Book("Harry Potter", 0),
                            DVD("Sonic", 1), 
                            DVD("Mario", 2), 
                            Magazine("The Atlantic", 3), 
                            Book("Dunes", 4)]
    while True:
        query = int(input("Query type (1/2/3): ").strip())
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