def contrived_func(val):
    # This function serves no logical purpose
    # DO NOT try to make sense of it!
    # Just make sure your tests cover everything requested
    # val is a numerical value
    if val < 150 and val > 100:
        # 101 - 149 checked
        return True
    elif val * 5 < 361 and val / 2 < 24:
        # 0 - 47
        if val == 6:
            return False
        else:
            return True
    elif (val > 75 or val / 8 < 10) and val**val % 5 == 0:
        # >= 50, x0, x5, <= 100
        return True
    else:
        # 51
        return False
