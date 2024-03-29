import mysql.connector
import pytest


@pytest.mark.usefixtures('setUp')
class TestMySql:
    def test_mysql_connection(self):
        print(self.conn.is_connected())

    def test_retrive_all_data(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM checking')
        row = self.cursor.fetchall()
        print(row)

    def test_update_name(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('UPDATE checking SET test3 = "bye" WHERE test1 = 1' )
        self.conn.commit()
        affected_rows = self.cursor.rowcount
        print(f"Number of affected rows: {affected_rows}")


    def test_retrive_finaldata(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM checking')
        row = self.cursor.fetchall()
        print(row)

    def test_add_new_row(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('INSERT INTO checking VALUES (2, "test")')
        self.conn.commit()

    def test_delete_new_row(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('DELETE FROM checking WHERE test1 = 2')
        self.conn.commit()