import streamlit as st
import requests
import json

st.set_page_config(page_title="抖音评论区分析器", page_icon="📊")

# 强制手机端容器自动撑开
st.markdown("""
    <style>
    .stMarkdown { max-height: none !important; overflow: visible !important; }
    .stAlert { max-height: none !important; overflow: visible !important; }
    .element-container { max-height: none !important; overflow: visible !important; }
    .stTextArea textarea { font-size: 16px; }
    button { font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 抖音评论区分析器")
st.markdown("粘贴评论区内容，AI 会分析高赞评论的爆款逻辑")

# ===== 智谱配置（替换成你的 API Key）=====
API_KEY = "c3d2696f16e543cc81b90e0491b6e410.qdLi7WMKlLKwDPei"
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
# =========================================

system_prompt = """你是抖音爆款内容分析师。用户会给你一段抖音评论区的内容（可能包含点赞数、用户名、评论内容）。

请按以下结构分析：

## 📈 高赞评论特征
- 列出点赞最高的3条评论，分析它们为什么能获得高赞

## 🧠 情绪触发点
- 这些评论触发了用户的什么情绪？（共鸣、好奇、反驳、感动等）

## 📝 可复用的文案公式
- 总结出2-3个可以直接套用的评论模板

## 💡 给博主的建议
- 根据评论区反馈，博主可以怎么优化内容？

请用简洁、直接的语言输出，不要废话。"""

st.markdown("---")

# 用户输入
user_input = st.text_area("粘贴评论区内容：", height=250, 
                          placeholder="例如：\n🔥 用户A：这个视频说得太对了！\n👍 用户B：学到了，谢谢博主\n❤️ 用户C：已转发给闺蜜")

if st.button("🔍 分析爆款逻辑", type="primary"):
    if not user_input:
        st.warning("请输入评论区内容")
    else:
        with st.spinner("分析中..."):
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
            
            try:
                response = requests.post(API_URL, headers=headers, json=data, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    ai_reply = result["choices"][0]["message"]["content"]
                    st.markdown("---")
                    st.markdown("### 📊 分析结果")
                    st.markdown(ai_reply)
                    
                    # 添加点赞按钮（可选）
                    st.markdown("---")
                    st.caption("🤖 分析由智谱 AI 提供")
                else:
                    st.error(f"API调用失败：{response.status_code}")
                    st.info("请检查 API Key 是否正确，或稍后重试")
                    
            except requests.exceptions.Timeout:
                st.error("请求超时，请稍后重试")
            except Exception as e:
                st.error(f"发生错误：{e}")