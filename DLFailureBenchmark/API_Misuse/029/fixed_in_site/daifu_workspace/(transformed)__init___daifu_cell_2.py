def __init___daifu_cell_2():
    try:
        global json_file, loaded_model_json, model_json_file, model_weights_file, self
        loaded_model_json = json_file.read()
        self.loaded_model = model_from_json(loaded_model_json)
    except Exception as __init___exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
