def train_daifu_cell_2():
    try:
        global F, args, batch_idx, data, device, epoch, loss, model, optimizer, output, target, train_loader
        data = augment(data)
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        try:
            output = model(data)
            loss = F.nll_loss(output, target)
            loss.backward()
            optimizer.step()
            if batch_idx % args.log_interval == 0:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(epoch, batch_idx * len(data), len(train_loader.dataset), 100.0 * batch_idx / len(train_loader), loss.item()))
                if args.dry_run:
                    return 'break', None
        except:
            return None, None
    except Exception as train_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
