"""Copyright marceloalvescl"""
import csv
from model.stats import Stats
from model.game import Game
from typing import Union
from fastapi import FastAPI

CSV_FILE_PATH = 'games.csv'
stats = Stats()

def verify_games(correct_numbers = ['11', '12', '23', '43', '50', '60']):
    '''Function to open games.csv and verify all of them agains the correct one'''
    with open(CSV_FILE_PATH, 'r') as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)

    games = []
    for row in data_list:
        game = Game(row[6], row[:6])
        stats.compute_game(game.numbers)
        games.append(game)
        print(game.owner, game.numbers)

    print('\n\n\n\n')
    print(stats.most_played())
    print(stats.least_played())
    print('numbers we played stats: \n')
    print(stats.numbers_we_played)
    print('winning numbers stats: \n')
    print(stats.winning_numbers)
    return stats.results_per_game(games, correct_numbers)

app = FastAPI()


@app.get("/resultado/{numbers}")
def result(numbers: str):
    '''Resultado da mega'''
    resultado_mega = verify_games(numbers.split(','))
    return {
        "Ganhamos?": stats.we_won, 
        "Resultado:": resultado_mega
    }
