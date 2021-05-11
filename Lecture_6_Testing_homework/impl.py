from collections import defaultdict

from Lecture_6_Testing_homework.err import DeadlineError
from datetime import datetime, timedelta


class Homework:
    def __init__(self, task_test: str, days_count: int):
        self.text = task_test
        self.created = datetime.now()
        self.deadline = timedelta(days=days_count)

    def is_active(self) -> bool:
        return self.created + self.deadline >= datetime.now()


class Person:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    def do_homework(self, homework: Homework, solution: str):
        if not homework.is_active():
            raise DeadlineError("You are late")

        return HomeworkResult(homework, solution, self)


class HomeworkResult:
    def __init__(self, homework: Homework, solution: str, author: Student):
        if not isinstance(homework, Homework):
            raise AttributeError('You gave a not Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.now()


class Teacher(Person):
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(task_test: str, days_count: int) -> Homework:
        return Homework(task_test, days_count)

    def check_homework(self, homework_result: HomeworkResult) -> bool:
        if len(homework_result.solution) > 5:
            self.homework_done[homework_result.homework].add(homework_result)
            return True
        else:
            return False

    @staticmethod
    def reset_results(task=None):
        if task is not None:
            Teacher.homework_done.get(task).clear()
        else:
            Teacher.homework_done.clear()
