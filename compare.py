import streamlit as st
import requests

st.set_page_config(page_title="AI 模型对比", page_icon="🔬")
st.title("🔬 AI 模型对比：智谱 vs DeepSeek")
st.markdown("输入同一个问题，看看两个模型的回答有什么不同")

# ===== 智谱配置 =====
ZHIPU_KEY = "c3d2696f16e543cc81b90e0491b6e410.qdLi7WMKlLKwDPei"
ZHIPU_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# ===== DeepSeek 配置（替换成你的 Key）=====
DEEPSEEK_KEY = "sk-3a9d6bf263424c089736e4b964433f4d"
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

# 用户输入
user_question = st.text_area("输入你的问题：", height=100)

if st.button("🔍 对比回答"):
    if not user_question:
        st.warning("请输入问题")
    else:
        col1, col2 = st.columns(2)
        
        # 调用智谱
        with col1:
            st.subheader("🧠 智谱 GLM-4-Flash")
            with st.spinner("智谱思考中..."):
                zhipu_headers = {
                    "Authorization": f"Bearer {ZHIPU_KEY}",
                    "Content-Type": "application/json"
                }
                zhipu_data = {
                    "model": "glm-4-flash",
                    "messages": [{"role": "user", "content": user_question}]
                }
                try:
                    r = requests.post(ZHIPU_URL, headers=zhipu_headers, json=zhipu_data, timeout=30)
                    if r.status_code == 200:
                        st.write(r.json()["choices"][0]["message"]["content"])
                    else:
                        st.error(f"错误: {r.status_code}")
                except Exception as e:
                    st.error(f"请求失败: {e}")
        
        # 调用 DeepSeek
        with col2:
            st.subheader("🚀 DeepSeek Chat")
            with st.spinner("DeepSeek 思考中..."):
                ds_headers = {
                    "Authorization": f"Bearer {DEEPSEEK_KEY}",
                    "Content-Type": "application/json"
                }
                ds_data = {
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": user_question}],
                    "max_tokens": 500
                }
                try:
                    r = requests.post(DEEPSEEK_URL, headers=ds_headers, json=ds_data, timeout=30)
                    if r.status_code == 200:
                        st.write(r.json()["choices"][0]["message"]["content"])
                    else:
                        st.error(f"错误: {r.status_code}")
                except Exception as e:
                    st.error(f"请求失败: {e}")