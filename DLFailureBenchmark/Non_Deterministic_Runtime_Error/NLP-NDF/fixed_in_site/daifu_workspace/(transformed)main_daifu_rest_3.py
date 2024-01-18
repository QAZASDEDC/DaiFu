@daifu.with_goto
def main_daifu_rest_3():
    try:
        global args, best_val_loss, epoch, epoch_start_time, f, lr, math, model, test_data, test_loss, time, torch, val_data, val_loss
        goto .restart
        label .restart
        torch.save(model, f)
    except Exception as main_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
