# 端口扫描

## portscan_with_args

尝试与目标主机建立TCP连接, 如果连接成功, 则说明该端口开放, 否则该端口关闭

对于开放的端口, 与 port_dict 中的端口进行比对输出可能的服务信息

```bash
python portscan_with_args.py -i [ip]
```

![image-20240117103445943](http://cdn.ayusummer233.top/DailyNotes/202401191718468.png)

