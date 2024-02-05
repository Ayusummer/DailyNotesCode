import xlsxwriter
from PIL import Image as PILImage
from pathlib import Path
from io import BytesIO

# 创建一个新的工作簿
excel_path = Path(__file__).parent / "test.xlsx"
workbook = xlsxwriter.Workbook(excel_path)
sheet = workbook.add_worksheet()

# 设置所有单元格列宽为4
sheet.set_column(0, 1000, 4)

# 设置第一行的行高为64
sheet.set_row(0, 50)


# 获取images目录中的所有图片文件
image_dir = Path(__file__).parent / "images"
image_files = [f for f in image_dir.iterdir() if f.is_file()]

# 合并首行单元格以两个两个的组合
for col in range(0, len(image_files) * 2, 2):
    sheet.merge_range(0, col, 0, col + 1, None)
    sheet.merge_range(1, col, 1, col + 1, None)

# 将每个图片依次插入到第一行合并后的单元格中
for idx, image_file in enumerate(image_files, start=0):
    # 构建图片文件的完整路径
    image_path = image_dir / image_file

    # 打开图片
    img = PILImage.open(image_path)

    # 将图像等比例放大两倍
    width, height = img.size
    new_width = width * 2
    new_height = height * 2
    img = img.resize((new_width, new_height))

    # 将图片转换为二进制数据
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")

    # 创建一个新的工作表单元格，并插入图片, 图片填充满竖直方向, 水平垂直均居中
    sheet.insert_image(
        0,
        idx * 2,
        str(image_path),
        {
            "image_data": img_bytes,
            "x_scale": 1,
            "y_scale": 1,
            "x_offset": 0,
            "y_offset": 0,
            "positioning": 1,
        },
    )

    # 在第二行对应的单元格中插入图片文件名(不包含路径与后缀名)
    sheet.write(1, idx * 2, image_file.stem)

# 全局设置工作表水平竖直均居中对齐
workbook.formats[0].set_align("center")
workbook.formats[0].set_align("vcenter")

# 保存工作簿
workbook.close()
