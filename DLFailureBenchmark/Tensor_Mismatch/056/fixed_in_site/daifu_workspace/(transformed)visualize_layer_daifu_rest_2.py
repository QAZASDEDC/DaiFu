@daifu.with_goto
def visualize_layer_daifu_rest_2():
    try:
        global epochs, f, filter_lower, filter_range, filter_upper, img_loss, input_img, layer, layer_dict, layer_name, layers, model, output_dim, output_layer, processed_filters, step, upscaling_factor, upscaling_steps
        goto .restart
        label .restart
        img_loss = _generate_filter_image(input_img, output_layer.output, f)
        if img_loss is not None:
            processed_filters.append(img_loss)
    except Exception as visualize_layer_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
