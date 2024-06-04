import datetime as dt

# Импортируем из библитеки SqlAlchemy нужные функции и классы
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, CheckConstraint
from sqlalchemy import Integer, String, Boolean, DateTime, Numeric, SmallInteger

# Импортируем из подмодуля ORM функции и классы, предназначенные для
# высокоуровневой работы с базой данных посредством построения объектной модели ORM
# (ORM ~ object-relational model)
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


# Так просто надо сделать
class Basis(DeclarativeBase):
    pass


class Employee(Basis):
    __tablename__ = "employees"
    employee_id = Column(Integer(), primary_key=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(50))
    hire_date = Column(String(100), nullable=False)
    job_id = Column(String(50), nullable=False)
    salary = Column(Numeric(100))
    commission_pct = Column(Numeric(100))
    manager_id = Column(Integer(), ForeignKey('employees.employee_id'))
    department_id = Column(Integer())

    def __str__(self):
        return f"<{self.employee_id}> {self.first_name} {self.last_name} наш {self.job_id}"

    def __repr__(self):
        return f"email {self.email} наш {self.first_name} {self.last_name})"


class Department(Basis):
    __tablename__ = "departments"
    department_id = Column(Integer(), primary_key=True, autoincrement=True)
    department_name = Column(String(100), nullable=False)
    manager_id = Column(String())
    location_id = Column(Integer())


class JobHisory(Basis):
    __tablename__ = "job_history"
    employee_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    start_date = Column(String(100), nullable=False)
    end_date = Column(String(), nullable=False)
    job_id = Column(String(), ForeignKey('employees.job_id'))


engine = create_engine("sqlite:///My Database/staff.db?echo=True")
Basis.metadata.create_all(engine)
factory = sessionmaker(bind=engine)
