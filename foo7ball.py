"""Script allowing to play the game by multiple players."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags
from absl import logging

from gfootball.env import config
from gfootball.env import football_env

FLAGS = flags.FLAGS

flags.DEFINE_string('players', 'keyboard:left_players=1;keyboard:right_players=1',
                    'Semicolon separated list of players, single keyboard '
                    'player on the left by default')
flags.DEFINE_string('level', '7v7', 'Level to play, default is 7v7 with easy difficulty')
flags.DEFINE_enum('action_set', 'default', ['default', 'full'], 'Action set')
flags.DEFINE_bool('real_time', True,
                  'If true, environment will slow down so humans can play.')
flags.DEFINE_bool('render', True, 'Whether to do game rendering.')


def main(_):
    cfg_values = {
        'action_set': FLAGS.action_set,
        'dump_full_episodes': True,
        'players': FLAGS.players.split(';') if FLAGS.players else '',
        'real_time': FLAGS.real_time,
        'level': FLAGS.level if FLAGS.level else '7v7',
    }
    cfg = config.Config(cfg_values)
    env = football_env.FootballEnv(cfg)
    if FLAGS.render:
        env.render()
    env.reset()
    try:
        while True:
            _, _, done, _ = env.step([])
            if done:
                env.reset()
    except KeyboardInterrupt:
        logging.warning('Game stopped, writing dump...')
        env.write_dump('shutdown')
        exit(1)


if __name__ == '__main__':
    app.run(main)
