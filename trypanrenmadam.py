import gfootball.env as football_env
env = football_env.create_environment(env_name='7v7', representation='pixels', render=True)

state_dims = env.observation_space.shape
print(state_dims)

n_actions = env.action_space.n
print(n_actions)
ppo_steps = 3000
states = []
actions = []
values = []
masks = []
rewards = []

for itr in range(ppo_steps):
    observation, reward, done, info = env.step(env.action_space.sample())
    truncated = False  # Add a default value for truncated

    if done:
        env.reset()


# Close the environment
env.close()
