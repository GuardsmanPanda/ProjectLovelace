def survive(a, donated_blood):
    for b in donated_blood:
        if a[-1] == '-' and b[-1] != '-':
            continue
        if len(a) == 3 or b[0] == 'O' or a[0] == b[0]:
            return True
    return False