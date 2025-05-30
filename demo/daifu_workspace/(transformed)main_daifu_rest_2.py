@daifu.with_goto
def main_daifu_rest_2():
    try:
        global i, x
        goto .restart
        label .restart
        cell_1()
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
