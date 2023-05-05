def main_daifu_cell_3():
    try:
        global batch_size, data, epoch, epochs, grads, itr, loss, model, np, optimizer, preds, tf, train_dataset, x, y
        preds = model(data)
        grads, loss = compute_gradient(model, preds, data)
        print(grads)
        apply_gradients(optimizer, grads, model.variables)
    except Exception as main_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
