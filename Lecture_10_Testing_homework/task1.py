from Lecture_10_Testing_homework.models import *

db.connect()
db.create_tables([Homework, Teacher, Student, HomeworkResult])

teacher = Teacher.create(first_name='Daniil', last_name='Shadrin')
student = Student.create(first_name='Roman', last_name='Petrov')

teacher.save()
student.save()

print(Teacher.select().get().last_name)

migrater = SqliteMigrator(db)
migrate(migrater.add_column('teacher', "qq", CharField(null=True)))

Teacher.create(first_name='Daniil1', last_name='Shadrin1', qq="jkui")
migrate(migrater.rename_table('teacher', 'teacher1'))


cursor=db.execute_sql("select * from teacher1;")
for row in cursor.fetchall():
    print(row)


migrate(migrater.drop_column('teacher1', "qq"))

#should be fail, since teacher table does not exists
cursor=db.execute_sql("select * from teacher;")
for row in cursor.fetchall():
    print(row)

