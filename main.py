# ------------------------------------------------------------------
# FileName:         main.py
# Author:           宁文彬
# Github:           http://github.com/simuler
# Version:          V 1.0
# Description:      草酸钴合成过程gym环境测试程序
# ------------------------------------------------------------------

import gym
import numpy as np

if __name__ == '__main__':
    print("start")
    env = gym.make('CoC2O4withoutT7_env-v0')
    init_state = env.reset()

    # test action
    action = np.ones((11,1), dtype=float) * 0.0005
    for k in range(5):
        print("第几轮= ", k)
        for i in range(11):
            next_state, r, done, _ = env.step(action[i])
            print("reward = ", r)
            print("is done :", done)
        state = env.reset()
        print("--------------此轮结束---------------------")