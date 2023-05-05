@daifu.transform(globals())
def visualize_layer(model, layer_name, step=1.0, epochs=15, upscaling_steps=9, upscaling_factor=1.2, output_dim=(412, 412), filter_range=(0, None)):
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
        img_loss = _generate_filter_image(input_img, output_layer.output, f)
        if img_loss is not None:
            processed_filters.append(img_loss)
    print('{} filter processed.'.format(len(processed_filters)))
    _draw_filters(processed_filters)
