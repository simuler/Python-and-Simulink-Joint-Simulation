# ------------------------------------------------------------------
# FileName:         CoC2O4withoutT7.py
# Author:           宁文彬
# Github:           http://github.com/simuler
# Version:          V 1.0
# Description:      草酸钴合成过程gym环境搭建
# ------------------------------------------------------------------

import matlab.engine
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
import os
import sys

class CoC2O4withoutT7Env(gym.Env):
    def __init__(self):

        self.action_space = spaces.Discrete(2)
        high = np.array([1e20, 1e20, 1e20, 1e20, 1e20, 1e20], dtype=np.float64)
        self.observation_space = spaces.Box(-high, high, dtype=np.float64)

        self.seed()
        self.state = None
        self.mean = np.array([2, 2, 5.6e16, 7.8e10, 1.2e5, 0.2])
        self.std = np.array([5, 0.5, 1.3e16, 1.6e10, 3.5e4, 0.07])

        self.time = 0
        self.done = False
        self.eng = matlab.engine.start_matlab()
        self.env_name = 'CoC2O4withoutT7'
        self.eng.load_system(self.env_name)

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        self.time += 60
        state = self.eng.CoC2O4_step(float(action), self.time, nargout=1)
        state = np.array(state)
        state = np.squeeze(state)

        if self.time == 660:
            self.done = True
            reward = state[3] / state[2] * 1e6
            if np.isnan(reward):
                reward = 0
        else:
            reward = 0
        state = (state - self.mean) / self.std
        return np.array(state, dtype=np.float64), reward, self.done, {}

    def reset(self):
        self.state = [0.0, 1.4, 0.0, 0.0, 0.0, 0.0]
        self.eng.reset_file(nargout=0)  # 运行初始化的m文件
        self.eng.CoC2O4_step(float(1e-6), 1, nargout=1)
        self.time = 0
        self.done = False
        return np.array(self.state, dtype=np.float64)