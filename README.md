# Beginner Python Projects

This folder contains small beginner-friendly Python projects used for learning and practice.

Included projects

1. Secret Auction: a simple auction program (projects/Secret Auction/main.py)
2. Find leap year
3. Calculator Program

## Secret Auction Program

How to run

1. Make sure you have Python 3 installed and available from the command line.

   ```cmd
   python "Secret Auction\main.py"
   ```

## Leap Year Program

- File: `leap_year.py`
- Description: A small script that asks the user to enter a year and prints whether that year is a leap year.

Rules used by the program:

- A year is a leap year if it is divisible by 4.
- However, years divisible by 100 are not leap years unless they are also divisible by 400.

How to run:

```cmd
python leap_year.py
```

Example interaction:

```
Enter a year: 2400
True
Enter a year: 1989
False
```

See `leap_year.py` for the implementation.

## Calculator Program

- File: `calculator.py`
- Description: A small interactive calculator that asks the user for two numbers and an operator (+, -, \*, /), then prints the result.

Notes:

- Inputs are parsed as integers. Division (/) will produce a floating-point result when needed.
- This script uses the Python `match` statement and requires Python 3.10 or later.

How to run:

```cmd
python calculator.py
```

Example interaction:

```
Enter the first number: 12
Enter the second number: 5
Enter the operator: /
2.4
```

See `calculator.py` for the implementation.
