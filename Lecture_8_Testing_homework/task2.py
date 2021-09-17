import sqlite3  # will be a list with data.


class TableRowData:
    def __init__(self, name, data):
        self.name = name
        self.data = data


class TableData:
    def __init__(self, db_name: str, table_name: str):
        self.cursor = sqlite3.connect(db_name).cursor().execute("SELECT * FROM '{0}';".format(table_name))

    def __len__(self):
        return len(self.__dict__) - 1

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self.cursor)

        self.__setattr__(row[0], TableRowData(row[0], row))
        return self.__getitem__(row[0])


presidents = TableData(db_name='example.sqlite', table_name='presidents')

for president in presidents:
    print(president.name)

assert len(presidents) == 3
assert presidents['Yeltsin'].data == ('Yeltsin', 999, 'Russia')
