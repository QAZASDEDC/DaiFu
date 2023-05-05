def test_daifu_cell_1():
    try:
        global adj_matrix, annotation, correct, criterion, dataloader, i, init_input, net, opt, optimizer, output, padding, pred, print_val, target, test_loss, torch
        test_loss = 0
        correct = 0
        net.eval()
        for i, (adj_matrix, annotation, target) in enumerate(dataloader, 0):
            try:
                daifu_return_tag, daifu_return_item = test_daifu_cell_2()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = test_daifu_rest_2()
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
        test_loss /= len(dataloader.dataset)
        print('Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)'.format(test_loss, correct, len(dataloader.dataset), 100.0 * correct / len(dataloader.dataset)))
        print_val[0] = 100.0 * correct / len(dataloader.dataset)
    except Exception as test_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
