import numpy as np
import functions
import tools
import grafs

class Generator:
    m_speed = 0  # среднее значение скорости
    sigma_speed = 0  # стандартное отклонение значение
    mu_angle = 0  # среднее значение угла наклона
    sigma_angle = 0  # стандартное отклонение значение
    mu_trenie = 0  # среднее значение коэффициента трения
    sigma_trenie = 0  # стандартное отклонение значение

    count_step = 50000
    count_range = 50000

    def __init__(self, mu_speed, sigma_speed, mu_angle, sigma_angle, mu_trenie, sigma_trenie, mu_veter, sigma_veter):
        self.mu_speed = mu_speed
        self.mu_angle = mu_angle
        self.mu_trenie = mu_trenie
        self.mu_veter = mu_veter
        self.sigma_speed = sigma_speed
        self.sigma_angle = sigma_angle
        self.sigma_trenie = sigma_trenie
        self.sigma_veter = sigma_veter
        self._gen_arrays()

    def _gen_arrays(self):
        speed_array = []
        friction_array = []
        angle_array = []
        veter_array = []

        speed = self.mu_speed + self.sigma_speed * np.random.randn(self.count_step)
        angle = self.mu_angle + self.sigma_angle * np.random.randn(self.count_step)
        friction = self.mu_trenie + self.sigma_trenie * np.random.randn(self.count_step)
        veter = self.mu_veter + self.sigma_veter * np.random.randn(self.count_step)

        tools.write_to_file('files/gen_data_speed.txt', speed)
        tools.write_to_file('files/gen_data_angle.txt', angle)
        tools.write_to_file('files/gen_data_fric.txt', friction)
        tools.write_to_file('files/gen_data_veter.txt', veter)

        #graf = grafs.Paintgraf()
        #graf.show_hist(speed, self.mu_speed, self.sigma_speed)

        for (i, item) in enumerate(speed):
            speed_array.append(item)

        for (i, item) in enumerate(friction):
            friction_array.append(item)

        for (i, item) in enumerate(angle):
            angle_array.append(item)

        for (i, item) in enumerate(veter):
            veter_array.append(item)

        self._math_array(speed_array, friction_array, angle_array, veter_array)

    def _math_array(self, speed_array, friction_array, angle_array, veter_array):

        file = open('files/gen_data.txt', 'w')

        for i in range(1, self.count_range):
            speed = float("{0:.4f}".format(speed_array[i]))
            fric = float("{0:.4f}".format(friction_array[i]))
            angle = float("{0:.4f}".format(angle_array[i]))
            veter = float("{0:.4f}".format(veter_array[i]))

            speed = speed * 1000 / 3600

            N = functions.save_lumbda_speed(speed, fric, angle, veter)

            file.write(str((int(float("{0:.4f}".format(N * 1000)))))+'\n')

        file.close()
