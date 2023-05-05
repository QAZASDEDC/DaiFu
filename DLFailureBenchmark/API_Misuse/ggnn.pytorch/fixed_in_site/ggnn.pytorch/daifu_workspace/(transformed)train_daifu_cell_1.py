def train_daifu_cell_1():
    try:
        global adj_matrix, annotation, criterion, dataloader, epoch, i, init_input, loss, net, opt, optimizer, output, padding, target, torch
        net.train()
        for i, (adj_matrix, annotation, target) in enumerate(dataloader, 0):
            try:
                daifu_return_tag, daifu_return_item = train_daifu_cell_2()
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
