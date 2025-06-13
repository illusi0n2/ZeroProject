# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task():
    def __init__(self, description, term, status = False):
        self.description = description
        self.term = term
        self.status = status

    def complete_task(self):
        self.status = True

    def check_task_status(self):
        if not self.status:
            return True
        else:
            return False

    def get_task_info(self):
        return f"Задача: {self.description}\nСрок до: {self.term}\n"
        
        
def get_list_of_tasks(tasks):
    print('Список не выполненных задач:')
    for task in tasks:
        if task.check_task_status():
            print(task.get_task_info())


task_list = [
    Task("Сделать уборку", "2025-01-01"),
    Task("Сходить в магазин", "2025-01-02"),
    Task("Приготовить еду", "2025-01-03"),
    Task("Изучить Python", "2025-01-04")
]

task_list[1].complete_task()

get_list_of_tasks(task_list)
