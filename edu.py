import streamlit as st
import pandas as pd

# 1. ページ設定
st.set_page_config(page_title="教育環境ナビ", layout="wide")

# CSS: デザイン・テーブル規格の統一
st.markdown("""
    <style>
    header { visibility: hidden; }
    .block-container { padding-top: 1rem !important; }
    .main-header { 
        font-size: 26px; font-weight: bold; color: #1a365d; 
        text-align: center; border-bottom: 3px solid #3498db;
        padding-bottom: 10px; margin-bottom: 20px; 
    }
    .highlight-box {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        margin-bottom: 15px;
    }
    .table-title {
        font-size: 18px; font-weight: bold; margin-top: 30px; margin-bottom: 15px;
        text-align: center; color: #2c3e50; border-left: 5px solid #3498db; padding-left: 10px;
    }
    .sub-table-title {
        font-size: 16px; font-weight: bold; margin-top: 15px; margin-bottom: 10px;
        color: #1a365d;
    }
    /* テーブル全体のデザインを統一 */
    table { width: 100%; border-collapse: collapse; margin-bottom: 20px; table-layout: fixed; }
    th { background-color: #f2f2f2; text-align: center !important; padding: 12px; font-size: 14px; border-bottom: 2px solid #ddd; }
    td { border-bottom: 1px solid #ddd; padding: 10px; text-align: center !important; font-size: 14px; overflow: hidden; text-overflow: ellipsis; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🏫 東京 難関校・教育環境完全ガイド</div>', unsafe_allow_html=True)

# --- 中学データ (規格統一：順位, 校名, 偏差値, 所在地, 最寄り) ---
school_data = [
    {"順位": 1, "校名": "開成中学校", "偏差値": 72, "カテゴリ": "男子校", "所在地": "荒川区", "詳細": "西日暮里"},
    {"順位": 2, "校名": "麻布中学校", "偏差値": 68, "カテゴリ": "男子校", "所在地": "港区", "詳細": "広尾"},
    {"順位": 3, "校名": "駒場東邦中学校", "偏差値": 67, "カテゴリ": "男子校", "所在地": "世田谷区", "詳細": "駒場東大前"},
    {"順位": 4, "校名": "武蔵中学校", "偏差値": 65, "カテゴリ": "男子校", "所在地": "練馬区", "詳細": "江古田"},
    {"順位": 5, "校名": "海城中学校", "偏差値": 64, "カテゴリ": "男子校", "所在地": "新宿区", "詳細": "新大久保"},
    {"順位": 6, "校名": "早稲田中学校", "偏差値": 64, "カテゴリ": "男子校", "所在地": "新宿区", "詳細": "早稲田"},
    {"順位": 7, "校名": "本郷中学校", "偏差値": 60, "カテゴリ": "男子校", "所在地": "豊島区", "詳細": "巣鴨"},
    {"順位": 1, "校名": "桜蔭中学校", "偏差値": 71, "カテゴリ": "女子校", "所在地": "文京区", "詳細": "水道橋"},
    {"順位": 2, "校名": "女子学院中学校", "偏差値": 69, "カテゴリ": "女子校", "所在地": "千代田区", "詳細": "市ヶ谷"},
    {"順位": 3, "校名": "豊島岡女子学園", "偏差値": 68, "カテゴリ": "女子校", "所在地": "豊島区", "詳細": "池袋"},
    {"順位": 4, "校名": "雙葉中学校", "偏差値": 67, "カテゴリ": "女子校", "所在地": "千代田区", "詳細": "四ツ谷"},
    {"順位": 5, "校名": "白百合学園", "偏差値": 64, "カテゴリ": "女子校", "所在地": "千代田区", "詳細": "九段下"},
    {"順位": 6, "校名": "吉祥女子中学校", "偏差値": 63, "カテゴリ": "女子校", "所在地": "武蔵野市", "詳細": "吉祥寺"},
    {"順位": 7, "校名": "鴎友学園女子", "偏差値": 62, "カテゴリ": "女子校", "所在地": "世田谷区", "詳細": "宮の坂"},
    {"順位": 1, "校名": "渋谷教育学園渋谷", "偏差値": 70, "カテゴリ": "共学", "所在地": "渋谷区", "詳細": "渋谷"},
    {"順位": 2, "校名": "筑波大学附属", "偏差値": 69, "カテゴリ": "共学", "所在地": "文京区", "詳細": "護国寺"},
    {"順位": 3, "校名": "広尾学園", "偏差値": 66, "カテゴリ": "共学", "所在地": "港区", "詳細": "広尾"},
    {"順位": 4, "校名": "慶應義塾中等部", "偏差値": 65, "カテゴリ": "共学", "所在地": "港区", "詳細": "三田"},
    {"順位": 5, "校名": "早稲田実業学校", "偏差値": 65, "カテゴリ": "共学", "所在地": "国分寺市", "詳細": "国分寺"},
    {"順位": 6, "校名": "芝浦工業大学附属", "偏差値": 62, "カテゴリ": "共学", "所在地": "江東区", "詳細": "豊洲"},
    {"順位": 7, "校名": "三田国際学園", "偏差値": 61, "カテゴリ": "共学", "所在地": "世田谷区", "詳細": "用賀"},
]

# --- 大学データ (規格統一) ---
univ_data = [
    {"順位": 1, "校名": "東京大学", "偏差値": 73, "所在地": "文京区", "詳細": "本郷キャンパス"},
    {"順位": 2, "校名": "一橋大学", "偏差値": 68, "所在地": "国立市", "詳細": "国立キャンパス"},
    {"順位": 3, "校名": "東京工業大学", "偏差値": 67, "所在地": "目黒区", "詳細": "大岡山キャンパス"},
    {"順位": 4, "校名": "早稲田大学", "偏差値": 67, "所在地": "新宿区", "詳細": "早稲田キャンパス"},
    {"順位": 5, "校名": "慶應義塾大学", "偏差値": 67, "所在地": "港区", "詳細": "三田キャンパス"},
    {"順位": 6, "校名": "上智大学", "偏差値": 65, "所在地": "千代田区", "詳細": "四ツ谷キャンパス"},
    {"順位": 7, "校名": "東京外国語大学", "偏差値": 64, "所在地": "府中市", "詳細": "府中キャンパス"},
]

ward_list = [
    "千代田区", "中央区", "港区", "新宿区", "文京区", "台東区", "墨田区", "江東区", "品川区", 
    "目黒区", "大田区", "世田谷区", "渋谷区", "中野区", "杉並区", "豊島区", "北区", 
    "荒川区", "板橋区", "練馬区", "足立区", "葛飾区", "江戸川区", 
    "武蔵野市", "国分寺市", "国立市", "府中市"
]

# --- ロジック ---
df_mid = pd.DataFrame(school_data)
df_univ = pd.DataFrame(univ_data)

def get_star_name(w):
    c = len(df_mid[df_mid["所在地"] == w]) + len(df_univ[df_univ["所在地"] == w])
    return f"{w}{'★' * c}"

ward_options = [get_star_name(w) for w in ward_list]

def show_centered_table(df):
    # 表示用の列名を統一して出力
    display_df = df[["順位", "校名", "偏差値", "所在地", "詳細"]]
    display_df.columns = ["順位", "校名", "偏差値", "所在地", "最寄り/キャンパス"]
    st.write(display_df.to_html(index=False, escape=False, justify='center'), unsafe_allow_html=True)

# 1. 📍 エリア選択
st.write("### 📍 エリアを選択して教育情報をチェック")
selected_option = st.selectbox("自治体を選択", ward_options, index=4, label_visibility="collapsed")
selected_ward_raw = selected_option.split("★")[0]

st.markdown(f"""
    <div class="highlight-box">
        <h3 style="margin-top:0; color:#1a365d;">{selected_option} の教育資源</h3>
        <p>選択されたエリアに所在する難関校（中学・大学）を抽出しています。</p>
    </div>
""", unsafe_allow_html=True)

# 選択区の一覧（復活＆規格統一）
local_mids = df_mid[df_mid["所在地"] == selected_ward_raw]
local_univs = df_univ[df_univ["所在地"] == selected_ward_raw]

if not local_mids.empty:
    st.markdown(f'<div class="sub-table-title">✨ {selected_ward_raw}内の難関中学校</div>', unsafe_allow_html=True)
    show_centered_table(local_mids)

if not local_univs.empty:
    st.markdown(f'<div class="sub-table-title">🎓 {selected_ward_raw}内の難関大学</div>', unsafe_allow_html=True)
    show_centered_table(local_univs)

st.markdown("---")

# 2. 🏆 中学ランキング（常時表示・規格統一）
st.markdown('<div class="table-title">🏆 東京都 難関私立中学ランキング</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<p style="color:#3498db; font-weight:bold; text-align:center;">🟦 男子校 TOP7</p>', unsafe_allow_html=True)
    show_centered_table(df_mid[df_mid["カテゴリ"] == "男子校"].sort_values("順位"))
with col2:
    st.markdown('<p style="color:#e91e63; font-weight:bold; text-align:center;">🟥 女子校 TOP7</p>', unsafe_allow_html=True)
    show_centered_table(df_mid[df_mid["カテゴリ"] == "女子校"].sort_values("順位"))
with col3:
    st.markdown('<p style="color:#9b59b6; font-weight:bold; text-align:center;">🟪 共学 TOP7</p>', unsafe_allow_html=True)
    show_centered_table(df_mid[df_mid["カテゴリ"] == "共学"].sort_values("順位"))

# 3. 🎓 大学ランキング（常時表示・規格統一）
st.markdown('<div class="table-title">🎓 東京都 難関大学偏差値ランキング TOP7</div>', unsafe_allow_html=True)
show_centered_table(df_univ)
