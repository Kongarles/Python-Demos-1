file = open(r"C:\Users\Kayra\Masaüstü\Python_Demos\Demos\project 3\employee_revenue.txt", "r")
data = file.read()

#print(data)

lines = data.splitlines()
#print(lines)

string = lines[0]
string = string.strip(" ")
string = string.lower()
string = string.capitalize()

split_string = string.split(" ")

name = split_string[0]

call_number = split_string[2]

for i in split_string:
    if "$" in i:
        average_deal_size = i.split("$")[0]

dollars_index = split_string.index("dollars")
revenue_index = dollars_index - 1
revenue = split_string[revenue_index]


# print("Name:", name)
# print("Number of calls:", call_number)
# print("Average deal siz:", average_deal_size)
# print("Revenue:", revenue)

average_deal_size = int(average_deal_size)
call_number = int(call_number)
revenue = int(revenue)

# print("Name:", type(name))
# print("Number of calls:", type(call_number))
# print("Average deal siz:", type(average_deal_size))
# print("Revenue:", type(revenue))

names = []
call_numbers = []
average_deal_sizes = []
revenues = []

for employee in lines:
    employee = employee.strip(" ")
    employee = employee.lower()
    employee = employee. capitalize()

    split_employee = employee.split(" ")

    name = split_employee[0]
    call_number = split_employee[2]

    for i in split_employee:
        if "$" in i:
            average_deal_size = i
    average_deal_size = average_deal_size.split("$")[0]

    dollars_index = split_employee.index("dollars")
    revenue_index = dollars_index - 1
    revenue = split_employee[revenue_index]

    average_deal_size = int(average_deal_size)
    call_numbers.append(call_number)
    average_deal_sizes.append(average_deal_size)
    revenues.append(revenue)

print("Names:", names)
print("Number of calls:", call_numbers)
print("Average deal sizes:", average_deal_sizes)
print("Revenues:", revenues)
