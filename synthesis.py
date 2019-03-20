import gym
from gym import spaces
from gym.utils import seeding


class SimpleSynthesis(gym.Env):
    """
    Description:
        An one-agent environment for synthesis. The goal is to synthesize target molecule.
    Observation:
        STUB
        The current synthesized molecule properties, like ...
    State:
        Set of molecules synthesized so far
        
    Actions:
        Type: Discrete(n)
        Enumerated available reagents.

    Reward:
        Closeness of current molecule to target one.
    Starting State:
        We have empty molecule at first.
    Episode Termination:
        The target molecule is synthesized.
        The maximum number of steps is reached.
    """

    def reset(self):
        self._reset()

    def _reset(self):
        self.state = None
        self.steps = 0
        return self.state

    def step(self, action):
        """
        Make new synthesis using current molecule and chosen reagent.
        :param action: chosed reagent to add
        """
        self._step(action)

    def _step(self, action):
        assert self.action_space.contains(action), \
            "%r (%s) invalid" % (action, type(action))
        self.state, similarity_score = self._add_reagent(action)

        done = False
        if self.steps >= self.max_steps or similarity_score == 1:
            done = True

        reward = similarity_score
        return self.state, reward, done, {}

    def render(self, mode='human', **kwargs):
        raise NotImplementedError

    def __init__(self, reagent_number, target, step_number=10):
        self.target = target
        self.action_space = spaces.Discrete(reagent_number)
        # FIXME: observation space should be replaced by correct one
        self.observation_space = spaces.Discrete(5)

        self.seed()
        self.state = None

        self.steps = 0
        self.max_steps = step_number

        self.np_random = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _add_reagent(self, reagent_num):
        """
        Adding a reagent to current molecule.
        :param reagent_num: reagent to add
        :return: set of new molecules, similarity score of closest molecule
                similarity score for a product and target
        """
        return None, 0.0
