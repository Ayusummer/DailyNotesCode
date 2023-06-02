from PIL import Image
from pathlib import Path

png_input_path = Path(__file__).parent / 'logo.png'
ico_output_path = Path(__file__).parent / 'output/favicon.ico'

# 2. 使用 PIL 打开 PNG 图像
img = Image.open(png_input_path)

# 3. 调整图像尺寸
img.thumbnail((48,48))

# 4. 保存为 ICO 文件
img.save(ico_output_path, format='ICO')
