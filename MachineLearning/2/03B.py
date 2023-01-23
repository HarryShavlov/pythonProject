Требуется реализовать на языке Python функцию, отображающую оценку плотности распределения столбца данных. Функция должна иметь следующий интерфейс


import pandas as pd
from typing import Union

def draw_pdf(data: pd.DataFrame, column: str, bins: Union[int, str] = 10) -> None:
    """
        Отображает оценку плотности распределения столбца данных

        Параметры:
            data: таблица данных.
            column: название столбца для отображения.
            bins: спецификация интервалов разбиения, аналогично matplotlib.pyplot.hist.
    """
    pass

import pandas as pd
from typing import Union
import matplotlib.pyplot as plt


def draw_pdf(data: pd.DataFrame, column: str, bins: Union[int, str] = 10) -> None:
    plt.xlim(data[column].min(), data[column].max())
    plt.hist(data[column], bins=bins, density=True, color='orange', label='Density', edgecolor='black')
    data[column].plot.kde(legend=True, title='', grid=True, label='KDE', color='black', linewidth=3)
    plt.legend(loc='upper right')
    plt.xlabel(data[column].name)
    plt.ylabel('')
    
data = pd.read_csv('data.csv')

plt.figure(figsize=(10, 5))
plt.rcParams.update({'font.size': 14})

draw_pdf(data, 'Account length', 'sturges')
plt.savefig('output.png')
