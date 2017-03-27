__author__ = 'Alexander'
# Обеспечим совместимость с Python 2 и 3
# pip install future
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

# отключим предупреждения Anaconda
import warnings
warnings.simplefilter('ignore')

# импортируем Pandas и Numpy
import pandas as pd
import numpy as np

#По умолчанию Pandas выводит всего 20 столбцов и 60 строк, поэтому если ваш датафрейм больше, воспользуйтесь функцией set_option:
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

#НАЧАЛО РАБОТЫ
df = pd.read_csv('../../data/telecom_churn.csv')
df.head()#начало таблицы
print(df.shape)#размер
print(df.columns)#список колонок
print(df.info())#полная информация

#Изменить тип колонки можно с помощью метода astype. Применим этот метод к признаку Churn и переведём его в int64:
df['Churn'] = df['Churn'].astype('int64')
df.describe() #показывает основные статистические характеристики данных по каждому числовому признаку (типы int64 и float64)
#Чтобы посмотреть статистику по нечисловым признакам, нужно явно указать интересующие нас типы в параметре include.
df.describe(include=['object', 'bool'])
#Для категориальных (тип object) и булевых (тип bool) признаков можно воспользоваться методом value_counts.
df['Churn'].value_counts()
#Укажем значение параметра normalize=True, чтобы посмотреть не абсолютные частоты, а относительные.
df['Area code'].value_counts(normalize=True)

#СОРТИРОВКА
df.sort_values(by='Total day charge', ascending=False).head()
df.sort_values(by=['Churn', 'Total day charge'], ascending=[True, False]).head()

#ИНДЕКСАЦИЯ
df['Churn'].mean()
df[df['Churn'] == 1].mean()
df[df['Churn'] == 1]['Total day minutes'].mean()
df[(df['Churn'] == 0) & (df['International plan'] == 'No')]['Total intl minutes'].max()
#Датафреймы можно индексировать как по названию столбца или строки, так и по порядковому номеру.
# Для индексации по названию используется метод loc, по номеру — iloc.
df.loc[0:5, 'State':'Area code']
df.iloc[0:5, 0:3]

#ПРИМЕНЕНИЕ ФУНКЦИИ
df.apply(np.max)
#Метод apply можно использовать и для того, чтобы применить функцию к каждой строке. Для этого нужно указать axis=1.
#Метод map можно использовать для замены значений в колонке, передав ему в качестве аргумента словарь вида {old_value: new_value}:
d = {'No' : False, 'Yes' : True}
df['International plan'] = df['International plan'].map(d)
#Аналогичную операцию можно провернуть с помощью метода replace:
df = df.replace({'Voice mail plan': d})
df.head()

#ГРУППИРОВКА ДАННЫХ
df.groupby(by=grouping_columns)[columns_to_show].function() #в общем случае
columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']
df.groupby(['Churn'])[columns_to_show].describe(percentiles=[])
#Сделаем то же самое, но немного по-другому, передав в agg список функций:
columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']
df.groupby(['Churn'])[columns_to_show].agg([np.mean, np.std, np.min, np.max])

#СВОДНЫЕ ТАБЛИЦЫ
pd.crosstab(df['Churn'], df['International plan'])
pd.crosstab(df['Churn'], df['Voice mail plan'], normalize=True)
#В Pandas за сводные таблицы отвечает метод pivot_table, который принимает в качестве параметров:
# values – список переменных, по которым требуется рассчитать нужные статистики,
# index – список переменных, по которым нужно сгруппировать данные,
# aggfunc — то, что нам, собственно, нужно посчитать по группам — сумму, среднее, максимум, минимум или что-то ещё.
df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'], ['Area code'], aggfunc='mean').head(10)

#ПРЕОБРАЗОВАНИЕ ДАТАФРЕИМОВ
total_calls = df['Total day calls'] + df['Total eve calls'] + df['Total night calls'] + df['Total intl calls']
df.insert(loc=len(df.columns), column='Total calls', value=total_calls)
# loc - номер столбца, после которого нужно вставить данный Series
# мы указали len(df.columns), чтобы вставить его в самом конце

#Добавить столбец из имеющихся можно и проще, не создавая промежуточных Series:
df['Total charge'] = df['Total day charge'] + df['Total eve charge'] + df['Total night charge'] + df['Total intl charge']
#Чтобы удалить столбцы или строки, воспользуйтесь методом drop, передавая в качестве аргумента нужные индексы
# и требуемое значение параметра axis (1, если удаляете столбцы, и ничего или 0, если удаляете строки):
df = df.drop(['Total charge', 'Total calls'], axis=1) # избавляемся от созданных только что столбцов
df.drop([1, 2]).head() # а вот так можно удалить строчки