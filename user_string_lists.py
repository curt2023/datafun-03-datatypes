"""
Modify this docstring.

"""

# imports first
import math
import statistics
import random

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

chaos_players =["George", "Bob", "Sally", "Denise", "Haley", "Frank", "Bill", "Aaron", "Mike"," Curtis", "Erin"]
possible_outcomes = ["win", "lose", "tie"]
teams_list = ["Sharks","Tigers", "Chaos", "Blue Streak", "Laser Legs"]
game_location = ["home","away"]

# reusable functions next

def random_choice():
    logger.info(f"Random value selected from teams: {teams_list}")

    random_value = (random.choice(teams_list))

    sentence = (
        f"The {random.choice(teams_list)} will be the {random.choice(game_location)} team today!!!"
        f" {random.choice(teams_list)} {random.choice(possible_outcomes)}!!" )

    logger.info(f"The random team is {random_value}")
    logger.info(sentence)

def process_text_juliuscaesar():
    logger.info(f"Calling process_text_juliuscaesar")

    with open("text_juliuscaesar.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()
        unique_words = set(list_words)

        word_count = len(list_words)
        unique_word_count = len(unique_words)
       
    
        


        logger.info(f"There are {word_count} words in the file.")
        logger.info(f"There are {unique_word_count} unique words in the file.")
        logger.info(f"The set of unique words is: {unique_words}")



def show_log():
    with open(logname, "r") as file_wrapper:
         print(file_wrapper.read())


# call functions and execute code
# use if __name__ == "__main__":

if __name__ == "__main__":
    logger.info("CALLING functions")
    logger.info("CALLING: random_choice function")

    random_choice()

    logger.info("*****=======================================******")
    logger.info("CALLING: process_text_juliuscaesar function")

    process_text_juliuscaesar()


    show_log()