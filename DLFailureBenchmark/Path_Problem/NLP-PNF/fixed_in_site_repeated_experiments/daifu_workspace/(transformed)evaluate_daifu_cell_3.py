def evaluate_daifu_cell_3():
    try:
        global args, corpus, data, data_source, eval_batch_size, hidden, i, ntokens, output, targets, torch, total_loss
        data, targets = get_batch(data_source, i)
        if args.model == 'Transformer':
            output = model(data)
            output = output.view(-1, ntokens)
        else:
            output, hidden = model(data, hidden)
            hidden = repackage_hidden(hidden)
        total_loss += len(data) * criterion(output, targets).item()
    except Exception as evaluate_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
