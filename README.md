# Bilibili 音频流爬取工具

一个简单的 Python 脚本，用于从 Bilibili 爬取音频流。 通过输入音频流的 URL、`SESSDATA` cookie 和原视频的 URL，即可下载音频流到本地。

## 功能介绍

- 下载指定 Bilibili 音频流到本地文件 `audio.m4s`。
- 支持自定义输入音频 URL 和视频 URL。
- 使用 Cookie 验证访问权限。

## 使用方法

### 1. 环境准备

确保已安装以下依赖项：
- Python 3.x
- `requests` 库
- 抓包软件（charles...)

如果尚未安装 `requests`，请运行以下命令安装：
'pip install requests'

### 2. 脚本运行
1.克隆或下载此项目到本地。
 
2.运行脚本 1.4request.py：
  'python 1.4request.py'

3.  根据提示输入以下信息：
 
 1. 音频流的 URL：Bilibili 音频流地址。(通过爬虫软件爬取）
 2. Cookies 的 SESSDATA：从浏览器开发者工具或请求中获取的 Bilibili 登录状态 Cookie。
 3. 原频的 URL：对应的 Bilibili 视频页面地址。
 4. 下载完成后，音频文件将保存为 audio.m4s。（若不想下载.m4s格式的播放器 可通过更改后缀进行操作）

### 3. 文件说明
•  1.4request.py：脚本文件。
•  audio.m4s：下载的音频流文件（默认文件名）。

注意事项
1.  确保输入的音频 URL 和原视频 URL 对应正确，否则可能导致下载失败。
2.  请勿非法使用此脚本，仅用于学习和交流，尊重 Bilibili 的使用条款。
3.  用 Cookie 时，请注意保护您的隐私，避免泄露登录信息。

示例输入
运行脚本后按提示输入以下内容：
1.  请输入音频流的URL: https://example.com/audio_url.m4s
2.  请输入cookies-sessdata: your_sessdata_value
3.  请输入原视频的URL: https://www.bilibili.com/video/example_video'

示例输出
'音频流下载完成！'

##  License
该项目仅供学习使用，禁止任何商业用途。


