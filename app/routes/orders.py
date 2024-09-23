from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user
from ..models import (
    db,
    Order,
    OrderDetail,
    Table,
    Employee,
    MenuItem,
    MenuItemType,
    Menu,
)
from ..forms import TableAssignmentForm, MenuItemAssignmentForm

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    # empty_tables = (
    #     Table.query.join(Order).filter(Order.finished == False).order_by(Table.id)
    # )
    free_employees = (
        Employee.query.join(Order)
        .filter(Order.finished is not False)
        .order_by(Employee.id)
        .all()
    )
    # Get the tables and open orders
    tables = Table.query.order_by(Table.number).all()
    open_orders = Order.query.filter(Order.finished == False)
    # print(open_orders, '----------------\n\n\t--------', open_orders.all())

    # Get the table ids for the open orders
    busy_table_ids = [order.table_id for order in open_orders]

    # Filter the list of tables for only the open tables
    open_tables = [table for table in tables if table.id not in busy_table_ids]

    # Finally, convert those tables to tuples for the select field and set the
    # choices property to it
    form = TableAssignmentForm()
    form.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]
    form.servers.choices = [
        (employee.id, f"Server {employee.employee_number}")
        for employee in free_employees
    ]

    order = (
        Order.query.join(Employee)
        .filter(Order.employee_id == current_user.id)
        .filter(Order.finished is not False)
    )
    # print(order, "kkkkkkkkkkk", current_user.id, order.all())

    menu_items = MenuItem.query.join(MenuItemType).order_by(
        MenuItemType.name, MenuItem.name
    )
    print(menu_items.all())

    menu_form = MenuItemAssignmentForm()
    menu_form.menu_item_ids.choices = [(item.id, "") for item in MenuItem.query.all()]
    # print(menu_items, "----------------", menu_items.all())

    return render_template(
        "app.html",
        form=form,
        menu_form=menu_form,
        open_orders=open_orders,
        open_tables=open_tables,
    )


@bp.route("/assign_table/<int:table_id>/<int:employee_id>/", methods=["POST"])
@login_required
def assign_table(table_id, employee_id):
    order = Order(employee_id=employee_id, table_id=table_id, finished=False)

    db.session.add(order)
    db.session.commit()

    return redirect(url_for(".index"))


@bp.route("/close_table/<int:order_id>/", methods=["POST"])
@login_required
def close_table(order_id):
    order = Order.query.get(order_id)
    order.finished = True

    db.session.add(order)
    db.session.commit()

    return redirect(url_for(".index"))


@bp.route("/add_to_order/<order_id>/")
@login_required
def add_to_order(order_id, **kwargs):
    pass
