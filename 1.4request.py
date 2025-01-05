import requests

a = input("请输入音频流的URL")
b = input("请输入cookies-sessdata")
c = input("请输入原视频的URL")

audio_url = a

cookies = {
    "SESSDATA": b,
}

headers = {
    "Referer": c,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Origin": "https://www.bilibili.com",
    "Connection": "keep-alive",
}

response = requests.get(audio_url, headers=headers, cookies=cookies, stream=True, verify=False)
if response.status_code == 200:
    with open("audio.m4s", "wb") as audio_file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                audio_file.write(chunk)
    print("音频流下载完成！")
else:
    print(f"请求失败，状态码: {response.status_code}")