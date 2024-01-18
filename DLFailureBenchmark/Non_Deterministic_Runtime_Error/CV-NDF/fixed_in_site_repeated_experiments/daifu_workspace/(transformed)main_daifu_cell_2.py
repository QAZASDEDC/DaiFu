def main_daifu_cell_2():
    try:
        global argparse, args, cuda_kwargs, dataset1, dataset2, datasets, device, epoch, model, optim, optimizer, parser, scheduler, test_kwargs, test_loader, torch, train_kwargs, train_loader, transform, transforms, use_cuda, use_mps
        train(args, model, device, train_loader, optimizer, epoch)
        test(model, device, test_loader)
        scheduler.step()
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
