@daifu.transform(globals())
def visualize_layer(model, layer_name, step=1.0, epochs=15, upscaling_steps=9, upscaling_factor=1.2, output_dim=(412, 412), filter_range=(0, 5)):
    daifu_store = {}
    for daifu_dataname in daifu.TRANSFORM_REGISTRY['visualize_layer']['dataname_list']:
        if daifu_dataname in globals():
            daifu_store[daifu_dataname] = globals()[daifu_dataname]
        if daifu_dataname in locals():
            globals()[daifu_dataname] = locals()[daifu_dataname]
        elif daifu_dataname not in globals():
            globals()[daifu_dataname] = None
    try:
        daifu_return_tag, daifu_return_item = visualize_layer_daifu_cell_1()
    except Exception:
        while True:
            try:
                daifu.RP_MANAGER.repair()
                daifu_return_tag, daifu_return_item = visualize_layer_daifu_rest_1()
                break
            except Exception:
                continue
    for daifu_dataname in daifu_store:
        globals()[daifu_dataname] = daifu_store[daifu_dataname]
