import pytest
from utils.random_generator import generate_string
from utils.date_utils import get_end_of_the_month_formatted
from utils.task_utils import *


@pytest.fixture(scope="class", autouse=True)
def before_class_setup():
    # Turning off confirmation for Task before running tests in class so that it's possible to do clean up
    subprocess.run("echo yes | task config confirmation off", capture_output=True, text=True, shell=True)


@pytest.fixture(scope="function", autouse=True)
def after_function_teardown():
    yield
    # Deleting all the pending tasks after each test function run
    number_of_pending_tasks = int(get_pending_tasks_count())
    for task_number in range(1, number_of_pending_tasks + 1):
        delete_task(task_number)


def test_create_multiple_tasks():
    task_names = [f"t1{generate_string()}", f"t2{generate_string()}", f"t3{generate_string()}"]
    create_multiple_tasks(task_names)
    result = list_all_tasks()
    assert task_names[0] in result, f"Task with name '{task_names[0]}' was not found in {result}"
    assert task_names[1] in result, f"Task with name '{task_names[1]}' was not found in {result}"
    assert task_names[2] in result, f"Task with name '{task_names[2]}' was not found in {result}"


def test_create_task_due_end_of_month():
    due_date = get_end_of_the_month_formatted()
    task_name = generate_string()
    create_task(task_name, "due:eom")
    result = list_task(task_name)
    assert due_date in result, f"Date '{due_date}' was not found in {result}"


def test_add_priority():
    task_name = generate_string()
    create_task(task_name)
    result_create = list_task(task_name)
    assert task_name in result_create, f"Task {task_name} was not shown in {result_create}"

    modify_task(task_name, "priority:H")
    result_modify = list_task(task_name)
    assert task_name in result_modify, f"Task {task_name} was not shown in {result_modify}"
    assert " 6\n" in result_modify, f"Urgency = 6 was not shown in {result_modify} for task {task_name}"
    assert " H " in result_modify, f"Priority = H was not shown in {result_modify} for task {task_name}"


def test_mark_done():
    task_name = generate_string()
    create_task(task_name)
    result_create = list_task(task_name)
    assert task_name in result_create, f"Task {task_name} was not shown in {result_create}"

    complete_task(task_name)
    result_complete = list_task(task_name)
    assert task_name not in result_complete, f"Task {task_name} was still in {result_complete} after completion"
