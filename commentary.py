import random

class Commentary:
    def __init__(self):
        # Match information
        self.current_game_mode = None
        self.first_kickoff = True
        self.home_score = 0
        self.away_score = 0
        self.possession_team = -1


        # Predefined commentary options for each scenario
        self.commentary_options = {
            'kickoff': [
                'The game kicks off in high spirits.',
                'And the ball rolls with the kickoff!',
                'The teams start aggressively with the kickoff.',
                'Excitement builds with the initial kickoff.',
                'A powerful kickoff starts the game!'
            ],
            'goal_kick': [
                'The goalkeeper prepares for a goal kick.',
                'A goal kick could turn the tide.',
                'The ball is set for a goal kick.',
                'Focus shifts to the goal kick.',
                'A strategic goal kick is in play.'
            ],
            'free_kick': [
                'A crucial free kick is coming up.',
                'The tension rises with this free kick.',
                'Ready for a potentially game-changing free kick.',
                'A free kick in a promising position.',
                'The team lines up for an important free kick.'
            ],
            'corner': [
                'The team readies for a corner kick.',
                'A corner kick could create a chance.',
                'Eyes on the corner flag for this kick.',
                'The corner kick offers a scoring opportunity.',
                'Anticipation builds for the corner kick.'
            ],
            'throw_in': [
                'The game resumes with a throw-in.',
                'A quick throw-in to maintain the tempo.',
                'Throw-in taken amidst the excitement.',
                'The ball is back in play with a throw-in.',
                'A strategic throw-in by the team.'
            ],
            'penalty': [
                'The crowd holds its breath for the penalty.',
                'A penalty kick, a moment of high drama!',
                'The penalty could be a game-changer.',
                'Tension peaks with this penalty kick.',
                'A crucial penalty kick is about to be taken.'
            ],
            'yellow_card_home': [
                'A yellow card for the home team.',
                'The home team receives a cautionary yellow card.',
                'The referee books a home player with a yellow.',
                'A home team player is warned with a yellow card.',
                'Yellow card - the home team must be careful now.'
            ],
            'yellow_card_away': [
                'The away team gets a yellow card.',
                'Yellow card shown to the away team.',
                'An away player receives a yellow card.',
                'The away team is cautioned with a yellow card.',
                'A stern warning to the away team with a yellow card.'
            ],
            'goal_home': [
                'Goal! The home team scores!',
                'The home team jubilates with a goal!',
                'A stunning goal by the home team!',
                'The home team finds the net!',
                'A brilliant goal for the home team!'
            ],
            'goal_away': [
                'The away team strikes with a goal!',
                'Goal for the away team!',
                'The away team celebrates a fine goal!',
                'A remarkable goal by the away team!',
                'The away team scores spectacularly!'
            ],
            'filler': [
    'The teams are exhibiting great skill today, showcasing their months of rigorous training and dedication.',
    'A moment of calm in an intense game, as players take a brief respite to regroup and strategize for the next play.',
    'Players are eagerly looking for opportunities, scanning the field with keen eyes and ready to make their move.',
    'The game is evenly balanced at this stage, with both teams demonstrating equal prowess and leaving fans in suspense.',
    'Both teams are playing with great determination, their resolve unwavering as they vie for the upper hand in this match.',
    'The stadium resonates with the roar of excited fans, their cheers echoing as a testament to the thrilling game unfolding.',
    'Players are weaving through their opponents with remarkable agility, displaying finesse and control in every move.',
    'The ball travels from player to player, a seamless display of teamwork and coordination on the field.',
    'Intensity builds as the teams engage in a tactical battle, each move more crucial than the last in this chess-like game.',
    'The goalkeeper stands vigilant, a sentinel guarding the goalpost with unwavering focus and ready to leap into action.',
    'Meticulous passing between the players, as they advance with a strategic rhythm, seeking an opening in the defense.',
    'A surge of energy sweeps through the players, their speed and agility amplified as they push towards the goal.',
    'Defenders form an impenetrable wall, skillfully thwarting the advances of the opposing team with practiced precision.',
    'Midfielders orchestrate the games rhythm, seamlessly linking defense and attack with their pivotal plays.',
    'The coach watches intently from the sidelines, strategizing and guiding the team with a keen tactical mind.',
    'Players exhibit incredible stamina, maintaining a high level of play despite the games unrelenting pace.',
    'The ball dances at the players feet, a testament to their technical prowess and years of honed skill.',
    'A game of enduring spirit and passion, with players leaving every ounce of their energy on the field.',
    'Strategic formations shift across the field, each team adapting and reacting to the flow of the game.',
    'The referee keenly observes the match, ensuring fair play and upholding the spirit of the game with every decision.',
    'Players movements are like a well-rehearsed dance, choreographed and precise in execution.',
    'The match is a showcase of both physical might and mental acumen, a true test of the players abilities.',
    'The field is a canvas, and the players are the artists, each stroke of the foot painting a picture of the game.',
    'The crowd holds its breath in anticipation of the next critical play, ready to erupt in joy or despair.',
    'The air is thick with competition, each team vying to outdo the other in a display of skill and strategy.',
    'Players dash across the field with lightning speed, chasing the ball and their dreams of victory.',
    'The match is a symphony of athleticism, each pass and move contributing to the beautiful games melody.',
    'Tactics evolve with every minute, the coaches strategies unfolding like an intricate game of chess.',
    'The players relentless pursuit of the ball is a testament to their unyielding dedication and spirit.',
    'The stadium is alive with the sound of chanting fans, their voices rising in unison to support their teams.',
    'The match unfolds like a gripping drama, each scene more compelling than the last, keeping the audience captivated.',
    'The players skillful control of the ball is mesmerizing, showcasing years of practice and mastery.',
    'The teams navigate the field with strategic precision, each maneuver a critical piece of the games puzzle.',
    'The stadium is a fortress of football fervor, with fans and players united in their passion for the game.',
    'The game ebbs and flows like a tide, with moments of calm followed by bursts of intense action.',
    'Players jostle for position, their physical strength and tactical acumen on full display.',
    'The ball is a coveted prize, players from both teams battling fiercely to claim control.',
    'Each pass is a thread in the tapestry of the match, woven together to create a masterpiece of football.',
    'The stadiums energy is palpable, a collective anticipation hanging in the air as the game progresses.',
    'Players footwork is like a ballet on grass, each step deliberate and graceful, yet full of power and purpose.',
    'The game is a testament to the players resilience, battling fatigue and pressure with unwavering focus.',
    'The field echoes with the sound of boots striking the ball, a rhythm that drives the heartbeat of the game.',
    'Each teams strategy unfolds, a dynamic and fluid plan adapting to the ever-changing landscape of the match.',
    'The players quick reflexes and sharp decision-making are crucial in the fast-paced environment of the game.',
    'The match is an embodiment of teamwork and individual brilliance, each player a vital cog in the teams machine.',
    'The game is a rollercoaster of emotions, each twist and turn eliciting cheers and gasps from the captivated crowd.',
    'The teams navigate the pitch like seasoned navigators, each move calculated and deliberate in the quest for victory.',
    'Players showcase their tactical intelligence, reading the game and anticipating their opponents moves.',
    'The stadium is a cauldron of passion, with each fan living and breathing every moment of the match.',
    'The match is a battle of endurance, with players pushing their limits to sustain their performance.',
    'Players quick thinking is on display, reacting to the unfolding game with precision and creativity.',
    'The game is a journey of highs and lows, each team experiencing moments of triumph and challenge.',
    'The match is punctuated by moments of brilliance, individual plays that stand out in the tapestry of the game.',
    'Players physical prowess is matched by their mental toughness, enduring the pressures of high-stakes competition.',
    'The stadium thrums with the energy of the crowd, a chorus of voices united in their love for the game.',
    'Each team crafts its narrative on the field, a story of ambition, skill, and the pursuit of footballing glory.',
    'The games pace is relentless, a non-stop display of action that keeps players and fans on the edge of their seats.',
    'The players agility and speed are a spectacle, a display of human potential and athletic excellence.',
    'The match is a canvas of strategy and skill, each team painting its path towards victory.',
    'The players coordination and teamwork are akin to a well-oiled machine, each part working in harmony.',
    'The game is a showcase of the players passion for football, their love for the game evident in every play.',
    'The teams strategic maneuvering is a chess game brought to life, each move critical to the matchs outcome.',
    'The stadium buzzes with the excitement of the fans, their energy fueling the players performance.',
    'The match is a testament to the players commitment, their dedication to the sport evident in every stride.',
    'Players navigate the field with purpose, each movement a calculated step in the dance of football.',
    'The game is a display of athletic artistry, each play a brushstroke in the masterpiece of the match.',
    'The teams competitive spirit is palpable, each striving to outperform the other in a display of footballing prowess.',
    'The players resilience is on display, battling through challenges and setbacks with unwavering determination.',
    'The stadium is a temple of football, where fans and players alike worship the beautiful game.',
    'The games tempo fluctuates, a dynamic and ever-changing rhythm that keeps the players and fans engaged.',
    'Players showcase their strategic acumen, outthinking their opponents in a mental battle on the field.',
    'The match is a journey through the peaks and valleys of competition, each moment a critical step towards victory.',
    'The players physical and mental agility is tested, their skills honed through years of training and experience.',
    'The game is a spectacle of footballing talent, each player contributing their unique skills to the teams effort.',
    'The teams tactical battle is a fascinating display, each trying to outmaneuver the other in a game of skill and wit.',
    'The stadium reverberates with the sound of the game, a symphony of cheers, whistles, and the thud of the ball.',
    'The match is a display of footballing grace under pressure, players maintaining composure in the heat of competition.',
    'Players movements are precise and deliberate, a dance of strategy and skill played out on the field.',
    'The game is a clash of footballing titans, each team a powerhouse of skill and strategy vying for supremacy.',
    'The players relentless pursuit of victory is inspiring, their dedication to the game evident in every move.',
    'The stadium is a melting pot of emotions, each fan living vicariously through the highs and lows of the match.',
    'The match is a testament to the beauty of football, a sport that captivates and enthralls fans around the world.',
    'Players display a blend of finesse and power, balancing technical skill with physical strength in their play.',
    'The game is an exhibition of footballing excellence, a celebration of the sports rich heritage and culture.',
    'The teams strategic dueling is a captivating display, each move a critical step in the chess game of football.'
            ]

        }

    def get_random_commentary(self, category):
        return random.choice(self.commentary_options[category])

    def process_observation(self, observation):
        # Input to model
        prompt = ''

        # Game mode information
        game_mode = observation['game_mode']
        if self.current_game_mode != game_mode:
            self.current_game_mode = game_mode
            if self.first_kickoff:
                self.first_kickoff = False
                prompt = self.get_random_commentary('kickoff')
            elif self.current_game_mode == 1:  # Kickoff
                prompt = self.get_random_commentary('kickoff')
            elif self.current_game_mode == 2:  # Goal Kick
                prompt = self.get_random_commentary('goal_kick')
            elif self.current_game_mode == 3:  # Free Kick
                prompt = self.get_random_commentary('free_kick')
            elif self.current_game_mode == 4:  # Corner
                prompt = self.get_random_commentary('corner')
            elif self.current_game_mode == 5:  # Throw-in
                prompt = self.get_random_commentary('throw_in')
            elif self.current_game_mode == 6:  # Penalty
                prompt = self.get_random_commentary('penalty')

        # Card/booking information


        # Goal information
        score = observation['score']
        if score[0] > self.home_score:
            self.home_score = score[0]
            prompt = self.get_random_commentary('goal_home')
        if score[1] > self.away_score:
            self.away_score = score[1]
            prompt = self.get_random_commentary('goal_away')

        # Add filler commentary if there is no significant event
        if not prompt:
            prompt = self.get_random_commentary('filler')

        return prompt
    
    def should_interrupt_with_event(self, game_mode):
        """
        Determines if the current commentary should be interrupted 
        for an event-specific commentary.
        """
        interrupting_modes = [1, 2, 4, 6]  # Kickoff, Goal Kick, Corner, Penalty
        return game_mode in interrupting_modes