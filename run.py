import sqlite3
from hoa import HOA

connection = sqlite3.connect(':memory:')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE homeowners (
    first text,
    last text,
    address integer
)""")

# cursor.execute("""UPDATE homeowners
#     SET address = 251
#     WHERE first = 'RUBY'
# """)

# cursor.execute("INSERT INTO homeowners VALUES ('RUBY', 'DO', 251)") # auto commit

# owner1 = HOA('MAI', 'NGUYEN', 247)
# owner2 = HOA('CORVETTE', 'NGUYEN', 245)
#
# cursor.execute("INSERT INTO homeowners VALUES (?, ?, ?)", (owner1.first, owner1.last, owner1.address))
#
# cursor.execute("INSERT INTO homeowners VALUES (:first, :last, :address)", {'first': owner2.first, 'last': owner2.last, 'address': owner2.address})
#
# # cursor.execute("SELECT * FROM homeowners")
# # cursor.execute("SELECT * FROM homeowners WHERE first='MAI'")
# cursor.execute("SELECT * FROM homeowners WHERE first=?", ('MAI',))
# print(cursor.fetchone())
#
# cursor.execute("SELECT * FROM homeowners WHERE first=:first", {'first': 'CORVETTE'})
#
# # print(cursor.fetchmany(2))  # fetchall, fetchmany return a list, fetches return None if nothing found
# print(cursor.fetchall())


# connection.commit()

def insert_owner(owner):
    with connection:
        cursor.execute("INSERT INTO homeowners VALUES (:first, :last, :address)", {
                       'first': owner.first, 'last': owner.last, 'address': owner.address})


def get_owner_by_lastname(lastname):
    cursor.execute("SELECT * FROM homeowners WHERE last=:last", {'last': lastname})
    return cursor.fetchall()


def update_owner(first, last, address):
    with connection:
        cursor.execute("""UPDATE homeowners SET first = :first, last =:last WHERE address = :address""",
                       {'first': first, 'last': last, 'address': address})


def remove_owner(owner):
    with connection:
        cursor.execute("DELETE from homeowners WHERE first= :first AND last= :last",
                       {'first': owner.first, 'last': owner.last})


owner1 = HOA('Nick', 'Nguyen', 249)
owner2 = HOA('Mai', 'Nguyen', 247)
owner3 = HOA('SASA', 'Nguyen', 255)

insert_owner(owner1)
insert_owner(owner2)
insert_owner(owner3)
owners = get_owner_by_lastname('Nguyen')
print(owners)

update_owner('Xuan', 'Nguyen', 247)
owners = get_owner_by_lastname('Nguyen')
print(owners)

remove_owner(owner3)
owners = get_owner_by_lastname('Nguyen')
print(owners)

connection.close()
