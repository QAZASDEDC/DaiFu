@daifu.with_goto
def main_daifu_rest_1():
    try:
        global args, best_val_loss, corpus, criterion, device, epoch, epoch_start_time, eval_batch_size, f, lr, math, model, nn, ntokens, test_data, test_loss, time, torch, train_data, val_data, val_loss
        goto .restart
        eval_batch_size = 10
        train_data = batchify(corpus.train, args.batch_size)
        val_data = batchify(corpus.valid, eval_batch_size)
        test_data = batchify(corpus.test, eval_batch_size)
        ntokens = len(corpus.dictionary)
        if args.model == 'Transformer':
            model = model.TransformerModel(ntokens, args.emsize, args.nhead, args.nhid, args.nlayers, args.dropout).to(device)
        else:
            label .restart
            model = model.RNNModel(args.model, ntokens, args.emsize, args.nhid, args.nlayers, args.dropout, args.tied).to(device)
        criterion = nn.NLLLoss()
        lr = args.lr
        best_val_loss = None
        for epoch in range(1, args.epochs + 1):
            try:
                daifu_return_tag, daifu_return_item = main_daifu_cell_2()
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
        with open(args.save, 'rb') as f:
            try:
                daifu_return_tag, daifu_return_item = main_daifu_cell_4()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = main_daifu_rest_4()
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
        test_loss = evaluate(test_data)
        print('=' * 89)
        print('| End of training | test loss {:5.2f} | test ppl {:8.2f}'.format(test_loss, math.exp(test_loss)))
        print('=' * 89)
        if len(args.onnx_export) > 0:
            export_onnx(args.onnx_export, batch_size=1, seq_len=args.bptt)
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
