from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import numpy as np
import grafs

class randforest:

    def __init__(self, data_x, data_y):
        self.data_x = data_x
        self.data_y = data_y
        self._random_forest()

    def _random_forest(self):

        get_generate_angle = open('files/gen_data_angle.txt')
        get_generate_fric = open('files/gen_data_fric.txt')
        get_generate_veter = open('files/gen_data_veter.txt')

        x_train = []
        x = 0
        with open('files/gen_data_speed.txt') as f:
            for speed in f:
                if x <= len(self.data_x)-1:
                    angle = float(get_generate_angle.readline())
                    fric = float(get_generate_fric.readline())
                    veter = float(get_generate_veter.readline())
                    x_train.append([float(speed), angle, fric, veter])
                x = x + 1

        # массив вида [1, 1, 0, 0]
        y_train = self.data_y
        clf_rf = RandomForestClassifier()

        X_train, X_test, Y_train, Y_test = train_test_split(x_train, y_train, test_size=0.2)
        clf_rf.fit(X_test, Y_test)

        importances = clf_rf.feature_importances_

        indices = np.argsort(importances)[::-1]
        names_indices = ['Скорость', 'Угол', 'Трение', 'Ветер']

        model = grafs.Paintgraf()
        model.show_importances(importances, indices, names_indices)

        print(clf_rf.predict(X_train))
        #print(clf_rf.predict([[20, 0.6, 1.3, 0.1]]))  # ручной ввод для теста
