## 目录结构

```
.
├── CVE-2022-45658_writeup.pdf     # CVE-2022-45658 漏洞分析文档
├── exp.py                         # 漏洞利用脚本
├── readme.md                      # 本说明文档
└── rootfs.tar.gz                  # 固件根文件系统压缩包
	└── start_server.sh            # 启动 httpd 服务器
	└── start_gdb.sh               # 启动调试环境
```

## 文件说明

### CVE-2022-45658_writeup.pdf
CVE-2022-45658 漏洞的详细分析报告，包含修复环境流程、漏洞点、利用思路。

### exp.py
针对该漏洞的 exploit 脚本。

### rootfs.tar.gz
IoT 设备固件的根文件系统。

解压后包含以下重要脚本：
- `start_server.sh` - 启动 httpd 服务器
- `start_gdb.sh` - 启动调试环境