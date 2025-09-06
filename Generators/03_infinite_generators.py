def infinite_item():
    count = 1
    while True:
        yield f"Item {count}"
        count += 1


allItems = infinite_item()

#  It is infinite but we are limiting it for iterations
for _ in range(3):
    print(next(allItems))