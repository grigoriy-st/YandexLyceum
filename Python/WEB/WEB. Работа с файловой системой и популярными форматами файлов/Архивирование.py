import os
import shutil
import datetime

def make_reserve_arc(source, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = f"backup_{timestamp}"
    archive_path = os.path.join(dest, archive_name)
    
    shutil.make_archive(archive_path, 'zip', source)
    print(f"Резервная копия создана: {archive_path}.zip")

source = input("Введите путь к каталогу для архивации: ").strip()
dest = input("Введите путь к каталогу для сохранения архива: ").strip()
make_reserve_arc(source, dest)