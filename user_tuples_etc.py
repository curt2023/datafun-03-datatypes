"""
Modify this docstring.

"""
import math
import statistics
import random


from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

#tuples
game_location_usa_tuple = ("Huston", "Dallas", "Kansas City", "Des Moines", "New York")
game_location_eu_tuple = ("Berlin", "London", "Paris", "Spain")

logger.info(f"game_location_usa_tuple = {game_location_usa_tuple}")
logger.info(f"game_location_usa_tuple = {game_location_eu_tuple}")
logger.info("****=================================****")

#sets

teams_set = {"Chaos", "Sharks", "Laser Legs", "Tigers", "Regulators"}
fall_points = {4,2,10,9,5,1}
spring_points = {5,3,3,8,9,7}

logger.info(f"seta = {fall_points}")
logger.info(f"setb = {spring_points}")
logger.info("****=================================****")

#intersection

points_intersection = fall_points & spring_points

#union
annual_points = fall_points | spring_points

logger.info(f"setc = {points_intersection}")
logger.info(f"setd = {annual_points}")
logger.info("****=================================****")

soccer_data_dict = {
    "player": ["Sally", "George", "Denise", "Frank", "Mark", "Haley"],
    "age": [25, 23, 35, 48, 52, 33],
    "position": ["striker", "striker", "sweeper", "wing", "striker", "wingback"],
    }
logger.info(f"soccer_data_dict = {soccer_data_dict}")
logger.info("****=================================****")


#dictonaries and text

with open("text_hamlet.txt") as file_object:
     word_list = file_object.read().split()
     unique_word_count = set(word_list)

# loop to count words
word_count_dict1 = {}
for word in word_list:
    if word in word_count_dict1:
        word_count_dict1[word] += 1
    else:
        word_count_dict1[word] = 1
logger.info(f"Dictonary loop to count words result is {word_count_dict1}")
logger.info("****=================================****")

# comprehension to count words

word_count_dict2 = {word: word_list.count(word) for word in word_list}

logger.info(f"Word count comprehension result is {word_count_dict2}")

def show_log():
    with open(logname, "r") as file_wrapper:
         print(file_wrapper.read())

if __name__=="__main__":
     
     logger.info("CALLING functions in user_tuple_etc.py")
     logger.info("****=================================****")

     show_log()

    