import os
import re


def reorder_jpgs(path, test=True):
    files = [os.path.join(path, f)
             for f in os.listdir(path)
             if os.path.isfile(os.path.join(path, f))]# and f[-3:].lower() == 'jpg']
    example_path, example_file = os.path.split(files[0])
    position = re.search('\d+', example_file)

    numbers = [int(f[len(example_path) + position.start() + 1:len(example_path) + position.end() + 1]) for f in files]
    for index, numb in enumerate(numbers[:-1]):
        if numb + 1 != numbers[index + 1]:
            last_number = numb
            break

    first_files = []
    last_files = []
    for index, file in enumerate(files):
        if index >= last_number:
            first_files.append(file)
        else:
            last_files.append(file)

    files = first_files + last_files

    for index, file in enumerate(files):
        number = '{:04d}'.format(index + 1)
        new_file = file[:len(example_path) + position.start() + 1] + number + '_.jpg'
        print(file, new_file)
        if not test:
            os.rename(file, new_file)