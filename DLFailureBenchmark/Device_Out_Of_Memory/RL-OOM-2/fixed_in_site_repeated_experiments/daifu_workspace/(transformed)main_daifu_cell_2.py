def main_daifu_cell_2():
    try:
        global _, action, args, device, done, env, ep_reward, i_episode, model, print_val, reward, running_reward, state, t, torch
        state, _ = env.reset()
        ep_reward = 0
        for t in range(1, 10000):
            try:
                daifu_return_tag, daifu_return_item = main_daifu_cell_3()
                if daifu_return_tag is not None:
                    if daifu_return_tag == 'break':
                        break
                    else:
                        return daifu_return_tag, daifu_return_item
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = main_daifu_rest_3()
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
                if daifu_return_tag == 'break':
                    break
        running_reward = 0.05 * ep_reward + (1 - 0.05) * running_reward
        finish_episode()
        if i_episode % args.log_interval == 0:
            print('Episode {}\tLast reward: {:.2f}\tAverage reward: {:.2f}'.format(i_episode, ep_reward, running_reward))
        if running_reward > env.spec.reward_threshold:
            print('Solved! Running reward is now {} and the last episode runs to {} time steps!'.format(running_reward, t))
            print_val[0] = running_reward
            torch.save(model.state_dict(), 'checkpoint/actor_critic_policy.pt')
            return 'break', None
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
