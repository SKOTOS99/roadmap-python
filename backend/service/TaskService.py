

class TaskService:
    def __init__(self):
        self.task = []

    def add_task(self, addTask):
        return self.task.append(addTask)

    def get_task(self):
        return self.task

    def remove_task(self, id):
        removeTask = next((u for u in self.task if u['ids'] == int(id)), None)
        return self.task.remove(removeTask)

    def get_by_id(self, id):
        for u in self.task:
            print(f"{type(id)} Buscando id: {id}, comparando con: {u['ids']} ({type(u['ids'])})")
        return next((u for u in self.task if u['ids'] == int(id)), None)

    def update_task(self, id, taskUpdate):
        taskBack = next((u for u in self.task if u['ids'] == int(id)), None)
        if taskBack:
            taskBack['tittle'] = taskUpdate['tittle']
            taskBack['description'] = taskUpdate['description']
            taskBack['active'] = taskUpdate['active']
            return taskBack

        return None

