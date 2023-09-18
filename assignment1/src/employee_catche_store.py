# import Employee


class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary


class EmployeeCatcheStore:
    def __init__(self):
        self.employee_list = []
        self.access_count = {}

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employee_list.append(employee)
        self.access_count[emp_id] = 0

    def get_employee_by_id(self, emp_id):
        self.access_count[emp_id] += 1
        for employee in self.employee_list:
            if employee.emp_id == emp_id:
                return employee
        return "Employ Not Found"

    def remove_employee_by_id(self, emp_id):
        employee = self.get_employee_by_id(emp_id)
        if employee:
            self.employee_list.remove(employee)
            del self.access_count[emp_id]
            return "Employ added Successfully"
        return "Not Added"

    def display_employees(self):
        for employee in self.employee_list:
            print(
                f"ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
        return employee

    def filter_most_frequently_accessed(self, top_n=3):
        sorted_access_count = sorted(
            self.access_count.items(), key=lambda x: x[1], reverse=True)
        top_n_ids = [emp_id for emp_id, _ in sorted_access_count[:top_n]]
        top_n_employees = [
            employee for employee in self.employee_list if employee.emp_id in top_n_ids]
        return top_n_employees


# Sample data
catchStore = EmployeeCatcheStore()
catchStore.add_employee(1, "Ram Verma", 30, 50000)
catchStore.add_employee(2, "Mohan Singh", 25, 60000)
catchStore.add_employee(3, "Shohan Dubay", 35, 75000)
catchStore.add_employee(3, "Ahmad Owais", 35, 75000)

# Simulate accessing employees multiple times
catchStore.get_employee_by_id(1)
catchStore.get_employee_by_id(2)
catchStore.get_employee_by_id(1)
catchStore.get_employee_by_id(3)

# Example filter function to get employees older than 28


# Display all employees
print("All Employees:")
catchStore.display_employees()
# Get an employee by ID
employee = catchStore.get_employee_by_id(2)
if employee:
    print(f"Employee ID 2: {employee.name}")

# Remove an employee by ID
if catchStore.remove_employee_by_id(1):
    print("Employee with ID 1 removed")

# Display employees after removal
print("Employees after removal:")
catchStore.display_employees()

# Filter and display the most frequently accessed employees (top 2 in this case)
most_frequently_accessed_employees = catchStore.filter_most_frequently_accessed(
    top_n=2)
print("Most frequently accessed employees:")
catchStore.display_employees()


# def filter_older_than_28(catchStore):
#    return catchStore.employee.age > 28

# Search employees with the filter function
# filtered_employees = catchStore.search_with_filter(filter_older_than_28)
# print("Employees older than 28:")
# catchStore.display_employees()
