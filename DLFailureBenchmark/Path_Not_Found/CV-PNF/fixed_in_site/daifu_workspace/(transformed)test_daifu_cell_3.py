def test_daifu_cell_3():
    try:
        global F, correct, data, device, model, output, pred, target, test_loader, test_loss, torch
        data, target = data.to(device), target.to(device)
        output = model(data)
        test_loss += F.nll_loss(output, target, reduction='sum').item()
        pred = output.argmax(dim=1, keepdim=True)
        correct += pred.eq(target.view_as(pred)).sum().item()
    except Exception as test_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
