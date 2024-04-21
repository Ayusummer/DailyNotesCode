# 正常编译, 运行后会弹出一个cmd窗口
go build -o normal.exe
# 隐藏窗口编译, 运行后不会弹出cmd窗口
go build -ldflags="-H windowsgui" -o hide_window.exe

# go build -ldflags="-H windowsgui" -o msedge.exe