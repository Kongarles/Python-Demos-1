salesperson_revenue = {
    "Ben": 0,
    "Omer": 0,
    "Karen": 0,
    "Celine": 0,
    "Sue": 0,
    "Bora": 0,
    "Rose": 0,
    "Ellen": 0
}

def enter_revenue(name, revenue):
    global salesperson_revenue
    salesperson_revenue[name] += revenue

while True:
    name = input("Employee name: ")
    if name == "quit":
        break
    revenue = int(input("Enter revenue: "))
    enter_revenue(name, revenue)
    print(f"{name}'s revenue is {salesperson_revenue[name]}")