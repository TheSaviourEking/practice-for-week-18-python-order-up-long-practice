from dotenv import load_dotenv

load_dotenv()

from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table

with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")

    beverages = MenuItemType(name="Beverages")

    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    # Seed tables
    table1 = Table(number=1, capacity=12)
    table2 = Table(number=2, capacity=3)
    table3 = Table(number=3, capacity=7)
    table4 = Table(number=4, capacity=8)
    table5 = Table(number=5, capacity=2)
    table6 = Table(number=6, capacity=12)
    table7 = Table(number=7, capacity=7)
    table8 = Table(number=8, capacity=10)
    table9 = Table(number=9, capacity=7)
    table10 = Table(number=10, capacity=4)

    db.session.add(employee)
    db.session.add(beverages)
    db.session.add(entrees)
    db.session.add(sides)
    db.session.add(dinner)
    db.session.add(fries)
    db.session.add(drp)
    db.session.add(jambalaya)

    db.session.add_all(
        [
            table1,
            table2,
            table3,
            table4,
            table5,
            table6,
            table7,
            table8,
            table9,
            table10,
        ]
    )

    db.session.commit()
