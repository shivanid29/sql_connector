import pytest
import mysql.connector


@pytest.fixture(scope="class")
def setUp(request):
    global conn
    conn = mysql.connector.connect(host='localhost', database= 'new_db', user='root', password='password')
    request.cls.conn = conn

    yield

    print("session closed", conn.close())
