Требуется на языке Python реализовать функцию
join_dataframes(users_df: pd.DataFrame, states_df: pd.DataFrame)
Функция принимает на вход два объекта DataFrame и возвращает объединённый DataFrame пользователей и штатов.

Функция имеет следующий интерфейс


import pandas as pd

def join_dataframes(data: pd.DataFrame, states: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает объединённый DataFrame

    Параметры:
      data: DataFrame с пользователями
      states: DataFrame с штатами

    Возвращаемое значение:
      объединённый DataFrame, содержащий поля 'Total day calls', 'Total night calls', 'State' в данном порядке
    """
    pass

import pandas as pd


def join_dataframes(data: pd.DataFrame, states: pd.DataFrame):

    merged_df = pd.merge(data, states, on='ID')
    merged_df = merged_df.loc[:, ['Total day calls', 'Total night calls', 'State']]
    return merged_df

states = pd.read_csv('states.csv', index_col='ID')
data = pd.read_csv('data.csv', index_col='ID')
joined_df = join_dataframes(data, states)
