def train_daifu_cell_3():
    try:
        global args, batch, corpus, cur_loss, data, elapsed, epoch, hidden, i, loss, lr, math, ntokens, output, p, start_time, targets, time, torch, total_loss, train_data
        p.data.add_(p.grad, alpha=-lr)
    except Exception as train_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
