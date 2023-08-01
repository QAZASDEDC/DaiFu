def main_daifu_cell_3():
    try:
        global _, action, args, done, env, ep_reward, i_episode, model, print_val, reward, running_reward, state, t, torch
        action = select_action(state)
        state, reward, done, _, _ = env.step(action)
        if args.render:
            env.render()
        model.rewards.append(reward)
        ep_reward += reward
        if done:
            return 'break', None
    except Exception as main_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
