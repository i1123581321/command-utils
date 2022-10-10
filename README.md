# command_utils

使用 python 编写的一系列简单的命令行脚本

## 安装

git clone 下来后直接在根目录运行

```shell
pip install .
````

或是 build 后安装

## ffmpeg_utils

基于 ffmpeg 的一系列脚本，需要路径中有 ffmpeg，ffprobe 等

### split_video

将视频切分成一小时左右的段落，主要是为了方便阿b投稿

超出一小时的部分如果不足半小时则不切分，否则单独切成一段

```
split_video -h
usage: split_video [-h] [-p PREFIX] input

Divide the video into paragraphs of about 1 hour

positional arguments:
  input                 Video path to be split

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        keep video name as output prefix
```
