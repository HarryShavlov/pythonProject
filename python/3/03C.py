На компьютере под управлением операционной системы Linux имеется каталог, содержащий N файлов. 
Пользователю требуется скопировать эти файлы на компьютер, работающий под управлением ОС Windows. 
К сожалению, файловая система Windows имеет странное свойство. 
Несмотря на то, что она сохраняет большие и малые буквы в именах файлов, имена, отличающиеся только регистром букв, считаются одинаковыми. 
Например, файлы с именами ChangeLog, CHANGELOG и changelog при копировании на файловую систему Windows попадут в один и тот же файл.
Чтобы избежать потери данных, предлагается при копировании переименовывать файлы по следующим правилам:
  Файлы копируются в порядке перечисления в исходном каталоге.
  Имена файлов считаются одинаковыми, если они совпадают с точностью до регистра.
  Если при копировании очередного файла выяснилось, что файл с таким именем уже был скопирован, то к имени текущего файла добавляется суффикс "1".
  Если имя, полученное после присоединения суффикса, также уже встречалось, то перебираются суффиксы "2", "3", ..., "10", "11", ... до тех пор, пока не найдётся суффикс, дающий уникальное имя.

  
 def rename_files(N: int, names: list[str]) -> list[str]:
    result = []
    used_names = set()
    for name in names:
        modified_name = name
        suffix = 1
        while modified_name.lower() in used_names:
            modified_name = f"{name}{suffix}"
            suffix += 1
        used_names.add(modified_name.lower())
        result.append(modified_name)
    return result


with open("input.txt", "r") as f:
    num_names = int(f.readline())
    file_names = [f.readline().strip() for _ in range(num_names)]

result = rename_files(num_names, file_names)
with open('output.txt', 'w') as f:
    for file_name in result:
        f.write(file_name + '\n')
