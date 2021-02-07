# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/python-lists
#
# Lists

def perform(commands):
    lst = []
    for command in commands:
        command = command.split()
        command_type = command[0]

        if command_type == 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif command_type == 'print':
            print(lst)
        elif command_type == 'remove':
            lst.remove(int(command[1]))
        elif command_type == 'append':
            lst.append(int(command[1]))
        elif command_type == 'sort':
            lst.sort()
        elif command_type == 'pop':
            lst.pop()
        elif command_type == 'reverse':
            lst.reverse()


if __name__ == '__main__':
    perform(['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6',
             'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse',
             'print'])
