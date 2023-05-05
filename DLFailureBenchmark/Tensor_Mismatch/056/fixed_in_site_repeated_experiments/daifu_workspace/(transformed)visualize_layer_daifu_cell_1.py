def visualize_layer_daifu_cell_1():
    try:
        global epochs, f, filter_lower, filter_range, filter_upper, img_loss, input_img, layer, layer_dict, layer_name, layers, model, output_dim, output_layer, processed_filters, step, upscaling_factor, upscaling_steps
        """Visualizes the most relevant filters of one conv-layer in a certain model.

    # Arguments
        model: The model containing layer_name.
        layer_name: The name of the layer to be visualized.
                    Has to be a part of model.
        step: step size for gradient ascent.
        epochs: Number of iterations for gradient ascent.
        upscaling_steps: Number of upscaling steps.
                         Starting image is in this case (80, 80).
        upscaling_factor: Factor to which to slowly upgrade
                          the image towards output_dim.
        output_dim: [img_width, img_height] The output image dimensions.
        filter_range: Tupel[lower, upper]
                      Determines the to be computed filter numbers.
                      If the second value is `None`,
                      the last filter will be inferred as the upper boundary.
    """
        assert len(model.inputs) == 1
        input_img = model.inputs[0]
        layer_dict = dict([(layer.name, layer) for layer in model.layers[1:]])
        output_layer = layer_dict[layer_name]
        assert isinstance(output_layer, layers.Conv2D)
        filter_lower = filter_range[0]
        filter_upper = filter_range[1] if filter_range[1] is not None else len(output_layer.get_weights()[1])
        assert filter_lower >= 0 and filter_upper <= len(output_layer.get_weights()[1]) and filter_upper > filter_lower
        print('Compute filters {:} to {:}'.format(filter_lower, filter_upper))
        processed_filters = []
        for f in range(filter_lower, filter_upper):
            try:
                daifu_return_tag, daifu_return_item = visualize_layer_daifu_cell_2()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = visualize_layer_daifu_rest_2()
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
        print('{} filter processed.'.format(len(processed_filters)))
        _draw_filters(processed_filters)
    except Exception as visualize_layer_exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
