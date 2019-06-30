import functions
import grafs
import randforest


class Classifield:

    gen_data = []

    def __init__(self, data):
        self._data = data
        self._prepare_data()

    def _prepare_data(self):

        get_generate_data = open('files/gen_data.txt')
        l_gen_data = []
        for line in get_generate_data:
            l_gen_data.append(int(line))

        l_key = []
        l_val = []
        val_for_train = []
        val_for_train_learn = []
        cont_ok = 0
        cont_non = 0

        for i in self._data:
            l_key.append(int(i))
            l_val.append(self._data[i])

        n = 0
        for val in l_gen_data:
            r = functions.nearest(l_key, val)
            d_effect = self._data[str(r)]
            if d_effect > 88:
                cont_ok = cont_ok + 1
                val_for_train_learn.append(1)
            else:
                cont_non = cont_non + 1
                val_for_train_learn.append(0)
            val_for_train.append(val)
            n = n + 1

        get_generate_data.close()
        randforest.randforest(val_for_train, val_for_train_learn)
