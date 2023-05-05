@daifu.with_goto
def main_daifu_rest_3():
    try:
        global batch_size, data, epoch, epochs, grads, itr, loss, model, np, optimizer, preds, tf, train_dataset, x, y
        goto .restart
        preds = model(data)
        grads, loss = compute_gradient(model, preds, data)
        print(grads)
        label .restart
        apply_gradients(optimizer, grads, model.variables)
    except Exception as main_exception_3:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
