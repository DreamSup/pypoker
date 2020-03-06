from re_learning_player import RLPlayer
from pypokerengine.api.game import setup_config, start_poker

config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
config.register_player(name="p1", algorithm=RLPlayer())
config.register_player(name="p2", algorithm=RLPlayer())
config.register_player(name="p3", algorithm=RLPlayer())
game_result = start_poker(config)
print(game_result)