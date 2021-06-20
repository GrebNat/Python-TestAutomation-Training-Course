from playhouse.migrate import *

db = SqliteDatabase('hw.db')

class Homework(Model):
    text = TextField()
    created = DateField()
    deadline = DecimalField()

    class Meta:
        database = db


class Person(Model):
    last_name = CharField()
    first_name = CharField()

    class Meta:
        database = db


class Teacher(Person):
    pass


class Student(Person):
    pass


class HomeworkResult(Model):
    homework = ForeignKeyField(Homework)
    solution = CharField()
    author = ForeignKeyField(Student)
    created = DateField()

    class Meta:
        database = db
