def serve_menu():
    yield "Chai"
    yield "Coffee"
    yield "Snack"
    yield "Main Course"
    yield "Sweet Dish"

customer = serve_menu()

# ❌ It is more likely to overflow
for i in range(6):
    print(next(customer))

# ✅ Correct Way 
for item in customer:
    print(item)