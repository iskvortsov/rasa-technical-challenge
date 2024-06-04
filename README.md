# Rasa Technical Challenge by Ivan Skvortsov

Initial task can be found [here](TASK.md).

## Project structure

The structure is as follows:

```
rasa-technical-challenge
    |
    |__ .github/workflows   <- Git Actions job .yaml file
    |
    |__ tests               <- Test folder with both API and CLI tests files
    |
    |__ utils               <- Utility classes used in both of the test files
```

## How to run locally 

### Requirements:

To run the project locally, you need to install: 
1) python version 3.8 
2) pytest
3) pytest requests
4) [taskwarrior](https://taskwarrior.org/download/#distributions)

_NOTE: If unsure, refer to [run_all_tests.yaml](/.github/workflows/run_all_tests.yaml)_

### Run tests:

#### CLI tests

Run `pytest test/test_cli.py` in repo root folder.

#### API tests

Run `pytest tests/test_api.py` in repo root folder.

## Part 1: CLI tests

First of all, I've decided to turn confirmations off for Task commands. This enabled me to do a cleanup after each test.

### Scenarios 

I've decided to use scenarios that I would personally use most of the time:
1) Create multiple tasks
2) Add priority to task
3) Create a task with due date
4) Mark task done 

### Other scenarios

The tool Task has a lot of features that could be covered as well: 
1) Tags
2) Project
3) Filtering (with lots of different parameters)
4) Due dates modification, expiration etc.
5) Searching
6) Task Server 

Honestly, there's just too much stuff in it :D The full doc is [here](https://taskwarrior.org/docs/)

### Future considerations

I could use pytest parametrized fixtures for other scenarios (like filtering or searching). 

Also, probably the output of `task list` could be parsed into an object to get more accurate assertions that don't depend on formatting.

Create task could be moved to before function fixture for some tests.

(just a few things from the top of my mind really)

## Part 2: API tests

I've decided to automate CRUD operations for `/products` endpoint + make a parametrized login user test.

### Other scenarios

The API is not that extensive so here's the list of other considerations:
1) CRUD operations for `cart` endpoint
2) CRUD operations for `user` endpoint
3) And GET sorted results for all three endpoints

[Here's full API documentation](https://fakestoreapi.com/docs#c-single)

### Future considerations

Create data objects for Product, Cart, User and use them instead of plain `response.json()`

Of course, more fixtures and parametrization can be used.

_Also `create product` request should have status code 201 instead of 200._


## Part 3: CI/CD config

Welp, there is just one job to run all the tests - [run_all_tests.yaml](/.github/workflows/run_all_tests.yaml).

I'm using GitHub Actions because it's ease of use and integration with GitHub.

### Future considerations

If it was a real working repository, I would add trigger on pull request. 

Scheduled run (using cron) also could work in some projects.

Also, integration with Slack is easy to do if it's needed.

Another thing is adding some test reports as artifacts.

## Feedback and a few thoughts

I've got to say that this challenge is one of the best I've seen so far throughout my career. Not only it is neatly organized, but it also gives a chance for potential employee to showcase his/her skills in solving variety of tasks. It didn't take a lot of my time (~4 hours + some time to write this README.md) and I enjoyed every minute of it. 

Also, if development workflow in Rasa is anything like this task, I'm even more excited about joining the team!

Last but no least, I have to say that even though I'm passionate about Python (I consider it one of my favourite programming languages) it's been a long time since I've used it in my work. So please don't judge too hard my usage of best practices. I'm a fast learner and motivated, too. So if I join it will take me a couple of weeks to get up to speed with latest best practices used in Python. I have a lot of experience with other languages, best practices and development principles though, and I'd love to start using Python in my daily workflow.

I wish a good day to anyone who reads that :)

_Cheers,
Ivan Skvortsov_
 