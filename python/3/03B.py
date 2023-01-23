Необходимо написать программу, которая группирует студентов по их группам.

groups = {}
with open("input.txt", 'r') as f:
    num_students = int(f.readline())
    for i in range(num_students):
        group, name = f.readline().split('\t')
        if group not in groups:
            groups[group] = []
        if "\n" in name:
            groups[group].append(name[:-1])
        else:
            groups[group].append(name)

with open("output.txt", 'w') as f:
    for group in sorted(groups):
        f.write(group+'\n')
        for student in sorted(groups[group]):
            f.write(student+"\n")
