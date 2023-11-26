from pubsub import pub

planned_task_list   = []
current_task_list  = []
completed_task_list = []


def add_planned_task(data):
    planned_task_list.append(data)