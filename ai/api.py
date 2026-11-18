import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-20b21efdffca47c1aaad7f8a7c49eec2",   # 换成你的 Key
    base_url="https://api.deepseek.com",
)

# 对话历史，system 消息只放一次
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
]

print("开始对话（输入 exit / quit 退出）\n")

while True:
    user_input = input("你: ").strip()
    if user_input.lower() in ("exit", "quit"):
        print("再见！")
        break
    if not user_input:
        continue

    # 1. 把用户这轮的话加入历史
    messages.append({"role": "user", "content": user_input})

    # 2. 带着完整历史请求模型
    response = client.chat.completions.create(
        model="deepseek-chat",          # 先用稳定模型名，跑通再换
        messages=messages,
        stream=False,
    )

    reply = response.choices[0].message.content
    print(f"AI: {reply}\n")

    # 3. 把模型回复也加入历史，下一轮模型才能"记得"
    messages.append({"role": "assistant", "content": reply})