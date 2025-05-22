import streamlit as st
import pandas as pd

# ページ設定
st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# サイドバー
with st.sidebar:
    st.title("Streamlit Demo")
    st.write("このアプリは様々なStreamlit機能のデモです")
    
    # ナビゲーション
    st.subheader("ナビゲーション")
    st.page_link("app.py", label="🏠 ホーム")
    st.page_link("pages/page1.py", label="📊 データ可視化")
    st.page_link("pages/page2.py", label="📝 データ編集")
    st.page_link("pages/page4.py", label="📋 フォーム")
    
    # 外部リンク
    st.divider()
    st.caption("参考リンク")
    st.page_link("https://docs.streamlit.io/develop/api-reference", label="🔗 Streamlit APIドキュメント")

# メインコンテンツ
st.title("Streamlit デモアプリケーション 👋")
st.markdown("""
このアプリケーションはStreamlitの様々な機能をデモンストレーションします。
サイドバーから各ページに移動して、それぞれの機能を試してみてください。
""")

# タブを使った基本デモ
tab1, tab2, tab3 = st.tabs(["テキスト表示", "データ表示", "スタイル例"])

with tab1:
    st.header("テキスト表示", divider="rainbow")
    
    st.subheader("基本的なテキスト")
    st.write("Hello World")
    st.write("Hello :blue[World]")
    
    st.subheader("コード表示")
    code = """
    import streamlit as st
    
    st.title("Hello Streamlit")
    st.write("This is a simple Streamlit app")
    """
    st.code(code, language="python")

with tab2:
    st.header("データ表示")
    
    st.subheader("シンプルなデータフレーム")
    df = pd.DataFrame({
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    })
    st.write(df)
    
    st.subheader("インタラクティブな表示")
    with st.expander("データフレームの詳細を見る"):
        st.dataframe(df, use_container_width=True)
        st.info("サイドバーのナビゲーションから「データ編集」ページに移動すると、より高度なデータ操作が可能です")

with tab3:
    st.header("UI要素とスタイル")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("カラムレイアウト")
        st.write("これはカラム1です")
        
        if st.button("通知を表示"):
            st.toast("通知が表示されました！")
            st.balloons()
    
    with col2:
        st.subheader("ポップオーバー")
        with st.popover("詳細を表示"):
            st.write("ポップオーバーの中身です")
            st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)

# フッター
st.divider()
st.caption("Streamlitデモアプリケーション © 2025")