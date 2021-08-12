# pyob
A simple python obfuscator
一个简单的python混淆器

## 使用

首先,下载链接里的pyob.py

> [直接链接](https://github.com/TES286/pyob/raw/pyob.py) [备用链接](https://proxy.0123456789.workers.dev/https://github.com/TES286/pyob/raw/pyob.py)

使用命令行运行

`pyob.py [源文件] [目标文件]`

> 使用exec运行,只能套两层

## 兼容性

没有测试,但应该主流版本都行

## 实现

将base64的字典打乱,然后一个一个字符拼接成源文件lzma压缩后的base64,释放后调用exec执行

## 捐赠

[这里](https://pyob.tes286.top/donate.htm)
