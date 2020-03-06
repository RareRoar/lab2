from os import remove, rename, path
from random import randint


# creating file
def create_file(name, quantity, min_value, max_value):
    with open("{}.txt".format(name), 'w') as new_file:
        for _ in range(quantity):
            new_file.write("{}\n".format(randint(min_value, max_value)))


def external_sort(name, cluster_size):
    # slicing file
    with open("{}.txt".format(name), 'r') as sort_file:
        buffer_list = []
        count = 0
        for line in sort_file:
            buffer_list.append(line)
            if len(buffer_list) == cluster_size:
                with open("temp{}.txt".format(count), 'w') as temp_file:
                    temp_file.writelines(buffer_list)
                count += 1
                buffer_list.clear()
        if buffer_list.__contains__('\n'):
            buffer_list.remove('\n')
        if buffer_list:
            with open("temp{}.txt".format(count), 'w') as temp_file:
                temp_file.writelines(buffer_list)
                count += 1
    # sorting files
    for i in range(count):
        with open("temp{}.txt".format(i), 'r+') as file:
            buffer = file.readlines()
            list_to_sort = [int(number.strip()) for number in buffer]
            list_to_sort.sort()
            file.seek(0)
            file.writelines(["{}\n".format(number) for number in list_to_sort])

    def _minimum(x, y):
        if y == '':
            return x
        if x == '':
            return y
        return x if int(x) < int(y) else y

    # merging files
    while count > 1:
        for i in range(0, count - count % 2, 2):
            with open("temp{}.txt".format(i), 'r') as file1:
                with open("temp{}.txt".format(i + 1), 'r') as file2:
                    with open("temp{}_{}.txt".format(i, i + 1), 'w') as file3:
                        temp1 = int(file1.readline().strip())
                        temp2 = int(file2.readline().strip())
                        file3.write("{}\n".format(temp1 if temp1 < temp2 else temp2))
                        if temp1 < temp2:
                            temp1 = file1.readline().strip()
                        else:
                            temp2 = file2.readline().strip()
                        while temp1 != '' or temp2 != '':
                            file3.write("{}\n".format(_minimum(temp1, temp2)))
                            if _minimum(temp1, temp2) == temp1:
                                temp1 = file1.readline().strip()
                            else:
                                temp2 = file2.readline().strip()
            remove("temp{}.txt".format(i))
            remove("temp{}.txt".format(i + 1))
        for i in range(0, count - count % 2, 2):
            rename("temp{}_{}.txt".format(i, i + 1), "temp{}.txt".format(i // 2))
        if path.isfile("temp{}.txt".format(count - 1)):
            rename("temp{}.txt".format(count - 1), "temp{}.txt".format(count // 2))
        count = count // 2 + count % 2
    if path.isfile("sorted.txt"):
        remove("sorted.txt")
    rename("temp0.txt", "sorted.txt")
