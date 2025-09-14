students = {
    "Sumit": 97,
    "Gaurav": 96.5,
    "Rohit": 95,
    "prashant":89
}

name = input("Enter name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")

else:
    print("student not found")