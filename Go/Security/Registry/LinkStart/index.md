# LinkStart

修改注册表, 使得当前程序在用户登录时执行, 向当前目录写一个 HelloWorld.txt 的空文件

---

对于

```go
cmd := exec.Command("reg", "add", `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, "/v", "MyAppWriteHelloWorld", "/t", "REG_SZ", "/d", ex, "/f")
```

reg 命令的各个参数的含义如下：

- `add`：表示要添加一个新的注册表项。
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`：注册表项的路径，这个路径下的每一项都会在用户登录时自动运行。
- `/v MyApp`：新的注册表项的名字是 MyApp。这只是一个示例，你可以根据需要替换为其他名字。
- `/t REG_SZ`：新的注册表项的类型是 REG_SZ，即一个以 null 结尾的字符串。
- `/d`：后面跟的是注册表项的数据。在这个例子中，数据是 ex，即当前程序的路径。这就是让当前程序在用户登录时自动运行的关键。
- `/f`：强制添加注册表项，如果同名的注册表项已经存在，则会被覆盖。

简单地说，这行代码的作用就是让当前程序在用户每次登录时自动运行。

不过这行代码使用的 `exec.Command` 调用了命令行窗口, 因此运行时会弹出命令行窗口, 这对于程序的隐蔽执行很不利, 因此要考虑换用其他方式执行
