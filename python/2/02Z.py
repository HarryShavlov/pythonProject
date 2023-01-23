Turing Machine

def read_input():
    N, M, K = map(int, input().split())
    commands_list = {}
    for i in range(N):
        commands_list[i] = input().split()
    tape = input().split()
    return M, commands_list, tape

def execute_machineTuring(M, commands_list, tape):
    position = 0
    condition = 0
    while condition != M:
        command = commands_list[int(tape[position])]
        tape[position] = command[condition * 3]
        if command[condition * 3 + 1] == "R":
            if position + 1 == len(tape):
                tape = tape + ["0"]
            position += 1
        elif command[condition * 3 + 1] == "L":
            if position - 1 < 0:
                tape = ["0"] + tape
                position = 0
            else:
                position -= 1
        condition = int(command[3 * condition + 2])
    return " ".join(tape[position:])

M, commands_list, start_tape = read_input()
print(execute_machineTuring(M, commands_list, start_tape))
