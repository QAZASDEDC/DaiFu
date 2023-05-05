def main_daifu_cell_1():
    try:
        global criterion, epoch, net, nn, opt, optim, optimizer, test_dataloader, test_dataset, train_dataloader, train_dataset
        train_dataset = bAbIDataset(opt.dataroot, opt.question_id, True)
        train_dataloader = bAbIDataloader(train_dataset, batch_size=opt.batchSize, shuffle=True, num_workers=2)
        test_dataset = bAbIDataset(opt.dataroot, opt.question_id, False)
        test_dataloader = bAbIDataloader(test_dataset, batch_size=opt.batchSize, shuffle=False, num_workers=2)
        opt.annotation_dim = 1
        opt.n_edge_types = train_dataset.n_edge_types
        opt.n_node = train_dataset.n_node
        net = GGNN(opt)
        net.double()
        print(net)
        criterion = nn.CrossEntropyLoss()
        if opt.cuda:
            net.cuda()
            criterion.cuda()
        optimizer = optim.Adam(net.parameters(), lr=opt.lr)
        for epoch in range(0, opt.niter):
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
    except Exception as main_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
