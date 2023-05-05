def train_daifu_cell_2():
    try:
        global adj_matrix, annotation, criterion, dataloader, epoch, i, init_input, loss, net, opt, optimizer, output, padding, target, torch
        net.zero_grad()
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
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if i % int(len(dataloader) / 10 + 1) == 0 and opt.verbal:
            print('[%d/%d][%d/%d] Loss: %.4f' % (epoch, opt.niter, i, len(dataloader), loss.data[0]))
    except Exception as train_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
