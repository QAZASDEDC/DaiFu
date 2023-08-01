def evaluate_daifu_cell_2():
    try:
        global args, corpus, data, data_source, eval_batch_size, hidden, i, ntokens, output, targets, torch, total_loss
        for i in range(0, data_source.size(0) - 1, args.bptt):
            try:
                daifu_return_tag, daifu_return_item = evaluate_daifu_cell_3()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = evaluate_daifu_rest_3()
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
    except Exception as evaluate_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
