def main_daifu_cell_2():
    try:
        global i, x
        cell_1()
    except Exception as main_exception_2:
        daifu.CT_MANAGER.save(locals())
        raise
    else:
        return None, None
