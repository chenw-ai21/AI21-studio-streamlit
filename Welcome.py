import streamlit as st
from utils.studio_style import apply_studio_style


if __name__ == '__main__':
    st.set_page_config(
        page_title="Welcome"
    )
    apply_studio_style()
    st.title("Welcome to AI21 Studio demos")
    st.markdown("Experience the incredible power of AI21's large language models first-hand. With these demos, you can explore a variety of unique use cases, from instant content generation to paraphraser that rewrite text." )
    st.markdown("If you're interested in learning more, sign up for a free trial account here: https://www.ai21.com/studio, or contact us at studio@ai21.com")
