---
title: Unit Testing
description: Unit Testing.
---


# Unit Testing

Unit Testing also includes complete installation testing.

This testing using `pytest` testing framework. It require to setup the testing environment.


## Pytest testing environment setup

This project uses [pytest](https://docs.pytest.org) to define tests because it allows you to use the `assert` keyword with good formatting for failed assertations.


```bash
pip install -e .[tests]
```



To run all the tests of a project, simply run the `pytest` command:
    ```bash
    pytest
    ```
This project by default uses docker. If you have all the required components installed and do not want to use docker for testing then run:
    ```bash
    USE_DOCKER=False pytest
    ```


## Examples



## Check Linting error in the project

* Check Linting error using `pre-commit`: First install `pip install pre-commit`
    ```bash
    bash pre-commit.sh
    ```
