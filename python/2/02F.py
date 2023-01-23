В ДВФУ у каждого студента и сотрудника есть персональный адрес электронной почты в домене dvfu.ru.
Требуется написать программу, которая по заданным фамилии, имени и роли пользователя создает адрес его электронной почты в формате [фамилия].[имя]@[роль].dvfu.ru

with open("input.txt","r") as f:
    content = f.read().splitlines()
with open("output.txt","w") as f:
    _sec = content[0]
    _nam = content[1]
    _rol = content[2]
    f.write(_sec+"."+_nam+"@"+_rol+".dvfu.ru")
