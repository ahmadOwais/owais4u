"""
// create and implement a class to be a temporary storage, like a cache, for some simple type of data.

// using a key:value pair, where the value is some string

// this storage must support all CRUD operations, like have ways for a user to add data into it and read data from it

// it should also allow the user to search with a filter for optimum performance (provided by the user of this class)

// the example code should be exercised with simple unit tests for the CRUD operations

// Please also provide an example filter to filter out the most frequently used data in the cache.
"""
from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel
from employee_catche_store import EmployeeCatcheStore, Employee

app = FastAPI()

# Create an instance of EmployeeCacheStore
cache_store = EmployeeCatcheStore()
cache_store.add_employee(1, "Ram Verma", 30, 50000)
cache_store.add_employee(2, "Mohan Singh", 25, 60000)
cache_store.add_employee(3, "Shohan Dubay", 35, 75000)
cache_store.add_employee(3, "Ahmad Owais", 35, 75000)


class Employee(BaseModel):
    emp_id: int
    name: str
    age: int
    salary: float


@app.post("/employees/", response_model=Employee)
async def add_employee(employee: Employee):
    cache_store.add_employee(**employee.dict())
    return employee


@app.get("/employees/{emp_id}", response_model=Employee)
async def get_employee(emp_id: int):
    employee = cache_store.get_employee_by_id(emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return Employee(**employee.__dict__)


@app.get("/employees/", response_model=list[Employee])
async def get_employees(
    skip: int = Query(0, description="Number of items to skip"),
    limit: int = Query(10, description="Number of items to retrieve"),
):
    # cache_store.employee_list[skip: skip + limit]
    employees = EmployeeCatcheStore().display_employees
    print('EMP :'+employees)
    return [Employee(**employee.__dict__) for employee in employees]


@app.get("/filter_employees/", response_model=list[Employee])
async def filter_employees(
    top_n: int = Query(
        3, description="Number of most frequently accessed employees to retrieve")
):
    most_frequently_accessed = cache_store.filter_most_frequently_accessed(
        top_n)
    return [Employee(**employee.__dict__) for employee in most_frequently_accessed]

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
