import streamlit as st
import requests
import json

st.set_page_config(page_title="心理安慰助手", page_icon="🌸")

st.title("🌸 心理安慰助手")
st.markdown("像苏格拉底一样，通过提问引导你思考")

# 你的 API 配置
API_KEY = "c470583ee2de409c80d5ca147b7d15e6.mni1syrY69Ua0bFB"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

system_prompt = """你的沟通风格是温柔而坚定，像苏格拉底一样通过提问引导人思考。用户会向你倾诉他的烦恼。请你按以下结构回应：
1. 【共情与反馈】用一句话精准地表达出，让他感到被理解。
2. 【认知探索】提出一个能引发思考的问题，帮助他审视自己的想法。
3. 【个人行动】给他一个非常具体、微小、今天就能做的实验性任务。"""

# 界面：用户输入
user_input = st.text_area("你有什么想聊的吗？", height=100)

if st.button("💬 发送"):
    if user_input:
        with st.spinner("思考中..."):
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
            data = {
                "model": "GLM-4-Flash",
                "messages": messages
            }
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            response = requests.post(API_URL, headers=headers, json=data)
            result = response.json()["choices"][0]["message"]["content"]
            st.success("回应：")
            st.write(result)
    else:
        st.warning("请输入内容")