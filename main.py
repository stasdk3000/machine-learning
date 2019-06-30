import generator
import datamining
import table_golden_motor

# входные данные для генератора тестовых данных
gen = generator.Generator(50, 30, 4, 2, 0.015, 0.009, 4, 10)
# gen = generator.Generator(35, 5, 8, 3, 0.025, 0.009, 2, 5)
# получаем данные с таблицы производителя
data = table_golden_motor.data
# отправляем данные на обработку
classifield = datamining.Classifield(data)
