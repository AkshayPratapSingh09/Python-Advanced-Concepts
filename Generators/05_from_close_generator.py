def local_items():
    yield "Paneer Butter Masala"
    yield "Dal Makhani"

def foreign_items():
    yield "Cheeze Pizza"
    yield "French Fries"

def full_menu():
    yield from local_items()
    yield from foreign_items()

for items in full_menu():
    print(items)   