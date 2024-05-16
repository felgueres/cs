import unittest
from MemdbImpl import MemDBImpl

class TestMemDB(unittest.TestCase):

    def test_create_table(self):
        db = MemDBImpl()
        cols = {'name': str, 'phone': int, 'address': str}
        table_name = 'users'
        is_created = db.create_table(table_name=table_name, schema=cols)
        self.assertGreater(len(db.tables),0)
        self.assertIs(is_created, True)
        self.assertIn(table_name, db.tables)
    
    def test_insert(self):
        db = MemDBImpl()
        table_name = 'users'
        schema = {'name': str, 'phone': int, 'address': str}
        row = {'name': 'pablo', 'phone': 123, 'address': '123'}
        db.create_table(table_name, schema)
        db.insert(table_name=table_name, row=row)
        self.assertGreater(len(db.tables['users']['rows']),0)

    def test_delete(self):
        db = MemDBImpl()
        table_name = 'users'
        schema = {'name': str, 'phone': int, 'address': str}
        row = {'name': 'pablo', 'phone': 123, 'address': '123'}
        db.create_table(table_name, schema)
        db.insert(table_name=table_name, row=row)
        self.assertGreater(len(db.tables['users']['rows']),0)
        db.delete(table_name, condition={'name': 'pablo', 'phone':123})
        self.assertEqual(len(db.tables['users']['rows']),0)

    def test_query(self):
        db = MemDBImpl()
        table_name = 'users'
        schema = {'name': str, 'phone': int, 'address': str}
        row1 = {'name': 'pablo', 'phone': 123, 'address': '123'}
        row2 = {'name': 'pablo', 'phone': 456, 'address': '456'}
        db.create_table(table_name, schema)
        db.insert(table_name=table_name, row=row1)
        db.insert(table_name=table_name, row=row2)
        self.assertEqual(len(db.query(table_name, {'name':'pablo'})), 2)

    def test_update(self):
        db = MemDBImpl()
        table_name = 'users'
        schema = {'name': str, 'phone': int, 'address': str}
        row1 = {'name': 'pablo', 'phone': 123, 'address': '123'}
        row2 = {'name': 'pablo', 'phone': 456, 'address': '456'}
        condition = {'name': 'pablo'}
        db.create_table(table_name, schema)
        db.insert(table_name=table_name, row=row1)
        db.insert(table_name=table_name, row=row2)
        db.update(table_name, condition, {'name': 'john'})
        self.assertEqual(len(db.query(table_name, {'name': 'john'})), 2)

if __name__ == '__main__':
    unittest.main()