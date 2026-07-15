import dashscope
import requests
from dotenv import load_dotenv
import os






# 强烈建议通过环境变量 DASHSCOPE_API_KEY 设置你的API Key
load_dotenv("./api.env")
api_key = os.getenv("DASHSCOPE_API_KEY")
if not dashscope.api_key:
    raise ValueError("请确保输入了正确的API")









#未完成
# 1. 构造消息，音频可以通过公网URL或本地文件路径提供
messages = [
    {
        "role": "user",
        "content": [
            # 方式A：使用公网可访问的音频URL（推荐）
            #{"audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"},
            # 方式B：使用本地文件路径（SDK会自动上传）
            {"audio": "./responsibility.m4a"},
        ]
    }
]

# 2. 调用 MultiModalConversation API
response = dashscope.MultiModalConversation.call(
    model="qwen3-asr-flash",  # 指定正确的模型名称
    messages=messages,
    api_key= os.getenv("DASHSCOPE_API_KEY"),  # 如果未设置环境变量，可在此处传入
)

# 3. 处理返回结果
if response.status_code == 200:
    # 提取识别出的文本
    transcribed_text = response.output.choices[0].message.content
    print(f"识别结果: {transcribed_text}")
else:
    print(f"调用失败: {response.code} - {response.message}")
