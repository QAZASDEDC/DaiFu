def evaluate_daifu_cell_1():
    try:
        global args, corpus, data, data_source, eval_batch_size, hidden, i, ntokens, output, targets, torch, total_loss
        model.eval()
        total_loss = 0.0
        ntokens = len(corpus.dictionary)
        if args.model != 'Transformer':
            hidden = model.init_hidden(eval_batch_size)
        with torch.no_grad():
            try:
                daifu_return_tag, daifu_return_item = evaluate_daifu_cell_2()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = evaluate_daifu_rest_2()
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
        return 'evaluate_daifu_cell_1', total_loss / (len(data_source) - 1)
    except Exception as evaluate_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
