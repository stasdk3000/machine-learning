def write_to_file(name, data):
    file = open(name, 'w')
    for (i, item) in enumerate(data):
        file.write(str(item) + '\n')

    file.close()
