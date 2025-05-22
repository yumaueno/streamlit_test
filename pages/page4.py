import streamlit as st
import pandas as pd

st.title("フォームサンプル")

# 基本的なフォームの例
st.header("お問い合わせフォーム")

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("お名前")
        email = st.text_input("メールアドレス")
        phone = st.text_input("電話番号（任意）")
    
    with col2:
        category = st.selectbox(
            "お問い合わせ種別",
            ["製品について", "サービスについて", "料金について", "その他"]
        )
        priority = st.radio(
            "優先度",
            ["高", "中", "低"]
        )
    
    message = st.text_area("お問い合わせ内容", height=150)
    agreement = st.checkbox("プライバシーポリシーに同意します")
    
    submitted = st.form_submit_button("送信")
    
    if submitted:
        if not name or not email or not message or not agreement:
            st.error("必須項目を入力し、プライバシーポリシーに同意してください。")
        else:
            st.success(f"お問い合わせを受け付けました。{name}様、ありがとうございます！")
            st.write("入力内容:")
            st.write({
                "お名前": name,
                "メールアドレス": email,
                "電話番号": phone,
                "種別": category,
                "優先度": priority,
                "お問い合わせ内容": message
            })

# ファイルアップロードの例
st.header("ファイルアップロード")
uploaded_file = st.file_uploader("CSVファイルをアップロード", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("アップロードされたデータ:")
        st.dataframe(df)
        
        st.subheader("データの基本統計")
        st.write(df.describe())
        
        if st.checkbox("カラムの選択"):
            selected_columns = st.multiselect(
                "表示するカラムを選択",
                df.columns.tolist()
            )
            if selected_columns:
                st.write(df[selected_columns])
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

# 高度なフォーム要素の例
st.header("その他のフォーム要素")

col1, col2 = st.columns(2)

with col1:
    st.subheader("数値入力")
    number = st.number_input("数値を入力", min_value=0, max_value=100, value=50)
    st.progress(number / 100)
    
    st.subheader("日付選択")
    date = st.date_input("日付を選択")
    st.write(f"選択された日付: {date}")

with col2:
    st.subheader("スライダー")
    age = st.slider("年齢", 0, 100, 25)
    st.write(f"年齢: {age}歳")
    
    st.subheader("色選択")
    color = st.color_picker("色を選択", "#00f900")
    st.write(f"選択された色: {color}")
    st.markdown(f"<div style='background-color:{color};width:100%;height:50px;'></div>", unsafe_allow_html=True)

# フッター
st.divider()
st.caption("フォームサンプルページ © 2025")