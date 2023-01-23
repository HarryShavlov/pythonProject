Требуется реализовать на языке Python функцию PrintMatrix(mat), которая принимает двумерный массив и печатает его. Пример использования функции в примерах тестов.

def PrintMatrix(mat):
    for i in range(len(mat)):
        _str=""
        for j in range(len(mat[i])):
            _str += str(mat[i][j])+" "
        print(_str[:len(_str)-1])  
