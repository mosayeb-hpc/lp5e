"""
File makedb.py: store Person objects on a shelve database
"""
import shelve
from person import Person, Manager

bob = Person("Bob Smith")
sue = Person("Sue Jones", job="dev", pay=100000)
tom = Manager("Tom Jones", pay=50000)

db = shelve.open("persondb")        # Filename where objects are stored
for obj in (bob, sue, tom):         # Use object's name attr as key
    db[obj.name] = obj              # Store object on shelve by key
db.close()                          # Close after making changes
