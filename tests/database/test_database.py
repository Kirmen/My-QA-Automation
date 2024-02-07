import sqlite3

import pytest

from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_get_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)


@pytest.mark.database
def test_get_user_by_name():
    db = Database()
    user = db.get_user_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'
    print(user)


@pytest.mark.database
def test_set_quantity():
    db = Database()
    db.update_quantity(1, 25)
    qnt_water = db.select_quantity(1)

    assert qnt_water[0][0] == 25


@pytest.mark.database
def test_insert_product():
    db = Database()
    db.insert_product(4, 'superwater', 'healthy', 22)
    qnt_water = db.select_quantity(4)

    assert qnt_water[0][0] == 22


@pytest.mark.database
def test_delete_product():
    db = Database()
    db.insert_product(99, 'superwater', 'healthy', 999)
    db.delete_product(99)
    qty = db.select_quantity(99)

    assert len(qty) == 0


@pytest.mark.database
def test_get_detail_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print('orders: ', orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == "солодка вода"


@pytest.mark.database
def test_insert_invalid_data_type():
    db = Database()

    with pytest.raises(sqlite3.DatabaseError):
        db.insert_product(1001, 'Invalid Product', 12345, 'abc')


@pytest.mark.database
def test_insert_product_with_float_qty():
    db = Database()
    db.insert_product(5, 'superwater', 'healthy', 23.0)
    qnt_water = db.select_quantity(5)

    assert qnt_water[0][0] == 23


@pytest.mark.database
def test_insert_product_with_float_name():
    db = Database()
    db.insert_product(5, 5.25, 'healthy', 23)
    product = db.get_product_name_by_id(5)

    assert product[0][0] == '5.25'
    assert product[0][0] != 5.25


@pytest.mark.database
def test_insert_product_with_minus_id():
    db = Database()
    db.insert_product(-5, 'some name', 'healthy', 23)
    product = db.get_product_name_by_id(-5)

    assert product[0][0] == 'some name'


@pytest.mark.database
def test_update_product_with_wrong_id():
    db = Database()
    db.update_quantity(99, 999)
    qty = db.select_quantity(99)

    assert len(qty) == 0
