def test_daifu_cell_2():
    try:
        global F, correct, data, device, model, output, pred, print_val, target, test_loader, test_loss, torch
        for data, target in test_loader:
            try:
                daifu_return_tag, daifu_return_item = test_daifu_cell_3()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = test_daifu_rest_3()
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
    except Exception as test_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
