"""Copyright marceloalvescl"""

class Stats:
    """Class to deal with statistics about the games played"""

    def __init__(self):
        self.numbers_we_played = {
            '01': 0,'02': 0,'03': 0,'04': 0,'05': 0,'06': 0,'07': 0,'08': 0, '09': 0, '10': 0,
            '11': 0,'12': 0,'13': 0,'14': 0,'15': 0,'16': 0,'17': 0,'18': 0, '19': 0, '20': 0,
            '21': 0,'22': 0,'23': 0,'24': 0,'25': 0,'26': 0,'27': 0,'28': 0, '29': 0, '30': 0,
            '31': 0,'32': 0,'33': 0,'34': 0,'35': 0,'36': 0,'37': 0,'38': 0, '39': 0, '40': 0,
            '41': 0,'42': 0,'43': 0,'44': 0,'45': 0,'46': 0,'47': 0,'48': 0, '49': 0, '50': 0,
            '51': 0,'52': 0,'53': 0,'54': 0,'55': 0,'56': 0,'57': 0,'58': 0, '59': 0, '60': 0,
        }
        self.winning_numbers = {}
        self.we_won = False

    def most_played(self):
        """Return key indicating most played number"""
        return max(self.numbers_we_played, key=lambda k: self.numbers_we_played[k])

    def least_played(self):
        """Return key indicating least played number"""
        return min(self.numbers_we_played, key=lambda k: self.numbers_we_played[k])

    def update_board_numbers_we_played(self, numbers_played):
        """Function to update the numbers played board"""
        for number in numbers_played:
            self.numbers_we_played[number] = self.numbers_we_played[number] + 1

    def compute_game(self, numbers_played):
        """Function to receive a game and compute numbers played"""
        self.update_board_numbers_we_played(numbers_played)

    def initiate_winning_numbers_board(self, correct_numbers):
        """Function to initiate winning_numbers dictionary"""
        for number in correct_numbers:
            self.winning_numbers[number] = 0

    def results_per_game(self, games, correct_numbers):
        """Function to verify results of our games"""
        self.initiate_winning_numbers_board(correct_numbers)
        for game in games:
            for number in game.numbers:
                if number in correct_numbers:
                    game.numbers_correct += 1
                    self.winning_numbers[number] = self.winning_numbers[number] + 1

        acertos = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for game in games:
            acertos[game.numbers_correct] += 1
        
        if acertos[6] >= 1:
            self.we_won = True
            print("""
                    PUTA QUE O PARIU A GNT GANHOU ESSA PORRA MLK, MEU DEUS DO CÉU
                    """)
        return acertos