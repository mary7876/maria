УСР: https://drive.google.com/drive/folders/1l8QY_kDdoaSBi1c2Hx0tTQSnyd-aPFlX?usp=sharing

**1 Лабораторная**

### 1. Цель работы  
Цель данной работы — реализовать математическую модель роста популяции кроликов с использованием рекурсивного подхода. Задача основана на последовательности Фибоначчи, но с модификацией, учитывающей коэффициент размножения.  

### 2. Задачи  
- Изучить рекурсивный подход в программировании.  
- Реализовать функцию, вычисляющую количество пар кроликов через n месяцев с учетом коэффициента размножения k.  
- Обеспечить корректный ввод данных пользователем.  
- Протестировать программу на различных значениях n и k.  

### 3. Инструменты и алгоритмы 
Используемые инструменты:  
- Язык программирования: Python  
- Среда разработки: PyCharm 

### Алгоритм работы:  
1. Рекурсивная функция `rabbit_pairs(n, k)`  
   - Если n = 1 или n = 2, возвращается 1 (базовый случай).  
   - Иначе, вычисляется сумма:  
     - rabbit_pairs(n - 1, k) (количество пар в предыдущем месяце)  
     - k * rabbit_pairs(n - 2, k) (новые пары, появившиеся от пар, существовавших два месяца назад)  

2. Ввод данных  
   - Пользователь вводит:  
     - n — номер месяца.  
     - k — количество пар потомков, производимых одной парой кроликов каждый месяц.  

3. Вывод результата  
   - Программа выводит общее количество пар кроликов на n-й месяц.  

### 4. Ошибки и их исправления  
1. Рекурсия без базового случая  
   - Ошибка: Если не предусмотреть условие n == 1 or n == 2, рекурсия уйдет в бесконечный цикл.  
   - Исправление: Добавлены базовые случаи.  

2. Некорректный ввод данных  
   - Ошибка: Если пользователь введет нечисловые значения, программа завершится с ошибкой.  
   - Исправление: Можно добавить обработку исключений:  
          try:
         n = int(input("Введите номер месяца (n): "))
         k = int(input("Введите количество пар потомков (k): "))
     except ValueError:
         print("Ошибка: введите целые числа!")
         exit()

3. Низкая производительность при больших `n`  
   - Ошибка: Рекурсивный подход неэффективен для больших значений n (например, n > 35).  
   - Исправление: Можно использовать мемоизацию (кэширование результатов) или итеративный подход.

 ### 5. Выводы

 1. Корректность модели
- Программа корректно вычисляет количество пар кроликов на n-й месяц, учитывая коэффициент размножения k.
- Рекурсивный алгоритм, основанный на последовательности Фибоначчи, доказал свою эффективность для небольших значений n (n ≤ 30).
  
 2. Ограничения рекурсивного подхода
- При больших значениях n (n > 35) наблюдается значительное замедление работы программы из-за экспоненциальной сложности алгоритма.
- Для улучшения производительности рекомендуется использовать методы динамического программирования или итеративный подход.

3. Практическая значимость
- Модель может быть адаптирована для анализа других биологических процессов, например, роста бактерий или распространения заболеваний.
- Программа демонстрирует важность оптимизации алгоритмов при работе с рекурсивными вычислениями.
   
   ![image](https://github.com/user-attachments/assets/d7770200-6494-4e2f-b16f-c21c02e7fe50)


**2 Лабораторная**

#### 1. Цель работы
Разработка программы для поиска всех вхождений подстроки в строку с использованием метода последовательного сравнения символов.

#### 2. Задачи
1. Реализовать алгоритм поиска подстроки перебором всех возможных позиций
2. Обеспечить корректный ввод строки и подстроки от пользователя
3. Выявить и исправить ошибки в исходной реализации
4. Протестировать программу на различных наборах данных
5. Составить отчет о проведенной работе

#### 3. Инструменты и алгоритмы
**Используемые инструменты:**
- Язык программирования Python 3
- Среда разработки на выбор: PyCharm
- Метод тестирования - ручной прогон тестовых случаев

**Описание алгоритма:**
1. Получение на вход строки s и подстроки t
2. Последовательный перебор всех возможных начальных позиций подстроки:
   - Для каждого i от 0 до len(s)-len(t)
   - Сравнение подстроки s[i:i+len(t)] с t
3. Фиксация позиций совпадений (с нумерацией с 1)
4. Вывод результатов пользователю

#### 4. Ошибки и их исправления
1. Основная ошибка исходного кода:
   ```python
   positions.append(1+1)  # Ошибка: всегда добавляется 2
   ```
   Исправленная версия:
   ```python
   positions.append(i+1)  # Корректное добавление позиции
   ```

#### 5. Выводы
1. Разработанная программа корректно решает задачу поиска подстроки в строке, демонстрируя работу простейшего алгоритма.

2. Основные характеристики реализации:
   - Простота и наглядность кода
   - Корректная обработка различных входных данных
   - Понятные сообщения об ошибках ввода
   - Нумерация позиций с 1 для удобства пользователя

3. Практическое применение:
   - Учебное пособие по работе со строками
   - Демонстрация принципов алгоритмов поиска
   - Базовый код для более сложных модификаций
     
![image](https://github.com/user-attachments/assets/a9d4b4bb-d013-4e0b-b382-b863e2f00401)

  
  **3 Лабораторная**
№1

#### 1. Цель работы
Целью данной работы является создание диаграммы рассеяния для визуализации взаимосвязи между двумя признаками (sepal length и sepal width) в наборе данных Iris, с разделением точек по классам (видам ирисов).

#### 2. Задачи
1. Загрузить набор данных Iris из библиотеки scikit-learn
2. Выбрать два признака для анализа (длина и ширина чашелистика)
3. Создать диаграмму рассеяния с разделением по классам
4. Настроить визуальные параметры графика (цвета, подписи, легенду)
5. Отобразить график с помощью matplotlib

#### 3. Инструменты и алгоритмы
**Используемые инструменты:**
- Библиотека matplotlib.pyplot для визуализации
- Набор данных Iris из sklearn.datasets
- Язык программирования Python 3

**Описание алгоритма:**
1. Загрузка данных:
   - Загружается стандартный набор данных Iris
   - X содержит признаки 
   - y содержит метки классов 
   - feature_names и target_names содержат названия признаков и классов

2. Подготовка к визуализации:
   - Выбираются индексы признаков для осей x и y (0 и 1 - длина и ширина чашелистика)
   - Создается фигура размером 10×6 дюймов

3. Построение диаграммы:
   - Для каждого класса создается отдельный слой точек
   - Точки каждого класса окрашиваются в свой цвет (красный, зеленый, синий)
   - Добавляются прозрачность (alpha=0.7) и обводка (edgecolor='k')

4. Оформление графика:
   - Добавляются подписи осей (названия признаков)
   - Задается заголовок графика
   - Добавляется легенда с названиями классов
   - Включается сетка для удобства чтения значений

#### 4. Ошибки и их исправления

1. **Проблемы с пробелами и форматированием**:
   - Было: Несоответствие PEP 8 в количестве пробелов вокруг операторов
   - Исправление:
     ```python
     # Было:
     X[y==i,x_index]  # Отсутствие пробелов вокруг оператора
     plt.scatter(X[y == i, x_index],X[y == i, y_index],c=color)  # Неправильные пробелы
     
     # Стало:
     X[y == i, x_index]  # Пробелы вокруг оператора сравнения
     plt.scatter(X[y == i, x_index], X[y == i, y_index], c=color)  # Правильные пробелы
     ```

   - Было: Неправильные отступы в блоках кода
   - Исправление:
     ```python
     # Было:
     for i, color in zip(range(len(target_names)), colors):
     plt.scatter(...)  # Отсутствие отступа
     
     # Стало:
     for i, color in zip(range(len(target_names)), colors):
         plt.scatter(...)  # 4 пробела для отступа
     ```

2. **Проблемы с импортом библиотек**:
   - Было: Неполный импорт необходимых модулей
   - Исправление:
     ```python
     # Было:
     import matplotlib.pyplot
     
     # Стало:
     import matplotlib.pyplot as plt
     from sklearn.datasets import load_iris
     ```

3. **Проблемы с названиями переменных**:
   - Было: Использование заглавных букв в названиях переменных
   - Исправление:
     ```python
     # Было:
     Feature_names = iris.feature_names
     
     # Стало:
     feature_names = iris.feature_names  # Все буквы строчные по PEP 8
     ```
     

#### 5. Выводы
1. Программа успешно создает информативную диаграмму рассеяния, наглядно демонстрирующую:
   - Распределение двух признаков (длина и ширина чашелистика)
   - Разделение цветков по видам
   - Взаимосвязь между признаками для разных видов

2. Основные преимущества реализации:
   - Четкое визуальное разделение классов с помощью цвета
   - Хорошая читаемость благодаря подобранным параметрам визуализации
   - Полная информация о данных в подписях и легенде
   - Простота кода при хорошем результате

4. Практическое применение:
   - Быстрый анализ взаимосвязи признаков
   - Демонстрация разделимости классов
   - Пример визуализации для учебных целей
  
№2

#### 1. Цель работы
Целью данной работы является создание линейных графиков для анализа динамики трех ключевых макроэкономических показателей (реальный ВВП, реальное потребление и реальные государственные расходы) за период с 1990 по 2009 год.

#### 2. Задачи
1. Создать структурированный DataFrame с макроэкономическими данными
2. Подготовить временной ряд (20 лет) с примерными значениями показателей
3. Построить совмещенный линейный график динамики трех показателей
4. Настроить визуальные параметры для улучшения читаемости
5. Добавить необходимые элементы оформления (легенду, сетку, подписи)

#### 3. Инструменты и алгоритмы
**Используемые инструменты:**
- Библиотека pandas для работы с данными
- Библиотека matplotlib.pyplot для визуализации
- Язык программирования Python 3

**Описание алгоритма:**
1. Подготовка данных:
   - Создается диапазон лет (1990-2009)
   - Генерируются синтетические данные для трех показателей:
     * realgdp - реальный ВВП (возрастающий тренд с ускорением)
     * realcons - реальное потребление (аналогичный тренд, но с меньшими значениями)
     * realgovt - реальные госрасходы (более плавный тренд роста)
   - Данные структурируются в DataFrame

2. Построение графиков:
   - Создается фигура размером 12×6 дюймов
   - Для каждого показателя строится отдельная линия:
     * ВВП - с круговыми маркерами (marker='o')
     * Потребление - с квадратными маркерами (marker='s')
     * Госрасходы - с треугольными маркерами (marker='^')
   - Добавляются подписи для каждой линии через параметр label

3. Оформление графика:
   - Устанавливается заголовок с описанием содержания
   - Добавляются подписи осей (X - год, Y - значение показателя)
   - Включается сетка для удобства чтения значений
   - Добавляется легенда с описанием линий
   - Настраиваются метки на оси X (поворот на 45 градусов)
   - Применяется tight_layout() для оптимального размещения элементов

### 4. Ошибки и их исправления

1. **Отсутствие импорта необходимых библиотек**:
   - Было: В коде используется pandas и matplotlib, но импорт не указан
   - Исправление: Добавлены строки импорта в начале кода
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   ```

2. **Неправильные отступы в коде**:
   - Было: В некоторых местах использовались смешанные табуляции и пробелы
   - Исправление: Приведено к единообразию (4 пробела на уровень отступа)
   ```python
   # Неправильно:
   plt.plot(df['year'], df['realgdp'], label='Real GDP', marker='o')
       plt.title('Macroeconomic Indicators')
   
   # Правильно:
   plt.plot(df['year'], df['realgdp'], label='Real GDP', marker='o')
   plt.title('Macroeconomic Indicators')
   ```

3. **Неоптимальное использование методов pandas**:
   - Было: Прямое обращение к колонкам через df['column']
   - Улучшение: Использование точечной нотации где возможно
   ```python
   # Было:
   plt.plot(df['year'], df['realgdp'])
   
   # Стало:
   plt.plot(df.year, df.realgdp)
   ```

4. **Отсутствие обработки ошибок при построении графиков**:
   - Проблема: Нет проверки на существование колонок
   - Решение: Добавить проверку перед построением
   ```python
   required_columns = ['year', 'realgdp', 'realcons', 'realgovt']
   if not all(col in df.columns for col in required_columns):
       raise ValueError("DataFrame не содержит всех необходимых колонок")
   ```


#### 5. Выводы
1. Программа успешно создает информативный линейный график, позволяющий:
   - Сравнивать динамику трех макроэкономических показателей
   - Анализировать взаимосвязи между показателями
   - Выявлять общие тренды экономического развития

2. Основные преимущества реализации:
   - Четкое визуальное разделение показателей
   - Удобное сравнение динамики благодаря совмещенному графику
   - Полная информация о данных в подписях и легенде
   - Хорошая читаемость благодаря подобранным параметрам

3. Практическое применение:
   - Демонстрация принципов работы с временными рядами
   - Шаблон для визуализации реальных экономических данных
   - Учебный пример для анализа макроэкономических трендов


![image](https://github.com/user-attachments/assets/5d479ba0-3e0d-46fc-9054-ade29b75123e)

![image](https://github.com/user-attachments/assets/4b7b157a-0979-453e-93f0-aa55dd033616)


**4 Лабораторная**

#### 1. Цель работы
Разработка Python-скриптов для анализа биологических последовательностей в формате GenBank без оптимизации производительности, с акцентом на выявление потенциальных ошибок.

#### 2. Задачи
1. Реализовать чтение GenBank-файлов
2. Рассчитать GC-состав последовательностей
3. Выполнить трансляцию CDS-регионов
4. Выявить возможные ошибки в реализации
5. Подробно описать алгоритмы работы

#### 3. Инструменты и алгоритмы

**Используемые библиотеки:**
```python
from Bio import SeqIO  # Основная библиотека для работы с GenBank
from Bio.Seq import Seq  # Для операций с последовательностями
```

**Алгоритм расчета GC-состава:**
1. Получить последовательность из записи GenBank
2. Привести последовательность к верхнему регистру
3. Посчитать количество нуклеотидов G и C
4. Разделить сумму G+C на общую длину последовательности
5. Вернуть результат в диапазоне 0-1

**Алгоритм трансляции CDS:**
1. Для каждой записи GenBank:
   a. Найти все особенности типа "CDS"
   b. Для каждой CDS:
      i. Извлечь последовательность с учетом экзонов
      ii. Учесть направление цепи (прямая/обратная)
      iii. Применить рамку считывания (codon_start)
      iv. Выполнить трансляцию по указанной таблице
      v. Остановиться при встрече стоп-кодона
   c. Сохранить результаты трансляции

#### 4. Потенциальные ошибки и их последствия

1. **Ошибка в пути к файлу:**
   - Пример ошибки:
     ```python
     file_path = "C:\Users\user\newfolder\sequence.gb"  # Необработанные спецсимволы
     ```
   - Последствия: SyntaxError из-за неверного escaping
   - Как избежать: Использовать сырые строки или двойные слеши

2. **Ошибка обработки последовательности:**
   - Пример ошибки:
     ```python
     sequence = record.seq  # Без преобразования в строку
     sequence.count('G')  # Ошибка для объектов Seq
     ```
   - Последствия: AttributeError
   - Как избежать: Явное преобразование: `str(record.seq)`

3. **Ошибка в расчете GC-состава:**
   - Пример ошибки:
     ```python
     gc_count = sequence.count('G') + sequence.count('C')
     total = len(sequence) or 1  # Деление на ноль
     ```
   - Последствия: ZeroDivisionError для пустых последовательностей
   - Как избежать: Проверка длины последовательности

4. **Ошибка обработки CDS:**
   - Пример ошибки:
     ```python
     codon_start = feature.qualifiers["codon_start"][0]  # Без try-except
     ```
   - Последствия: KeyError при отсутствии qualifier
   - Как избежать: Использовать .get() с значением по умолчанию

5. **Ошибка трансляции:**
   - Пример ошибки:
     ```python
     protein_seq = Seq(cds_seq).translate(to_stop=False)
     ```
   - Последствия: Белки со стоп-кодонами внутри
   - Как избежать: Всегда использовать to_stop=True

6. **Ошибка вывода результатов:**
   - Пример ошибки:
     ```python
     print(f"{record_id}: {description}, GC = {gc_content}%")  # Не форматировано
     ```
   - Последствия: Длинные числа с множеством знаков
   - Как избежать: Форматирование: `{gc_content:.2f}%`

### 5. Выводы

1. **Основные результаты**:
   - Успешно реализованы функции для анализа GC-состава и трансляции CDS-регионов
   - Обеспечена корректная обработка биологических особенностей (альтернативные таблицы трансляции, обратные цепи ДНК)


2. **Практическое применение кода**:

1. Анализ состава геномов:
   - Сравнение GC-состава разных видов бактерий
   - Выявление горизонтального переноса генов
2. Контроль качества данных:
   - Проверка сборки геномов
   - Обнаружение загрязнений в образцах
3. **Аннотация генов**:
   - Верификация предсказанных CDS-регионов
   - Проверка рамок считывания
4. Эволюционные исследования:
   - Анализ мутационных предпочтений
   - Изучение давления отбора на кодоны
5. Биотехнологические приложения:
   - Оптимизация генов для экспрессии
   - Подбор специфичных праймеров
6. Образовательные цели:
   - Демонстрация работы с биологическими данными
   - Обучение основам биоинформатики
7. Медицинская диагностика:
   - Идентификация патогенов по GC-профилю
   - Анализ мутаций в клинических изолятах

![image](https://github.com/user-attachments/assets/87915026-bb3a-4f26-9944-13ab7e9881f6)
![image](https://github.com/user-attachments/assets/6ac366d8-1513-4543-97de-d13a68913d73)
![image](https://github.com/user-attachments/assets/a22c9c05-9c8f-4314-9c29-ab0a2fd6182b)

