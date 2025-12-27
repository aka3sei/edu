import streamlit as st
import pandas as pd

# 1. ページ設定
st.set_page_config(page_title="教育環境ナビ", layout="wide")

# CSS: デザイン調整
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
    table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
    th { background-color: #f2f2f2; text-align: center !important; padding: 12px; font-size: 14px; border-bottom: 2px solid #ddd; }
    td { border-bottom: 1px solid #ddd; padding: 10px; text-align: center !important; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🏫 東京 難関校・教育環境完全ガイド</div>', unsafe_allow_html=True)

# --- データ定義 ---
school_data = [
    {"順位": 1, "学校名": "開成中学校", "偏差値": 72, "カテゴリ": "男子校", "所在地": "荒川区", "最寄り": "西日暮里"},
    {"順位": 2, "学校名": "麻布中学校", "偏差値": 68, "カテゴリ": "男子校", "所在地": "港区", "最寄り": "広尾"},
    {"順位": 3, "学校名": "駒場東邦中学校", "偏差値": 67, "カテゴリ": "男子校", "所在地": "世田谷区", "最寄り": "駒場東大前"},
    {"順位": 4, "学校名": "武蔵中学校", "偏差値": 65, "カテゴリ": "男子校", "所在地": "練馬区", "最寄り": "江古田"},
    {"順位": 5, "学校名": "海城中学校", "偏差値": 64, "カテゴリ": "男子校", "所在地": "新宿区", "最寄り": "新大久保"},
    {"順位": 6, "学校名": "早稲田中学校", "偏差値": 64, "カテゴリ": "男子校", "所在地": "新宿区", "最寄り": "早稲田"},
    {"順位": 7, "学校名": "本郷中学校", "偏差値": 60, "カテゴリ": "男子校", "所在地": "豊島区", "最寄り": "巣鴨"},
    {"順位": 1, "学校名": "桜蔭中学校", "偏差値": 71, "カテゴリ": "女子校", "所在地": "文京区", "最寄り": "水道橋"},
    {"順位": 2, "学校名": "女子学院中学校", "偏差値": 69, "カテゴリ": "女子校", "所在地": "千代田区", "最寄り": "市ヶ谷"},
    {"順位": 3, "学校名": "豊島岡女子学園", "偏差値": 68, "カテゴリ": "女子校", "所在地": "豊島区", "最寄り": "池袋"},
    {"順位": 4, "学校名": "雙葉中学校", "偏差値": 67, "カテゴリ": "女子校", "所在地": "千代田区", "最寄り": "四ツ谷"},
    {"順位": 5, "学校名": "白百合学園", "偏差値": 64, "カテゴリ": "女子校", "所在地": "千代田区", "最寄り": "九段下"},
    {"順位": 6, "学校名": "吉祥女子中学校", "偏差値": 63, "カテゴリ": "女子校", "所在地": "武蔵野市", "最寄り": "吉祥寺"},
    {"順位": 7, "学校名": "鴎友学園女子", "偏差値": 62, "カテゴリ": "女子校", "所在地": "世田谷区", "最寄り": "宮の坂"},
    {"順位": 1, "学校名": "渋谷教育学園渋谷", "偏差値": 70, "カテゴリ": "共学", "所在地": "渋谷区", "最寄り": "渋谷"},
    {"順位": 2, "学校名": "筑波大学附属", "偏差値": 69, "カテゴリ": "共学", "所在地": "文京区", "最寄り": "護国寺"},
    {"順位": 3, "学校名": "広尾学園", "偏差値": 66, "カテゴリ": "共学", "所在地": "港区", "最寄り": "広尾"},
    {"順位": 4, "学校名": "慶應義塾中等部", "偏差値": 65, "カテゴリ": "共学", "所在地": "港区", "最寄り": "三田"},
    {"順位": 5, "学校名": "早稲田実業学校", "偏差値": 65, "カテゴリ": "共学", "所在地": "国分寺市", "最寄り": "国分寺"},
    {"順位": 6, "学校名": "芝浦工業大学附属", "偏差値": 62, "カテゴリ": "共学", "所在地": "江東区", "最寄り": "豊洲"},
    {"順位": 7, "学校名": "三田国際学園", "偏差値": 61, "カテゴリ": "共学", "所在地": "世田谷区", "最寄り": "用賀"},
]

univ_data = [
    {"順位": 1, "大学名": "東京大学", "偏差値": 73, "キャンパス": "本郷(文京区)", "所在地": "文京区"},
    {"順位": 2, "大学名": "一橋大学", "偏差値": 68, "キャンパス": "国立(国立市)", "所在地": "国立市"},
    {"順位": 3, "大学名": "東京工業大学", "偏差値": 67, "キャンパス": "大岡山(目黒区)", "所在地": "目黒区"},
    {"順位": 4, "大学名": "早稲田大学", "偏差値": 67, "キャンパス": "早稲田(新宿区)", "所在地": "新宿区"},
    {"順位": 5, "大学名": "慶應義塾大学", "偏差値": 67, "キャンパス": "三田(港区)", "所在地": "港区"},
    {"順位": 6, "大学名": "上智大学", "偏差値": 65, "キャンパス": "四ツ谷(千代田区)", "所在地": "千代田区"},
    {"順位": 7, "大学名": "東京外国語大学", "偏差値": 64, "キャンパス": "府中(府中市)", "所在地": "府中市"},
]

# 自治体基本データ（省略版）
ward_list = [
    "千代田区", "中央区", "港区", "新宿区", "文京区", "台東区", "墨田区", "江東区", "品川区", 
    "目黒区", "大田区", "世田谷区", "渋谷区", "中野区", "杉並区", "豊島区", "北区", 
    "荒川区", "板橋区", "練馬区", "足立区", "葛飾区", "江戸川区", 
    "武蔵野市", "国分寺市", "国立市", "府中市"
]

ward_info_map = {
    "千代田区": {"特色": "ICT教育先進。九段中等教育学校が人気。", "支援": "次世代育成手当月5000円。"},
    "中央区": {"特色": "晴海校舎新設。放課後プレディ全校実施。", "支援": "第2子以降保育料無償。"},
    "港区": {"特色": "英語教育注力。御三家の一角、麻布がある。", "支援": "出産助成最大60万円。"},
    "新宿区": {"特色": "海城・早稲田など名門男子校が集まる。", "支援": "子どもショートステイ。"},
    "文京区": {"特色": "教育の府。東大・桜蔭・筑附を擁する。", "支援": "文京区版ネウボラ。"},
    "目黒区": {"特色": "東工大がある文教地区。思考力可視化教育。", "支援": "支援センター「ほっぺ」。"},
    "世田谷区": {"特色": "駒東・三田国際など難関校が多い住宅街。", "支援": "せたがや子育て利用券。"},
    "豊島区": {"特色": "豊島岡・本郷がある。スキップ学習支援。", "支援": "第2子以降保育料無償。"},
    "荒川区": {"特色": "開成中を擁する。読書のまち。学力上昇。", "支援": "塾代助成（中学生）。"},
    "練馬区": {"特色": "武蔵中を擁する。公立校数最多で安定。", "支援": "第3子祝金10万円。"},
    "武蔵野市": {"特色": "文教都市。吉祥女子がある。地域見守り強固。", "支援": "独自の教育相談体制。"},
    "国分寺市": {"特色": "早稲田実業がある。理数フィールド学習。", "支援": "子育てアプリ充実。"},
    "国立市": {"特色": "一橋大を擁する。景観・教育への意識が高い。", "支援": "産前産後ケア充実。"},
    "府中市": {"特色": "東京外大がある。スポーツ・教育の融合。", "支援": "経済的支援の安定。"},
    # 他の区はデフォルト表示（必要に応じ追加可能）
}

# --- ロジック ---
df_mid = pd.DataFrame(school_data)
df_univ = pd.DataFrame(univ_data)

# 星付き名称の生成
def get_star_name(w):
    c = len(df_mid[df_mid["所在地"] == w]) + len(df_univ[df_univ["所在地"] == w])
    return f"{w}{'★' * c}"

ward_options = [get_star_name(w) for w in ward_list]

# 共通表示関数
def show_centered_table(df):
    st.write(df.to_html(index=False, escape=False, justify='center'), unsafe_allow_html=True)

# 1. 📍 エリア選択
st.write("### 📍 エリアを選択して教育情報をチェック")
selected_option = st.selectbox("自治体を選択", ward_options, index=4, label_visibility="collapsed")
selected_ward_raw = selected_option.split("★")[0]

# 自治体情報表示
info = ward_info_map.get(selected_ward_raw, {"特色": "ICT教育や地域連携を推進。", "支援": "各ライフステージに合わせた支援。"})
st.markdown(f"""
    <div class="highlight-box">
        <h3 style="margin-top:0; color:#1a365d;">{selected_option} の教育・子育て</h3>
        <p><b>■ 教育特色:</b> {info['特色']}</p>
        <p><b>■ 独自支援:</b> {info['支援']}</p>
    </div>
""", unsafe_allow_html=True)

# 選択された区の学校一覧（復活）
local_mids = df_mid[df_mid["所在地"] == selected_ward_raw]
local_univs = df_univ[df_univ["所在地"] == selected_ward_raw]

if not local_mids.empty:
    st.markdown(f'<div class="sub-table-title">✨ {selected_ward_raw}内の難関中学校</div>', unsafe_allow_html=True)
    show_centered_table(local_mids[["順位", "学校名", "偏差値", "カテゴリ", "最寄り"]])

if not local_univs.empty:
    st.markdown(f'<div class="sub-table-title">🎓 {selected_ward_raw}内の難関大学</div>', unsafe_allow_html=True)
    show_centered_table(local_univs[["順位", "大学名", "偏差値", "キャンパス"]])

st.markdown("---")

# 2. 🏆 中学ランキング（常時表示）
st.markdown('<div class="table-title">🏆 東京都 難関私立中学ランキング</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<p style="color:#3498db; font-weight:bold; text-align:center;">🟦 男子校 TOP7</p>', unsafe_allow_html=True)
    show_centered_table(df_mid[df_mid["カテゴリ"] == "男子校"].sort_values("順位")[["順位", "学校名", "偏差値"]])
with col2:
    st.markdown('<p style="color:#e91e63; font-weight:bold; text-align:center;">🟥 女子校 TOP7</p>', unsafe_allow_html=True)
    show_centered_table(df_mid[df_mid["カテゴリ"] == "女子校"].sort_values("順位")[["順位", "学校名", "偏差値"]])
with col3:
    st.markdown('<p style="color:#9b59b6; font-weight:bold; text-align:center;">🟪 共学 TOP7</p>', unsafe_allow_html=True)
    show_centered_table(df_mid[df_mid["カテゴリ"] == "共学"].sort_values("順位")[["順位", "学校名", "偏差値"]])

# 3. 🎓 大学ランキング（常時表示・中学の下に配置）
st.markdown('<div class="table-title">🎓 東京都 難関大学偏差値ランキング TOP7</div>', unsafe_allow_html=True)
show_centered_table(df_univ[["順位", "大学名", "偏差値", "キャンパス"]])
