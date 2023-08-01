def test_daifu_cell_1():
    try:
        global F, correct, data, device, model, output, pred, target, test_loader, test_loss, torch
        model.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
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
        test_loss /= len(test_loader.dataset)
        print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(test_loss, correct, len(test_loader.dataset), 100.0 * correct / len(test_loader.dataset)))
    except Exception as test_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
