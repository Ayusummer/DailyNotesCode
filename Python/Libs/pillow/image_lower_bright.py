from PIL import Image, ImageEnhance

from pathlib import Path

# 从当前文件索引
image_path = Path(__file__).parent / "42.jpg"
img = Image.open(image_path) # 载入图片
enhancer = ImageEnhance.Brightness(img) # 创建亮度调节器
img = enhancer.enhance(0.5) # 将亮度降低50%
img.save("image_dark.jpg") # 保存图片