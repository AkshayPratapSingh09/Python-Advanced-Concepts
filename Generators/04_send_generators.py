def customer_bills():
    print("Welcome to Our Restaurent!! What are you having??")
    #  Similarly working like destructing in JS
    # Can be done for multiple elements
    order = yield
    while True:
        print(f"Thanks for having {order}")
        #  Looks for new values for next iteration
        order = yield #--> in this line
        # Without it, its an infinite loop

consumer1 = customer_bills()
next(consumer1)
# uptil this code it is stoping at the first print in the func

consumer1.send("Chai")
consumer1.send("Coffee")
consumer1.send("Snack")
consumer1.send("Main Course")