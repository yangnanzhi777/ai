import requests
import json

# 1. 配置区：换上你自己的智谱 API Key
API_KEY = "c470583ee2de409c80d5ca147b7d15e6.mnilSyrY69UaObFB"  # ← 改这里！
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 2. 初始化窗口
print("=" * 50)
print("🧠 你的私人 AI 角色工厂已上线")
print("用法1：直接问任何问题。")
print("用法2：输入 '换人'，然后描述你想创造的AI专家。")
print("输入 '退出' 关闭程序。")
print("=" * 60)

# 消息列表会记录所有对话，实现记忆功能
messages = []

while True:
    user_input = input("\n你：")
    
    if user_input == "退出":
        print("工厂已关闭。")
        break
    
    # 核心功能：换人！
    if user_input == "换人":
        messages = []
        new_role = input("请告诉我，你想让AI变成什么角色：")
        messages.append({"role": "system", "content": new_role})
        print(f"角色已设定为：{new_role}")
        continue
    
    # 如果列表是空的，就给他一个默认身份
    if not messages:
        default_role = "你是一位知识渊博且耐心的导师，总是用大白话解释复杂概念。"
        messages.append({"role": "system", "content": default_role})
    
    messages.append({"role": "user", "content": user_input})
    
    data = {
        "model": "GLM-4-Flash",
        "messages": messages
    }
    
    try:
        response = requests.post(API_URL, headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }, json=data)
        result = response.json()
        
        if "choices" in result:
            ai_reply = result["choices"][0]["message"]["content"]
            print("AI：", ai_reply)
            messages.append({"role": "assistant", "content": ai_reply})
        else:
            print("API 返回错误：", json.dmps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"网络或程序出错：{e}")