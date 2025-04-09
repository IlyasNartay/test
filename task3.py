import os
import shutil

# 1. Путь к папке с файлами заказчика
source_folder = "Раздаточный материал 1\\Файлы заказчика\\"

# 3. Создаем папку "Содержит 2" в текущей директории
destination_folder = os.path.join(os.getcwd(), 'Содержит 2')
os.makedirs(destination_folder, exist_ok=True)

# 2. Перебираем файлы и перемещаем те, что содержат цифру "2" в имени
for filename in os.listdir(source_folder):
    if '2' in filename:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f'Файл "{filename}" перемещен в папку "Содержит 2"')
