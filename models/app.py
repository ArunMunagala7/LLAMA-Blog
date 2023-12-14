import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")
