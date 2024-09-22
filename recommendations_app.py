import streamlit as st
import recommendations_lib as rlib  # reference to local lib script

st.set_page_config(page_title="OpenAI Services Recommendations", layout="wide")
st.title("OpenAI Services Recommendations")

input_text = st.text_input("What kind of AI capabilities are you looking for?")
go_button = st.button("Get Recommendations", type="primary")

if go_button:
    with st.spinner("Analyzing your requirements..."):
        response_content = rlib.get_similarity_search_results(question=input_text)
        
        for result in response_content:
            st.markdown(f"### [{result['name']}]({result['url']})")
            st.write(result['summary'])
            with st.expander("Service Description"):
                st.write(result['original'])

st.sidebar.markdown("""
## About
This app provides personalized recommendations for OpenAI services based on your requirements.
Simply enter what you're looking for, and we'll suggest the most relevant OpenAI services.
""")