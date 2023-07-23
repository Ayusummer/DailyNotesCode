from PIL import Image
from pathlib import Path

# 从当前文件索引
image_path = Path(__file__).parent / "42.jpg"
image = Image.open(image_path) # 载入头像
gray_image = image.convert("L") # 转换为灰度图像
gray_image.save("gray_avatar.png") # 保存灰度头像