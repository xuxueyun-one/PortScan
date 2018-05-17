# PortScan 端口扫描器多种语言实现方案

### go语言实现的端口扫描器
代码在go目录下，分别为tcp扫描以及syn扫描，运行命令：
```bash
go run filename
```

### python语言实现的端口扫描器
代码在python目录下，分别为tcp扫描以及syn扫描，并利用了socket、scapy模块以及nmap接口实现，运行命令：
```bash
python filename
```

### python+go实现的端口扫描器
代码在python+go目录下，实现了syn扫描，并提供了go打包后的文件，可直接供python调用，运行：
```bash
python tcp_syn_scan.py
```

### 更多介绍
https://thief.one/2018/05/17/1/