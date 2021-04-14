from datetime import datetime, timedelta


class Homework:
    def __init__(self, task_test: str, days_count: int):
        self.text = task_test
        self.created = datetime.now()
        self.deadline = timedelta(days=days_count)

    def is_active(self) -> bool:
        return self.created + self.deadline <= datetime.now()


class Teacher:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(task_test: str, days_count: int) -> Homework:
        return Homework(task_test, days_count)


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework):
        if homework.is_active():
            print("You are late")
            return None

        return homework
