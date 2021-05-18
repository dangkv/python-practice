# [Pytest](https://docs.pytest.org/)

# Installing pytest
```shell script
python -m pip install pytest
```

# Pytest Conventions

By default pytest only identifies the file names starting with `test_` or 
ending with `_test` as the test files.

```text
test_calculator.py - valid
calculator_test.py - valid
testcalculator.py -invalid
logincalculator.py -invalid
```

Pytest requires the test method names to start with `test`.

```text
def test_add(): - valid
def testadd(): - valid
def add(): - invalid
```

# Learning Resources
[Python Testing 101 with pytest](https://www.youtube.com/watch?v=etosV2IWBF0)

[PyTest Tutorial | Unit Testing Framework In Python | How to use PyTest | Python Training | Edureka](https://www.youtube.com/watch?v=byaxg00Gf9I)

[Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)