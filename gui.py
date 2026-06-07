import requests
import json
import PySimpleGUI as sg

# 1. 配置区：把引号里的内容换成你自己的 API Key
API_KEY = "c470583ee2de409c80d5ca147b7d15e6.mnilSyrY69UaObFB"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

def analyze_comment(comment_text):
    if API_KEY == "你的API-Key":
        return "❌ 错误：请用记事本打开文件，把 API_KEY 换成你自己的智谱 API Key。"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = """你是一位顶尖的社交媒体分析师。用户会给你一条抖音高赞评论，请你从以下三个角度简要分析：
【观点提炼】
【为什么能火】
【可学习的点】"""
    
    data = {
        "model": "GLM-4-Flash",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"请分析这条抖音评论：\n{comment_text}"}
        ]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()
        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            return f"❌ API 调用失败：\n{json.dumps(result, indent=2, ensure_ascii=False)}"
    except Exception as e:
        return f"❌ 网络或程序出错：{e}"

# 2. 界面布局
sg.theme("LightBlue2")

layout = [
    [sg.Text("抖音评论区 AI 分析工具", font=("微软雅黑", 16))],
    [sg.Text("在下方粘贴高赞评论，然后点击按钮开始分析：")],
    [sg.Multiline(key="-INPUT-", size=(60, 10), font=("微软雅黑", 12))],
    [
        sg.Button("开始分析", key="-ANALYZE-", size=(15, 1)),
        sg.Button("清空内容", key="-CLEAR-", size=(15, 1)),
        sg.Button("退出程序", key="-EXIT-", size=(15, 1))
    ],
    [sg.Text("分析结果：", font=("微软雅黑", 12))],
    [sg.Multiline(key="-OUTPUT-", size=(60, 15), font=("微软雅黑", 12), disabled=True, background_color="white")]
]

window = sg.Window("抖音评论分析器", layout, resizable=True)

# 3. 事件循环
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "-EXIT-"):
        break
    elif event == "-CLEAR-":
        window["-INPUT-"].update("")
        window["-OUTPUT-"].update("")
    elif event == "-ANALYZE-":
        user_comment = values["-INPUT-"].strip()
        if not user_comment:
            sg.popup("请先粘贴评论再分析", font=("微软雅黑", 12))
        else:
            window["-OUTPUT-"].update("分析中，请稍候...")
            window.refresh()
            result_text = analyze_comment(user_comment)
            window["-OUTPUT-"].update(result_text)

window.close()