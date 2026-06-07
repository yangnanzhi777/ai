import requests

import json

url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
headers = {
    "Authorization": "Bearer c470583ee2de409c80d5ca147b7d15e6.mnilSyrY69UaObFB",
    "Content-Type": "application/json"
}

history = []

print("AI助手已上线！输入你的问题，回车即可。输入“退出”结束对话。")

while True:
    user_input = input("你：")
    if user_input == "退出":
        break
    
    history.append({"role": "user", "content": user_input})
    
    data = {
        "model": "GLM-4-Flash",
        "messages": history
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    if "choices" in result:
        ai_reply = result["choices"][0]["message"]["content"]
        print("AI：", ai_reply)
        history.append({"role": "assistant", "content": ai_reply})
    else:
        print("AI 返回了错误信息:", json.dumps(result, indent=2, ensure_ascii=False))