def serve_menu():
    yield "Chai"
    yield "Coffee"
    yield "Snack"
    yield "Main Course"
    yield "Sweet Dish"

customer = serve_menu()

print(next(customer))
print(next(customer))
print(next(customer))
print(next(customer))
print(next(customer))
# print(next(customer)) --> Overflow for elements more than it has