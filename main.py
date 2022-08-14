
from fastapi import FastAPI, HTTPException
from typing import List
from mangum import Mangum


from pydantic import BaseModel

 
class Employee(BaseModel):
    Emp_ID: int
    F_Name: str
    L_Name: str
    Salary: int


app = FastAPI()
handler = Mangum(app)


db: List[Employee] = [
    Employee(Emp_ID=1, F_Name='Ahmed', L_Name='Kotb', Salary=4444)
    , Employee(Emp_ID=2, F_Name='Heba', L_Name='Gaber', Salary=5000)

]


@app.get("/")
async def gethelloworld():
    return 'Hello to Lambda'


@app.get("/Employee")
async def Get_All_Employees():
    return db


@app.post("/Employee")
async def Create_New_Employee(emp: Employee):
    db.append(emp)

    return "New Employee Added successfully"


@app.delete("/Employee/{Emp_ID}")
async def Delete_Employee(Emp_ID: int):
    for emp in db:
        if Emp_ID == emp.Emp_ID:
            db.remove(emp)
            return "Employee deleted successfully"

    raise HTTPException(status_code=404, detail=f"Employee with ID {Emp_ID}  does not exist")


@app.put("/Employee/{Emp_ID}")
async def Update_Employee(Emp_ID: int, emp: Employee):
    for exist in db:
        if Emp_ID == exist.Emp_ID:
            if emp.F_Name is not None:
                exist.F_Name = emp.F_Name
            if emp.L_Name is not None:
                exist.L_Name = emp.L_Name
            if emp.Salary is not None:
                exist.Salary = emp.Salary

            return "Employee updated successfully"

    raise HTTPException(status_code=404, detail=f"Employee with ID {Emp_ID}  does not exist")