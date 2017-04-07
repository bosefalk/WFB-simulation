
def to_hit(WS_att, WS_def):

    diff = WS_att - WS_def
    if diff > 0:
        success_roll = 3
        return success_roll;
    if diff < 2 * WS_att:
        success_roll = 5
        return success_roll;
    else:
        success_roll = 4
        return success_roll;


def to_wound(S_att, T_def):
    diff = S_att - T_def
    if diff >= 2:
        success_roll = 2
        return success_roll;
    if diff == 1:
        success_roll = 3
        return success_roll;
    if diff == 0:
        success_roll = 4
        return success_roll;
    if diff == -1:
        success_roll = 5
        return success_roll;
    if diff <= -2:
        success_roll = 6
        return success_roll;


def armour_save(S_att, save):
    # Armour save is lowered (higher roll needed to save) by every point S > 3
    lower = S_att - 3
    if lower < 0:
        lower = 0
    success_roll = save + lower
    return success_roll;
