from board import *
from constants import *
from RandomPlayer import *
from Game import *
from model import *
from DeepPlayer import *
from Trainer import *
from utils import Evaluator

from config import ModelConfig

config = ModelConfig()
model = C4Model(config)
model.build()

# make a trainer to train the model on self-play data
trainer = Trainer(model)
trainer.setup()
losses_before, draws_before = Evaluator.combat_random(trainer.get_trained_model(), 10)
trainer.train_epoch(games = 10, epochs = 20, generations = 1)
losses_during, draws_during = Evaluator.combat_random(trainer.get_trained_model(), 10)
trainer.train_epoch(games = 10, epochs = 20, generations = 1)
losses_after, draws_after = Evaluator.combat_random(trainer.get_trained_model(), 10)

print("losses before training: " + str(losses_before))
print("losses during training: " + str(losses_during))
print("losses after training: " + str(losses_after))