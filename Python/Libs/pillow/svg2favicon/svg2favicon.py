import cairosvg
from PIL import Image
from pathlib import Path

svg_path = Path(__file__).parent / 'input.svg'
png_output_path = Path(__file__).parent / 'output.png'
ico_output_path = Path(__file__).parent / 'favicon.ico'

# 1. 将 SVG 转换为 PNG
cairosvg.svg2png(url="input.svg", write_to="output.png")

# 2. 使用 PIL 打开 PNG 图像
img = Image.open(png_output_path)

# 3. 调整图像尺寸为 32x32
img.thumbnail((32,32))

# 4. 保存为 ICO 文件
img.save(ico_output_path, format='ICO')
