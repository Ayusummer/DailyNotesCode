# Picture to ICO

将`png,jpg,jpeg`图片转换为ICO格式, 使用方法如下(先cd到项目根目录):

```bash
# 安装模块
go mod download
# 将 input.png 转换为 output.ico
go run main.go -i input.png -o output.ico
```

![image-20240429140021631](http://cdn.ayusummer233.top/DailyNotes/image-20240429140021631.png)

默认输出的ICO文件包含了`16x16, 32x32, 48x48, 64x64, 128x128, 256x256` 六种尺寸的图标, 如果需要自定义尺寸, 可以使用`-size`参数, 例如:

```bash
go run main.go -i input.png -o output.ico -size 64
```

![image-20240429140306990](http://cdn.ayusummer233.top/DailyNotes/image-20240429140306990.png)