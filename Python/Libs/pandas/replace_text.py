import pandas as pd
from pathlib import Path

excel_path = Path(__file__).parent / "test.xlsx"
output_path = Path(__file__).parent / "output.xlsx"
src_text = "待替换文本"
dst_text = "替换后文本"

# 示例数据，您可以替换为您自己的CSV文件或DataFrame
df = pd.read_excel(excel_path, sheet_name="Sheet1", header=0)


df = df.replace(src_text, dst_text, regex=True)
print(df)

# 将结果写入Excel文件
df.to_excel(output_path, index=False)
