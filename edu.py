import streamlit as st
import pandas as pd

st.set_page_config(page_title="学区・教育環境ガイド", layout="wide")

st.title("🏫 学区・教育環境ガイド")

tab1, tab2, tab3 = st.tabs(["🎓 私立中学一覧", "🧸 周辺環境スコア", "📈 自治体支援比較"])

# --- タブ1: 私立中学の一覧 ---
with tab1:
    st.subheader("東京都内の私立中学校")
    # 簡易データベース例（実際には数百件のリストを読み込みます）
    school_data = [
        {"学校名": "開成中学校", "所在地": "荒川区西日暮里", "共学/別学": "男子校", "最寄り駅": "西日暮里"},
        {"学校名": "桜蔭中学校", "所在地": "文京区本郷", "共学/別学": "女子校", "最寄り駅": "水道橋"},
        {"学校名": "広尾学園", "所在地": "港区南麻布", "共学/別学": "共学", "最寄り駅": "広尾"},
    ]
    df_school = pd.DataFrame(school_data)
    
    area_filter = st.multiselect("エリアを選択", df_school["所在地"].unique())
    if area_filter:
        df_school = df_school[df_school["所在地"].isin(area_filter)]
    
    st.dataframe(df_school, use_container_width=True)

# --- タブ3: 自治体支援の中身サンプル ---
with tab3:
    st.subheader("23区 子育て支援比較")
    support_data = {
        "項目": ["給食費無償化", "高校生医療費", "塾代助成", "出産祝金"],
        "葛飾区": ["全公立無償", "18歳まで無料", "なし", "5万円"],
        "江戸川区": ["全公立無償", "18歳まで無料", "所得制限あり助成", "なし"],
        "港区": ["全公立無償", "18歳まで無料", "なし", "最大60万円"]
    }
    st.table(pd.DataFrame(support_data))