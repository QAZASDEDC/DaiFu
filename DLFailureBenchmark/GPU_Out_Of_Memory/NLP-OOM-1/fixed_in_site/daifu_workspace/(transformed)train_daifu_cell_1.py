def train_daifu_cell_1():
    try:
        global args, batch, corpus, cur_loss, data, elapsed, epoch, hidden, i, loss, lr, math, ntokens, output, p, start_time, targets, time, torch, total_loss, train_data
        model.train()
        total_loss = 0.0
        start_time = time.time()
        ntokens = len(corpus.dictionary)
        if args.model != 'Transformer':
            hidden = model.init_hidden(args.batch_size)
        for batch, i in enumerate(range(0, train_data.size(0) - 1, args.bptt)):
            try:
                daifu_return_tag, daifu_return_item = train_daifu_cell_2()
                if daifu_return_tag is not None:
                    if daifu_return_tag == 'break':
                        break
                    else:
                        return daifu_return_tag, daifu_return_item
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = train_daifu_rest_2()
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
    except Exception as train_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
