Требуется на языке Python реализовать функцию
get_businessmen(df: pd.DataFrame)
Функция принимает на вход объект DataFrame библиотеки Pandas и возвращает DataFrame пользователей, совершивших 20 и более международных звонков.

В объекте DataFrame присутствуют следующие поля:

ID — идентификатор пользователя, целое уникальное число
Total day minutes — сумма минут дневных звонков, вещественное число
Total day calls — количество дневных звонков, целое число
Total night minutes — сумма минут ночных звонков, вещественное число
Total night calls — количество ночных звонков, целое число
Total intl minutes — сумма минут международных звонков, вещественное число
Total intl calls — количество международных звонков, целое число
Customer service calls — количество обращений в техническую поддержку, целое число
Функция имеет следующий интерфейс


import pandas as pd

def get_businessmen(df: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает DataFrame, оставляя в нём только пользователей из df,
    совершивших 20 и более международных звонков

    Параметры:
      df: исходный DataFrame

    Возвращаемое значение:
      отфильтрованный DataFrame
    """
    pass
  
 import pandas as pd

def get_businessmen(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['Total intl calls'] >= 20]
  
# Пример вызывающего кода

df = pd.read_csv('data.csv')
businessmen = get_businessmen(df)
