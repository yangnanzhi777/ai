import streamlit as st
import requests

st.set_page_config(page_title="心理安慰助手", page_icon="🌸")

# 强制手机端容器自动撑开，消除空白
st.markdown("""
    <style>
    .stMarkdown {
        max-height: none !important;
        overflow: visible !important;
    }
    .stAlert {
        max-height: none !important;
        overflow: visible !important;
    }
    .element-container {
        max-height: none !important;
        overflow: visible !important;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    button {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌸 心理安慰助手")
st.markdown("像苏格拉底一样，通过提问引导你思考")

API_KEY = "c3d2696f16e543cc81b90e0491b6e410.qdLi7WMKlLKwDPei"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

system_prompt = """你的沟通风格是温柔而坚定，像苏格拉底一样通过提问引导人思考。用户会向你倾诉他的烦恼。请你按以下结构回应：
1. 【共情与反馈】用一句话精准地表达出，让他感到被理解。
2. 【认知探索】提出一个能引发思考的问题，帮助他审视自己的想法。
3. 【个人行动】给他一个非常具体、微小、今天就能做的实验性任务。"""

user_input = st.text_area("你有什么想聊的吗？", height=120)

if st.button("发送"):
    if not user_input:
        st.warning("请输入内容")
    else:
        with st.spinner("思考中..."):
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "glm-4-flash",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            }
            response = requests.post(API_URL, headers=headers, json=data)
            
            if response.status_code == 200:
                reply = response.json()["choices"][0]["message"]["content"]
                st.markdown("### 🌸 回应：")
                st.markdown(reply)
            else:
                st.error(f"调用失败：{response.status_code}")