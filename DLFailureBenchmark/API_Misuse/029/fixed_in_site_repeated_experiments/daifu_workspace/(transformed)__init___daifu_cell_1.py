def __init___daifu_cell_1():
    try:
        global json_file, loaded_model_json, model_json_file, model_weights_file, self
        with open(model_json_file, 'r') as json_file:
            try:
                daifu_return_tag, daifu_return_item = __init___daifu_cell_2()
            except Exception:
                while True:
                    try:
                        daifu.RP_MANAGER.repair()
                        daifu_return_tag, daifu_return_item = __init___daifu_rest_2()
                        if daifu_return_tag is not None:
                            if daifu_return_tag == 'break':
                                break
                            else:
                                return daifu_return_tag, daifu_return_item
                        break
                    except Exception:
                        continue
        self.loaded_model.load_weights(model_weights_file)
        self.loaded_model.make_predict_function()
        daifu.log_program_end()
    except Exception as __init___exception_1:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
