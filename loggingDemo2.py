import logging

logging.basicConfig(filename = "log.txt", level = logging.INFO)

logging.info("A new request came")

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x/y)
except ZeroDivisionError as msg:
    print("cannot divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("Enter only int values")
    logging.exception(msg)
logging.info("value of x: " + str(x))
logging.info("value of y: " + str(y))
logging.info("Request processing Completed")