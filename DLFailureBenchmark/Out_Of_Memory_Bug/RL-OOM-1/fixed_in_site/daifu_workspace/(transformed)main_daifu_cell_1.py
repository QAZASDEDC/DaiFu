def main_daifu_cell_1():
    try:
        global _, action, args, device, done, env, ep_reward, i_episode, model, reward, running_reward, state, t, torch
        model.to(device)
        running_reward = 10
        for i_episode in count(1):
            try:
                daifu_return_tag, daifu_return_item = main_daifu_cell_2()
                if daifu_return_tag is not None:
                    if daifu_return_tag == 'break':
                        break
                    else:
                        return daifu_return_tag, daifu_return_item
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = main_daifu_rest_2()
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
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
