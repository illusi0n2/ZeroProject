class Task():
    def __init__(self, task_name, task_date):
        self._task_name = task_name
        self._task_date = task_date

    def set_name(self, name):
        self._task_name = name

    def set_date(self, date):
        self._task_date = date

    def get_name(self):
        return self._task_name

    def get_date(self):
        return self._task_date
