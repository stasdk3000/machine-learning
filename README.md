# machine-learning
Python machine learning for electromoto project

## Данный проект разрабатывался для информационно-аналитического модуля для блока управления электродвигателя

В частности для проекта электромотоцикла, созданного на базе СФУ.

**Цель — найти и проверить способ оптимизации потребления батареи электродвигателем.**

![Image moto](https://github.com/stasdk3000/machine-learning/blob/master/img/moto.png)


## Принцип действия

>Мощность двигателя вычисляется сложением таких составляющих как сопротивление дороги, сопротивление подъема, сопротивление ветра. Данные параметры собираются датчиками на электромотоцикле.

График зависимости эффективности работы электродвигателя от выделяемой мощности (в проекте используется электромотор golden motor). 
Визуально виден диапазон эффективных величин, по оси Х мощность, по оси Y эффективность. Зеленой зоной отмечана зона эффективности которую мы берем за положительную и целевую.

![Image grafic](https://github.com/stasdk3000/machine-learning/blob/master/img/grafik.png)

Генерируем тестовые данные для входящих параметров. Набор параметров имеет вид { sigmaX, sigmaY, sigmaZ, sigmaT }

Данные генерируеются с показателями для городской местности и для холмистой, загородной местности.

```python
gen_city = generator.Generator(50, 30, 4, 2, 0.015, 0.009, 4, 10)
```
или
```python
gen_outcity = generator.Generator(35, 5, 8, 3, 0.025, 0.009, 2, 5)
```

Получаем результат, для примера выводятся графики в таком виде:

![Image grafic2](https://github.com/stasdk3000/machine-learning/blob/master/img/grafik2.png)
![Image grafic3](https://github.com/stasdk3000/machine-learning/blob/master/img/grafik3.png)

Полученные данные классифицируются, основываясь на таблицу эффективности электродвигателя.

Повторяем алгоритм 10 раз и в результате каждого повторения классификации наблюдаются зависимости. Таблицы с результатами для двух наборов тестовых данных:

>В каждом тесте 50000 сгенерированных параметров для моделирования движения по городской местности

номер | кол. неэффективных | кол. эффективных
----- | ------------------ | ----------------
1 | 26520 | 23479
2 | 26431 | 23568
3 | 26276 | 23723
4 | 26542 | 23457
5 | 26404 | 23595
6 | 26466 | 23533
7 | 26516 | 23483
8 | 26615 | 23384
9 | 26576 | 23423
10 | 26307 | 23692

>В каждом тесте 50000 сгенерированных параметров для моделирования движения по холмистой местности 

номер | кол. неэффективных | кол. эффективных
----- | ------------------ | ----------------
1 | 17877 | 32122
2 | 17832 | 32167
3 | 17687 | 32312
4 | 17817 | 32182
5 | 17786 | 32213
6 | 17900 | 32099
7 | 17760 | 32239
8 | 18001 | 31998
9 | 17901 | 32098
10 | 17878 | 32121

Данные результаты используем для обучения по методу Random forest, используется библиотека sklearn. 

В результате реализованный метод можно использовать для проверки эффективности движения выбранного электротранспорта по заданному заранее маршруту. Или, при использовании, датчиков ассистировать водителя о текущей эффективности при движении, уведомление с подсказками как двигаться для экономии заряда