from DeepPlayer import *
from RandomPlayer import *
from constants import *
from Game import *

class Evaluator:
    # returns the fraction of wins of model_1 against model_2
    @staticmethod
    def combat_model(model_1, model_2, iterations):
        player_1 = DeepPlayer(model_1, PLAYER_1)
        player_2 = DeepPlayer(model_2, PLAYER_2)
        
        return Evaluator.combat(player_1, player_2, iterations)
    
    # returns the fraction of wins of model against a random player
    @staticmethod
    def combat_random(model, iterations):
        player_1 = RandomPlayer()
        player_2 = DeepPlayer(model, PLAYER_2)
        
        return Evaluator.combat(player_1, player_2, iterations)
    
    # has players 1 and 2 play against each other
    @staticmethod
    def combat(player_1, player_2, iterations):
        player_1_wins = 0
        player_2_wins = 0
        draws = 0
        
        for i in range(iterations):
            print("game " + str(i))
            
            player_1.reset()
            player_2.reset()
            game = Game(player_1, player_2)
            res = game.play()
        
            if res == PLAYER_1_WINS:
                player_1_wins += 1
                print("player 1 wins")
            elif res == PLAYER_2_WINS:
                player_2_wins += 1
                print("player 2 wins")
            elif res == DRAW:
                draws += 1
                print("draw")
            
        return player_1_wins / iterations, draws / iterations