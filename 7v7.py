
from . import *

def build_scenario(builder):
    builder.config().game_duration = 3000
    builder.config().right_team_difficulty = 0.05
    builder.config().left_team_difficulty = 0.05
    builder.config().deterministic = False
    if builder.EpisodeNumber() % 2 == 0:
        first_team = Team.e_Left
        second_team = Team.e_Right
    else:
        first_team = Team.e_Right
        second_team = Team.e_Left
    builder.SetTeam(first_team)
    builder.AddPlayer(-0.7, 0.0, e_PlayerRole_GK, controllable=False)
    builder.AddPlayer(0.0, -0.15, e_PlayerRole_CF)
    builder.AddPlayer(-0.3, -0.1, e_PlayerRole_LB)
    builder.AddPlayer(-0.3,  0.1, e_PlayerRole_CB)
    builder.AddPlayer(-0.5,  0.0, e_PlayerRole_CB)
    builder.AddPlayer(-0.6, -0.2, e_PlayerRole_CM)
    builder.AddPlayer(-0.6,  0.2, e_PlayerRole_CM)

    builder.SetTeam(second_team)
    builder.AddPlayer(-0.7, 0.0, e_PlayerRole_GK, controllable=False)
    builder.AddPlayer(0.0, -0.15, e_PlayerRole_CF)
    builder.AddPlayer(-0.3, -0.1, e_PlayerRole_LB)
    builder.AddPlayer(-0.3,  0.1, e_PlayerRole_CB)
    builder.AddPlayer(-0.5,  0.0, e_PlayerRole_CB)
    builder.AddPlayer(-0.6, -0.2, e_PlayerRole_CM)
    builder.AddPlayer(-0.6,  0.2, e_PlayerRole_CM)

