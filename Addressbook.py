from collections import UserDict
from Record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name.value in self.data:
            print(f"Contact with name {record.name.value} already exists")
        else:
            self.update({record.name.value: record})

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact with name {name} not found")
