import pytest
from employee_catche_store import EmployeeCatcheStore


@pytest.fixture
def catch_store():
    employees = EmployeeCatcheStore()
    employees.add_employee(1, "Ram Verma", 30, 50000)
    employees.add_employee(2, "Mohan Singh", 25, 60000)
    employees.add_employee(3, "Shohan Dubay", 35, 75000)
    employees.add_employee(3, "Ahmad Owais", 35, 75000)
    return employees


def test_get_employee_by_id(catch_store: EmployeeCatcheStore):
    employee = catch_store.get_employee_by_id(2)
    assert employee is not None
    assert employee.name == "Ram Verma"


def test_get_employee_by_nonexistent_id(catch_store: EmployeeCatcheStore):
    employee = catch_store.get_employee_by_id(4)
    assert employee is None


def test_remove_employee_by_id(catch_store: EmployeeCatcheStore):
    assert catch_store.remove_employee_by_id(1) is True
    assert len(catch_store.employee_list) == 2


def test_remove_employee_by_nonexistent_id(catch_store: EmployeeCatcheStore):
    assert catch_store.remove_employee_by_id(4) is False


def test_filter_most_frequently_accessed(catch_store: EmployeeCatcheStore):
    # Access employees multiple times
    catch_store.get_employee_by_id(1)
    catch_store.get_employee_by_id(2)
    catch_store.get_employee_by_id(1)

    # Filter the most frequently accessed employees (top 2 in this case) filtered_employees = catchStore.search_with_filter(filter_older_than_29)
    most_frequently_accessed_employees = catch_store.filter_most_frequently_accessed(
        top_n=2)
    assert len(most_frequently_accessed_employees) == 2
    assert most_frequently_accessed_employees[0].emp_id == 1
    assert most_frequently_accessed_employees[1].emp_id == 2


if __name__ == "__main__":
    pytest.main()
