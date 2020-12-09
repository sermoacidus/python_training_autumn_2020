import sqlite3
from itertools import zip_longest
from typing import Iterator


class TableData:
    """
    Wrapper class for database table, that when initialized with database name and table
    acts as collection object (implements Collection protocol)
    """

    class TableDataDecorators:
        @staticmethod
        def db_conn(func):
            def wrapper(*args, **kwargs):
                conn = sqlite3.connect(args[0].database_name)
                cur = conn.cursor()
                result = func(*args, **kwargs, bd_connect=cur)
                conn.commit()
                conn.close()
                return result

            return wrapper

    @staticmethod
    def check_connection(bd_connection):
        if not bd_connection:
            raise ConnectionError("No database connection")

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def __repr__(self):
        return f"{self.__class__.__name__}(database_name={self.database_name}, table_name={self.table_name})"

    @TableDataDecorators.db_conn
    def __len__(self, bd_connect: sqlite3.Cursor = None) -> int:
        self.check_connection(bd_connect)
        premade_selection = f"select * from {self.table_name}"
        return len([_ for _ in bd_connect.execute(premade_selection)])

    @TableDataDecorators.db_conn
    def __getitem__(self, item, bd_connect: sqlite3.Cursor = None):
        self.check_connection(bd_connect)
        premade_selection = f"select * from {self.table_name} where name=:name"
        return bd_connect.execute(premade_selection, (item,)).fetchall()[0]

    @TableDataDecorators.db_conn
    def __contains__(self, item, bd_connect: sqlite3.Cursor = None):
        self.check_connection(bd_connect)
        premade_selection = f"select * from {self.table_name} where name=:name"
        return len(bd_connect.execute(premade_selection, (item,)).fetchall()) > 0

    def __iter__(self):
        return TableDataIter(self.database_name, self.table_name)


class TableDataIter:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.iter_limiter = 0

    def __iter__(self):
        return self

    @TableData.TableDataDecorators.db_conn
    def __next__(self, bd_connect: sqlite3.Cursor = None) -> Iterator:
        iter_collection = []
        premade_selection = f"select * from {self.table_name}"
        select_result = bd_connect.execute(premade_selection)
        column_names = [description[0] for description in select_result.description]
        for element in select_result:
            iter_collection.append(dict(zip_longest(column_names, element)))
        if self.iter_limiter < len(iter_collection):
            self.iter_limiter += 1
            return iter_collection[self.iter_limiter - 1]
        else:
            raise StopIteration
