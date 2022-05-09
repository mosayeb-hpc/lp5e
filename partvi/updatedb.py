"""
File updatedb.py: update Person object on database
"""
import shelve


db = shelve.open("persondb")

for k in sorted(db):
    print(k, '\t=>', db[k])

sue = db['Sue Jones']
sue.give_raise(.10)
db['Sue Jones'] = sue
db.close()
