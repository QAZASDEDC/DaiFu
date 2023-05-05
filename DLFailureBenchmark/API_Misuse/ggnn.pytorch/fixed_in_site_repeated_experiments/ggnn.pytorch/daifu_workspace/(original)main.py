@daifu.transform(globals())
def main(opt):
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
        train(epoch, train_dataloader, net, criterion, optimizer, opt)
        test(test_dataloader, net, criterion, optimizer, opt)
