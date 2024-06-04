from schema import factory
from schema import Employee

session = factory()

employee = session.query(Employee).filter(Employee.manager_id == 149).all()

print(*(employee))
