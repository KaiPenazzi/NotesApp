import sqlite3
import unittest

from app.Task import Task

class DB:
    _instance = None
    def __init__(self):
        raise RuntimeError('Call instance() instead')
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.con = sqlite3.connect('tasks.db')
            cls.cur = cls.con.cursor()
            cls.create_table(cls)

        return cls._instance

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            date DATETIME NOT NULL
            )
            ''')
        self.con.commit()

    def new_task(self, task):
        self.cur.execute('''INSERT INTO tasks (text, date) VALUES (?, ?)''',
                         (task.text, str(task.date),))
        self.con.commit()
        return self.cur.lastrowid

    def get_tasks(self):
        self.cur.execute('SELECT * FROM tasks ORDER BY date ASC')
        ret = self.cur.fetchall()

        tasks = []
        for item in ret:
            tasks.append(Task(item[0], item[1], item[2]))

        return tasks

    def get_task(self, id):
        res = self.cur.execute('SELECT * FROM tasks WHERE id=?', (id,))
        task = res.fetchone()
        try:
            return Task(task[0], task[1], task[2])
        except:
            return None

    def rm_task(self, id):
        self.cur.execute('DELETE FROM tasks WHERE id=?', (id,))
        self.con.commit()

    def __del__(self):
        self.con.close()

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DB.instance()

    def tearDown(self):
        self.db = None

    def test_create_task(self):
        id = self.db.new_task(Task(text='test task'))
        self.assertIsNotNone(id, 'id should not be NONE')
        
        task = self.db.get_task(id)
        self.assertEqual(task.text, 'test task')

    def test_delete_task(self):
        res = self.db.get_tasks()

        for task in res:
            self.db.rm_task(task.id)

            task = self.db.get_task(task.id)
            self.assertIsNone(task)

if __name__ == '__main__':
    unittest.main()

