"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics




# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger


# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions

list1 = [1,10,13,4,5,5,5,1,6,10,11,12,17,17,1,1,2,3,3,4,4,4,4,4,2,4,5,8,8,9,6,7,7,3,2,1,1,1,4,5,10,11]
listx = [1,2,3,4,5,6,7,8,9,10]
listy = [1,5,2,2,3,4,7,9,6,3]

# TODO: define some custom functions

def measures_of_central_tendency():
    logger.info(f"Points scored: {list1}")
    logger.info(f"Range to 10: {listx}")

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    logger.info(f"Points scored mean:{mean}")
    logger.info(f"Points scored median: {median} ")
    logger.info(f"Points scored mode: {mode}")
    
    logger.info(f"Points scored standard deviation: {stdev} ")
    logger.info(f"Points scored variance: {variance}")

def correlation_function():
    logger.info(f"Listx:{listx}")
    logger.info(f"Listy:{listy}")
    
    correlationxy = statistics.correlation(listx, listy)
    slope, intercept = statistics.linear_regression(listx, listy)

    x_max = max(listx)
    newx = 15
    newy = slope * newx + intercept

    logger.info(f"correlation between x and y: {correlationxy}")
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")
    logger.info(f"We predict that when x = {newx}, y will be about {newy}")

def list_info():
    logger.info(f"General information for the following list: {list1}")

    min_value = min(list1)
    max_value = max(list1)
    length = len(list1)
    total = sum(list1)
    average = (total/length)
    set_list1 = set(list1)
    sorted_values = sorted(list1)
    sorted_reversed = sorted(list1, reverse=True)

    logger.info(f"The min of list1 is {min_value}")
    logger.info(f"The msx of list1 is {max_value}")
    logger.info(f"The length of list1 is {length}")
    logger.info(f"The total of list1 is {total}")
    logger.info(f"The average of list 1 is {average}")
    logger.info(f"The set of list1 is {set_list1}")
    logger.info(f"List1 sorted is {sorted_values}")
    logger.info(f"List1 sorted and reversed is {sorted_reversed}")

def list_transformation():
    logger.info(f"General transformations of list1: {list1}")

    high_scores = list(filter(lambda x: x >=5, list1))
    scores_cubed = list(map(math.cbrt, list1))
    list_value = 4
    volume = (list_value**3)
    
    logger.info(f"The scores that are greater than or equal to 5 are: {high_scores}")
    logger.info(f"The scores cube rooted are: {scores_cubed}")
    logger.info(f"The Volume of a cube with the side equal to 4 is {volume}")

def list_transformation_comprehensions():
    logger.info(f"General list transformations using comprehensions of list1: {list1}")

    goals_over8 = [x for x in list1 if x > 8]
    goals_trippled = [x*3 for x in list1]
    goals_sqrt = [math.sqrt(x) for x in list1]

    logger.info(f"The scores that are greater than 8 are: {goals_over8}")
    logger.info(f"The goals trippled are: {goals_trippled}")
    logger.info(f"Goals square rooted are: {goals_sqrt}")

def show_log():
     with open(logname, "r") as file_wrapper:
         print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    logger.info("CALLING functions")
    logger.info("CALLING measures_of_central_tendency")
    measures_of_central_tendency()

    logger.info("***==============================================***")
    logger.info("CALLING correlation_function")
    correlation_function()

    logger.info("***==============================================***")
    logger.info("CALLING list_info")
    list_info()

    logger.info("***==============================================***")
    logger.info("CALLING list_transformation")
    list_transformation()

    logger.info("***==============================================***")
    logger.info("CALLING list_transformation_comprehensions")
    list_transformation_comprehensions()

    show_log()





   



