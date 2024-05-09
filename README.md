# MODULE 9. Homework. Basics of Working with Classes goit-pycore-hw-06

## Technical task

## Develop a system for managing an address book.

### Entities:

- **Field**: Base class for record fields.
- **Name**: Class for storing contact names. A required field.
- **Phone**: Class for storing phone numbers. Has format validation (10 digits).
- **Record**: Class for storing contact information, including name and list of phones.
- **AddressBook**: Class for storing and managing records.

### Functionality:

- **AddressBook:** Adding records.
- **Searching** records by name.
- **Deleting** records by name.
- **Record:** Adding phones.
- **Deleting** phones.
- **Editing** phones.
- **Searching** for a phone.

### Recommendations for implementation

As a starting point, you can take the following basic code to implement this homework assignment:

```
from collections import UserDict

class Field:
def init(self, value):
self.value = value

python
Copy code
def **str**(self):
return str(self.value)
class Name(Field):

# implementation of the class

pass

class Phone(Field):

# implementation of the class

pass

class Record:
def init(self, name):
self.name = Name(name)
self.phones = []

python
Copy code

# implementation of the class

def **str**(self):
return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
class AddressBook(UserDict):

# implementation of the class

pass
```

After implementing your code, it should work as follows:

```
Creating a new address book
python
Copy code
book = AddressBook()

# Creating a record for John

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Adding John's record to the address book

book.add_record(john_record)

# Creating and adding a new record for Jane

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Printing all records in the book

for name, record in book.data.items():
print(record)

# Finding and editing John's phone

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john) # Output: Contact name: John, phones: 1112223333; 5555555555

# Searching for a specific phone in John's record

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}") # Output: 5555555555

# Deleting Jane's record

book.delete("Jane")
```

In the next homework assignment, we will add this logic to our bot.

## Assessment criteria

### Class AddressBook:

- Implemented the add_record method, which adds a record to self.data.
- Implemented the find method, which finds a record by name.
- Implemented the delete method, which deletes a record by name.

### Class Record:

- Implemented storage of the Name object in a separate attribute.
- Implemented storage of the list of Phone objects in a separate attribute.
- Implemented methods for adding - add_phone/removing - remove_phone/editing - edit_phone/searching for Phone objects - find_phone.

### Class Phone:

- Implemented phone number validation (must check for 10 digits).
