from dotenv import load_dotenv
from app.models import Menu, MenuItem, MenuItemType, Table



load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)


    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    table_1 = Table(number=1, capacity=4)
    table_2 = Table(number=2, capacity=4)
    table_3 = Table(number=3, capacity=2)
    table_4 = Table(number=4, capacity=4)
    table_5 = Table(number=5, capacity=2)
    table_6 = Table(number=6, capacity=4)
    table_7 = Table(number=7, capacity=6)
    table_8 = Table(number=8, capacity=8)
    table_9 = Table(number=9, capacity=10)
    table_10 = Table(number=10, capacity=3)

    db.session.add(table_1)
    db.session.add(table_2)
    db.session.add(table_3)
    db.session.add(table_4)
    db.session.add(table_5)
    db.session.add(table_6)
    db.session.add(table_7)
    db.session.add(table_8)
    db.session.add(table_9)
    db.session.add(table_10)




    db.session.add(beverages)
    db.session.add(entrees)
    db.session.add(sides)
    db.session.add(dinner)
    db.session.add(fries)
    db.session.add(drp)
    db.session.add(jambalaya)

    db.session.commit()
