import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        file_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, 'f'Время изменения: {file_time_readable}, '
      f'Родительская директория: {parent_dir}')
