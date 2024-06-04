# Добавим немношка пользователей

from schema import factory
from schema import Employee

u1 = Employee(employee_id='333', last_name="иванов", first_name="иван", email="ргашцру",
              phone_number="111111111",
              hire_date='1960-12-12', job_id='SA_REP', salary=10000000, manager_id=100, department_id=110)

u2 = Employee(employee_id='777', last_name="вася", first_name="васильев", email="gqyedgu__1",
              phone_number="111222333",
              hire_date='2000-01-01', job_id='ST_MAN', salary=500000, manager_id=300, department_id=110)

session = factory()
session.add_all([u1, u2])
session.commit()
