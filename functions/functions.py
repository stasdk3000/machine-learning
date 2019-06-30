import numpy as np
def save_lumbda_speed(speed, fric, angle, veter):
    S = 0.25  # площадь поперечного сечения транспортного средства (лобовая площадь ТС)
    g = 9.8  # ускорение свободного падения
    m = 230  # масса
    kb = 0.1  # коэффициент сопротивления воздуха

    NV = (kb * S * (speed + veter) ** 2 * speed) / 1000  # мощность преодоления сил ветра
    ND = (fric * m * g * speed) / 1000  # мощность преодоления сил дороги
    NP = (speed * m * g * np.sin(np.radians(angle))) / 1000  # мощность преодоления сил сопротивления подъема
    if angle > 0:
        NK = (speed * ((115 + speed) / 10000) * m * g * np.cos(
            np.radians(angle))) / 1000  # мощность преодоления сил сопротивления качению
    else:
        NK = 0

    N = NV + ND + NP + NK
    return N


def nearest(lst, target):
    return min(lst, key=lambda x: abs(x-target))


def middle_val_list(val):
    res = sum(val) / float(len(val))
    return res