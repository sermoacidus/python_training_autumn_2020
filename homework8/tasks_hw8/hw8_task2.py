import sqlite3


class TableData:
    def __init__(self, database_name=None, table_name=None):
        self.database_name = database_name
        self.table_name = table_name
        self.iter_limiter = 0

    def _conn_deco(self):
        def wrapper(f):
            conn = sqlite3.connect(self.database_name)
            cur = conn.cursor()
            result = f(cur)
            conn.close()
            return result

        return wrapper

    def __repr__(self):
        return f"{self.__class__.__name__}(database_name={self.database_name}, table_name={self.table_name})"

    @_conn_deco
    def __len__(self, *args):
        print(args)
        premade_selection = f"select * from {self.table_name}"
        return len([_ for _ in cur.execute(premade_selection)])

    def __getitem__(self, item):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()
        premade_selection = f"select * from {self.table_name} where name=?"
        return cur.execute(premade_selection, (item,)).fetchall()

    def __contains__(self, item):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()
        premade_selection = f"select * from {self.table_name} where name=?"
        return len(cur.execute(premade_selection, (item,)).fetchall()) > 0

    def __iter__(self):
        self.limit = 0
        return self

    def __next__(self):
        conn = sqlite3.connect(self.database_name)
        premade_selection = f"select * from {self.table_name}"
        cur = conn.execute(premade_selection)
        names = [description[0] for description in cur.description]
        collect = []
        fetched_inf = cur.fetchall()
        for i in fetched_inf:
            collect.append(dict(zip(names, i)))
        if self.iter_limiter < len(names):
            self.iter_limiter += 1
            return collect[self.iter_limiter - 1]
        else:
            raise StopIteration


if __name__ == "__main__":

    presidents = TableData(database_name="example.sqlite", table_name="presidents")
    # print(presidents)
    print(len(presidents))
    # print(presidents['Yeltsin'])
    # print('Yeltsin' in presidents)
    # for president in presidents:
    #    print('+',president['name'])
