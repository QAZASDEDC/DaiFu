@daifu.with_goto
def main_daifu_rest_2():
    try:
        global args, best_val_loss, epoch, epoch_start_time, f, lr, math, model, test_data, test_loss, time, torch, val_data, val_loss
        goto .restart
        epoch_start_time = time.time()
        train()
        val_loss = evaluate(val_data)
        print('-' * 89)
        print('| end of epoch {:3d} | time: {:5.2f}s | valid loss {:5.2f} | valid ppl {:8.2f}'.format(epoch, time.time() - epoch_start_time, val_loss, math.exp(val_loss)))
        print('-' * 89)
        if not best_val_loss or val_loss < best_val_loss:
            label .restart
            with open(args.save, 'wb') as f:
                try:
                    daifu_return_tag, daifu_return_item = main_daifu_cell_3()
                except Exception:
                    while True:
                        try:
                            daifu.RP_MANAGER.repair()
                            daifu_return_tag, daifu_return_item = main_daifu_rest_3()
                            if daifu_return_tag is not None:
                                if daifu_return_tag == 'break':
                                    break
                                else:
                                    return daifu_return_tag, daifu_return_item
                            break
                        except Exception:
                            continue
            best_val_loss = val_loss
        else:
            lr /= 4.0
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
