# FOO7BALL

FOO7BALL is a 7vs7 player vs AI  football game [with commentary] developed using gfootball engine
## Step-1 [[INSTALLATION]](https://github.com/google-research/football)

install [gfootball](https://github.com/google-research/football)

```bash
pip install gfootball
```

## Step-2 [[UNSERSTANDING]](https://github.com/Watxsh1/7v7-Football-Game/blob/main/trypanrenmadam.py)
Understanding the code:

### Support
goal kicks

side kicks

corner kick

both yellow and red cards

offsides

handballs

penalty

Each of these actions return a unique value.[which is later used in commentary]

The length of the game is measured in terms of the
number of frames, and the default duration of a full game
is 3000 (10 frames per second for 5 minutes)

### Mini Map
The Mini Map is represented by four 72 × 96 matrices encoding information about the home
team, the away team, the ball, and the active player respectively.

### Pixels
The representation consists of a 1280 × 720 RGB
image corresponding to the rendered screen. This includes
both the scoreboard and a small map in the bottom middle
part of the frame from which the position of all players can
be inferred in principle.

### The floats 
This representation provides a compact encoding and consists of a 115-dimensional vector summarizing many aspects of the game, such as players coordinates,
ball possession and direction, active player, or game mode.

### Actions:
19 actions each assigned to a Number ![image](https://github.com/Watxsh1/7v7-Football-Game/assets/101169160/ad048831-6dfc-4ae0-af47-aeb31051a69c)


## Step-3 [[CREATING ENVIRONMENT]](https://github.com/Watxsh1/7v7-Football-Game/blob/main/7v7.py)
We have to make 2 teams - team right & team left

each team must have one goal keeper and 6 players

## Step-4 [[TRAIN PPO MODEL]](https://github.com/Watxsh1/7v7-Football-Game/blob/main/ppotraining7v7.py)

Multiple Agent Re-enforcement learning using Actor - Critic Model.
![image](https://github.com/Watxsh1/7v7-Football-Game/assets/101169160/89d8637a-633b-45bb-9605-82efab89ea39)


## Step-5[[TEST MODEL]](https://github.com/Watxsh1/7v7-Football-Game/blob/main/foo7ball.py)

Run the game without Player controls i.e., AI vs AI check if both the AI's try to score the Goal.
if yes the model is correct.

## Step-6[[KEY-BOARD MAPPINGS]](https://github.com/Watxsh1/7v7-Football-Game/blob/main/play_game.py)

We use default Controls given by the GFootball library

s - pass | pressure

a - lofted pass | slide

d - shot | pressure

w - long pass | gk run

q - switch player

c - dribble

e- sprint

## Step-7 [[SCENARIO BASED COMMENTARY]](https://github.com/Watxsh1/7v7-Football-Game/blob/main/commentary.py)

Scenario based commentary generated by chatGPT using pyttsx3

