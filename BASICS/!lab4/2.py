#Добавим новое отделение
from schema import factory
from schema import Department

u1 = Department(department_id=9999, department_name="Physical Education", manager_id=100, location_id=2500)


session = factory()
session.add(u1)
session.commit()
