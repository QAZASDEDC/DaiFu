def test_daifu_cell_2():
    try:
        global adj_matrix, annotation, correct, criterion, dataloader, i, init_input, net, opt, optimizer, output, padding, pred, target, test_loss, torch
        padding = torch.zeros(len(annotation), opt.n_node, opt.state_dim - opt.annotation_dim).double()
        init_input = torch.cat((annotation, padding), 2)
        if opt.cuda:
            init_input = init_input.cuda()
            adj_matrix = adj_matrix.cuda()
            annotation = annotation.cuda()
            target = target.cuda()
        init_input = Variable(init_input)
        adj_matrix = Variable(adj_matrix)
        annotation = Variable(annotation)
        target = Variable(target)
        output = net(init_input, annotation, adj_matrix)
        test_loss += criterion(output, target).data.item()
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()
    except Exception as test_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
