def main_daifu_cell_2():
    try:
        global criterion, epoch, net, nn, opt, optim, optimizer, test_dataloader, test_dataset, train_dataloader, train_dataset
        train(epoch, train_dataloader, net, criterion, optimizer, opt)
        test(test_dataloader, net, criterion, optimizer, opt)
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
