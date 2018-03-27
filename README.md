# Price Formatter

The script get price and reformat it. If third digit more than four(4) then total price will round. 
Required input formats: digits.digits, digits, digits.(zeros or nothing). 
In all another cases you will see following Error: 

```

INPUT FORMAT ERROR. Required price format see in help

```

# How to run

Example of script launch on Windows, Python 3.5:

```

$ python format_price.py USER_PRICE

```

Enter required price instead of USER_PRICE!!!

# Results

Examples of program results:
```
$ python format_price.py 1500.99

Formated price: 1 500.99

```

```
$ python format_price.py 1500.99sd

INPUT FORMAT ERROR. Required price format see in help

```

# How to launch tests

```

$ python tests.py

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
