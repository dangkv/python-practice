# [Pytest](https://docs.pytest.org/)

## Installing Pytest
```shell script
python -m pip install pytest
```

## Pytest Conventions

By default pytest only identifies the file names starting with `test_` or 
ending with `_test` as the test files.

```text
test_calculator.py - valid
calculator_test.py - valid
testcalculator.py -invalid
calculator.py -invalid
```

Pytest requires the test method names to start with `test`.

```text
def test_add(): - valid
def testadd(): - valid
def add(): - invalid
```

## Assertions in Pytest
```python
assert "hello" == "Hai" # is an assertion failure.
assert 4==4 # is a successful assertion
assert True # is a successful assertion
assert False # is an assertion failure.
```

## [Fixture in Pytest](https://docs.pytest.org/en/stable/fixture.html#what-fixtures-are)
Fixture, in Pytest is a decorator for methods that prepares data before
performing a test. Example, in my [test_calculator.py](test/test_calculator.py)
file, I must initialize the `calculator` class before performing each tests.

### 1. Create fixture method
Create a fixture method is as simple as adding `@pytest.fixture` decorator
on top of the fixture method.

```python
import pytest
from pytest_example import calculator_example as calc

@pytest.fixture
def calculator():
    return calc.Calculator()
```

### 2. Apply fixture to each test
Add fixture method variable as a test method argument.
```python
def test_add(calculator):
    pass
```

## [Custom Markers in Pytest](https://docs.pytest.org/en/stable/example/markers.html#working-with-custom-markers)
Pytest gives you the option to execute tests in groups instead of testing each
test individually. In this example I will show you a basic way to group your 
tests however Pytest has more complex features to go about grouping tests.

### 1. Register custom markers
Create a `pytest.ini` file in your `test` folder and register all custom 
markers you plan to use to group your test methods.

```text
[pytest]
markers =
    operations: test operations functions from calculator.py
    exceptions: test exceptions from calculator.py
``` 

### 2. Add custom mark decorator to your methods
Add decorators `@pytest.mark.name_of_the_mark` on top of your test methods. 

```python
@pytest.mark.operations
def test_add():
    pass

@pytest.mark.operations
def test_subtract():
    pass

@pytest.mark.exceptions
def test_divide_by_zero():
    pass
```

### 3. Run custom marked tests
To run marked tests use the `-m` flag to specify which marker to test in 
terminal.
```shell script
pytest -m operations
```

## Best Practices
[Arrange Act Assert pattern](https://jamescooke.info/arrange-act-assert-pattern-for-python-developers.html)

[Packaging a Python Library](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure)


## Learning Resources
[Python Testing 101 with pytest](https://www.youtube.com/watch?v=etosV2IWBF0)

[PyTest Tutorial | Unit Testing Framework In Python | How to use PyTest | Python Training | Edureka](https://www.youtube.com/watch?v=byaxg00Gf9I)

[Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)