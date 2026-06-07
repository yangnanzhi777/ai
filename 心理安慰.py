import requests
import json

# --- 配置区：换成你自己的 API Key ---
API_KEY = "c470583ee2de409c80d5ca147b7d15e6.mnilSyrY69UaObFB"  # ← 记得改成你自己的
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# --- 系统提示词 (System Prompt) ---
system_prompt = """
你的沟通风格是温柔而坚定，像苏格拉底一样通过提问引导人思考。用户会向你倾诉他的烦恼。请你按以下结构回应：
1. 【共情与反馈】用一句话精准地表达出对方的感受，让他感到被理解。
2. 【认知探索】提出一个能引发思考的问题，帮助他审视自己的想法。
3. 【个人行动】给他一个非常具体、微小、今天就能做的实验性任务。
"""

# --- 初始化消息列表，并放入 System Prompt ---
messages = [{"role": "system", "content": system_prompt}]

print("=" * 40)
print("🧠 心理安慰助手已上线")
print("向我倾诉你的烦恼，我会倾听并给你建议。")
print("输入 '退出' 结束对话。")
print("=" * 40)

# --- 主程序循环 ---
while True:
    user_input = input("\n你：")
    if user_input == "退出":
        print("👋 助手已关闭，祝你一切顺利。")
        break
    
    # 将用户输入添加到对话历史
    messages.append({"role": "user", "content": user_input})
    
    # 准备发送给 API 的数据
    data = {
        "model": "GLM-4-Flash",
        "messages": messages
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()
        
        if "choices" in result:
            ai_reply = result["choices"][0]["message"]["content"]
            print("AI：", ai_reply)
            # 将 AI 的回复也添加到对话历史，以实现记忆功能
            messages.append({"role": "assistant", "content": ai_reply})
        else:
            print("❌ API 调用失败，返回的错误信息是：")
            print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"❌ 网络或程序运行出错：{e}")