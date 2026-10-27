from gym.envs.registration import register

def register_envs():
    register(
        id='cheetah-hw4_part1-v0',
        entry_point='rob831.hw4_part1.envs.cheetah:HalfCheetahEnv',
        max_episode_steps=1000,
    )
    register(
        id='obstacles-hw4_part1-v0',
        entry_point='rob831.hw4_part1.envs.obstacles:Obstacles',
        max_episode_steps=500,
    )
    register(
        id='reacher-hw4_part1-v0',
        entry_point='rob831.hw4_part1.envs.reacher:Reacher7DOFEnv',
        max_episode_steps=500,
    )
