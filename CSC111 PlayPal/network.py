""" The file responsible for reading the data and creaeting our decision tree"""

import csv


def read_steam_data(steam_data: str) -> dict:
    """Load the data from the CSV file

        Return a dictionary with X key values
            - Games: A list of Game objects
            - Genres: A set of strings that represent unique game genres

        Preconditions:
            - steam_data refers to a valid CSV file in the format described on the assignment handout
    """
    with open(steam_data, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        main_dict = {}
        genres = set()
        games = []
        for row in reader:
            if row[1] == 'app':
                game_genres = row[13].split(",")
                genres.add(genre for genre in game_genres)
                game_name = get_game_name(row[2])
                # game = GameNode() #Implement this after Ivan is done with the tree
                games.append(game_name)  # To be changed to game afterwards
        main_dict['Genres'] = genres
        main_dict['Games'] = games
        return main_dict


def get_game_name(game_name: str) -> str:
    """A helper function for read_steam_data that helps get names of games that
    cannot be encoded using the default encoder (UTF-8)
    """
    try:
        encoded_name = game_name.encode('utf-8')
    except UnicodeEncodeError:
        return ''
    return encoded_name.decode('utf-8')
