import subprocess


def create_task(task_name, option=None):
    __run_task_command__(f"add {task_name} {option}")


def create_multiple_tasks(task_names, option=None):
    for task_name in task_names:
        create_task(task_name, option)


def modify_task(task_name, change):
    __run_task_command__(f"{task_name} modify {change}")


def complete_task(task_name):
    __run_task_command__(f"{task_name} done")


def list_all_tasks():
    return __run_task_command__("list")


def list_task(task_name):
    return __run_task_command__(f"list {task_name}")


def get_pending_tasks_count():
    return __run_task_command__("status:pending count")


def delete_task(task_id):
    return __run_task_command__(f"delete {task_id}")


def __run_task_command__(args):
    command = f"task {args}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip()
