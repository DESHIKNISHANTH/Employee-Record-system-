import json
import os

FILE = "employees.json"

# -------------------------
# Load & Save Functions
# -------------------------
def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# -------------------------
# CRUD Operations
# -------------------------
def add_employee():
    data = load_data()
    emp = {}

    emp["id"] = input("Enter Employee ID: ")
    emp["name"] = input("Enter Employee Name: ")
    emp["age"] = input("Enter Age: ")
    emp["role"] = input("Enter Role: ")
    emp["salary"] = input("Enter Salary: ")

    data.append(emp)
    save_data(data)
    print("\n✔ Employee added successfully!\n")

def view_employees():
    data = load_data()
    if not data:
        print("\nNo employee records found.\n")
        return
    print("\n----- All Employees -----")
    for emp in data:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Age: {emp['age']} | Role: {emp['role']} | Salary: {emp['salary']}")
    print("-------------------------\n")

def search_employee():
    data = load_data()
    emp_id = input("Enter Employee ID to search: ")
    for emp in data:
        if emp["id"] == emp_id:
            print(f"\nFound: {emp}\n")
            return
    print("\nEmployee not found.\n")

def update_employee():
    data = load_data()
    emp_id = input("Enter Employee ID to update: ")
    for emp in data:
        if emp["id"] == emp_id:
            print("\nEnter new details (leave blank to keep old value):")
            name = input("New Name: ")
            age = input("New Age: ")
            role = input("New Role: ")
            salary = input("New Salary: ")

            if name: emp["name"] = name
            if age: emp["age"] = age
            if role: emp["role"] = role
            if salary: emp["salary"] = salary

            save_data(data)
            print("\n✔ Employee updated successfully!\n")
            return

    print("\nEmployee not found.\n")

def delete_employee():
    data = load_data()
    emp_id = input("Enter Employee ID to delete: ")
    new_data = [emp for emp in data if emp["id"] != emp_id]

    if len(new_data) == len(data):
        print("\nEmployee not found.\n")
    else:
        save_data(new_data)
        print("\n✔ Employee deleted successfully!\n")

# -------------------------
# Main Menu
# -------------------------
def main():
    while True:
        print("""
===== Employee Record System =====
1. Add Employee
2. View All Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
