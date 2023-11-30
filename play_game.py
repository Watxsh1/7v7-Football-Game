from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import threading
import pyttsx3
from absl import app, flags, logging
from gfootball.env import config, football_env
from commentary import Commentary

FLAGS = flags.FLAGS

flags.DEFINE_string('players', 'keyboard:left_players=1',
                    'Semicolon separated list of players, single keyboard '
                    'player on the left by default')
flags.DEFINE_string('level', '', 'Level to play')
flags.DEFINE_enum('action_set', 'default', ['default', 'full'], 'Action set')
flags.DEFINE_bool('real_time', True,
                  'If true, environment will slow down so humans can play.')
flags.DEFINE_bool('render', True, 'Whether to do game rendering.')

# Function to handle TTS in a separate thread
def play_commentary(text):
    try:
        tts_engine = pyttsx3.init()
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        logging.error(f"Error in TTS playback: {e}")

def main(_):
    players = FLAGS.players.split(';') if FLAGS.players else ''
    assert not (any(['agent' in player for player in players])), \
        ('Player type \'agent\' cannot be used with play_game.')

    cfg_values = {
        'action_set': FLAGS.action_set,
        'dump_full_episodes': True,
        'players': players,
        'real_time': FLAGS.real_time,
    }
    if FLAGS.level:
        cfg_values['level'] = FLAGS.level
    cfg = config.Config(cfg_values)
    env = football_env.FootballEnv(cfg)
    commentary = Commentary()

    tts_engine = pyttsx3.init()  # Initialize the TTS engine once
    current_thread = None

    if FLAGS.render:
        env.render()
    env.reset()

    try:
        while True:
            observation, _, done, _ = env.step([])
            commentary_text = commentary.process_observation(observation)

            if commentary_text:
                if current_thread and current_thread.is_alive():
                    if commentary.should_interrupt_with_event(commentary.current_game_mode):
                        tts_engine.stop()  # Stop the current speech

                current_thread = threading.Thread(target=play_commentary, args=(commentary_text,))
                current_thread.start()

            if done:
                env.reset()
    except KeyboardInterrupt:
        logging.warning('Game stopped, writing dump...')
        env.write_dump('shutdown')
        exit(1)

if __name__ == '__main__':
    app.run(main)