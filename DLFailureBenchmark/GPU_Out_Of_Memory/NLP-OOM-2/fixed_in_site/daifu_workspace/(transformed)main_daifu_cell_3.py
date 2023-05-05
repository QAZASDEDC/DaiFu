def main_daifu_cell_3():
    try:
        global args, best_val_loss, corpus, criterion, device, epoch, epoch_start_time, eval_batch_size, f, lr, math, model, nn, ntokens, test_data, test_loss, time, torch, train_data, val_data, val_loss
        torch.save(model, f)
    except Exception as main_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
