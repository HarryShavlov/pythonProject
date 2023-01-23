Требуется на языке Python реализовать функцию
get_busiest_states(data: pd.DataFrame)
Функция принимает на вход объект DataFrame и возвращает Series, отсортированный по убыванию, в котором штаты являются индексами, а значения — количеством международных звонков в данном штате.

Функция имеет следующий интерфейс


import pandas as pd

def get_busiest_states(data: pd.DataFrame) -> pd.Series:
    """
    Вычисляет Series, в котором индексы - наименования штатов, а значение - количество совершённых международных звонов. 

    Параметры:
      data: DataFrame с данными

    Возвращаемое значение:
      Series отсортированный по убыванию значений.
    """
    pass
import pandas as pd

def get_busiest_states(data: pd.DataFrame) -> pd.Series:
    states = data.groupby(['State'])['Total intl calls'].sum()
    return states.sort_values(ascending=False)

df = pd.read_csv('data.csv')
busiest_states = get_busiest_states(df)
      
