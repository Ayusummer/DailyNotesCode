import os

source_folder = (
    "E:\DownloadFile\Test\【未】[山田钟人&アベツカサ]葬送的芙莉莲\【个人汉化】推特官方短篇第二弹《勇者辛梅尔的冒险谭》"  # 替换为你的目录路径
)
count = 1

# 获取目录中的所有文件
files = os.listdir(source_folder)

# 按创建时间升序排序文件
files.sort(key=lambda x: os.path.getctime(os.path.join(source_folder, x)))

for filename in files:
    file_extension = os.path.splitext(filename)[1]
    new_name = f"{count:02d}{file_extension}"

    # 构建旧路径和新路径
    old_path = os.path.join(source_folder, filename)
    new_path = os.path.join(source_folder, new_name)

    # 重命名文件
    os.rename(old_path, new_path)

    count += 1
