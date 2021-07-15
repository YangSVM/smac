from smac.env import StarCraft2Env
import numpy as np

env=StarCraft2Env(map_name='3m') 
env.reset()

np.random.seed(0)

for i in range(200):

    actions = []
    for i in range(3):
        action_avail = env.get_avail_agent_actions(i)
        # print('agent ', i, 'avail_action: ', action_avail)
        if action_avail[0] == 1:
            # 如果死亡，只有一个动作
            action = 0
        elif any(action_avail[6:8]) == 1:
            # 如果能够攻击，就攻击
            avail_actions_ind = np.nonzero(action_avail[6:9])[0]
            action = np.random.choice(avail_actions_ind)+6
            print('attack')
        elif action_avail[4] == 1:
            # 往东走
            action = 4
        else:
            avail_actions_ind = np.nonzero(action_avail)[0]
            action = np.random.choice(avail_actions_ind)

        actions.append(action)
    # print('actions: ', actions)
    
    r,t,info =env.step(actions)
    print(info)
    r_totall  = env.reward_battle()
    r_multi = env.reward_multi_task()
    r_multi_sum = 0
    for ri in r_multi:
        r_multi_sum +=ri
    if r_multi_sum  != r_totall or len(r_multi)!=3:
        print('error','*'*60)

    print('reward: ', r)
