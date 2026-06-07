import requests
import json

# 你的 API 配置（和之前一样）
url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
headers = {
    "Authorization": "Bearer c470583ee2de409c80d5ca147b7d15e6.mnilSyrY69UaObFB",
    "Content-Type": "application/json"
}

print("=" * 40)
print("🎯 抖音评论区 AI 分析工具")
print("粘贴高赞评论，按回车。输入 '退出' 结束。")
print("=" * 40)

while True:
    comment = input("\n📋 粘贴评论: ")
    if comment == "退出":
        print("👋 工具已关闭。")
        break
    
    # 预设的分析规则
    system_prompt = """你是一位顶尖的社交媒体分析师。用户会给你一条抖音高赞评论，请你从以下三个角度简要分析：

【观点提炼】这条评论的核心观点是什么？（通俗易懂）

【为什么能火】从情绪、幽默、共鸣、槽点等维度，分析为什么能获高赞

【可学习的点】我能借鉴什么？用于写爆款评论、自媒体或营销中，请给一条实用建议
"""
    data = {
        "model": "GLM-4-Flash",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"请分析这条抖音评论：\n{comment}"}
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    if "choices" in result:
        ai_reply = result["choices"][0]["message"]["content"]
        print("\n 🤖 深度分析：\n", ai_reply)
    else:
        print("❌ API 调用失败：", json.dumps(result, indent=2, ensure_ascii=False))