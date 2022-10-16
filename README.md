# python-mysql-example

A small example to show how to use **mysql** in python.

## Requirements

- [python3](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)

## Prepare

Activate virtual environment

```shell
source env/bin/activate
```

Install dependencies

```shell
pip install -r requirements.txt
```

Deactivate the virtual environment when you finished

```shell
deactivate
```

## Usage

Enter a string (name) and a number (revenue):

```shell
./main.py   # OR    python main.py
Customer name: foo
Customer revenue: 123

READ:   []
CREATE
READ:   [('foo', None)]
UPDATE
READ:   [('foo', Decimal('123'))]
DELETE
READ:   []
```