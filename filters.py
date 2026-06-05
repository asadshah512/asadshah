import streamlit as st

def get_category_filters(df):
    st.sidebar.header("Filters")
    all_categories = df['Major_category'].unique()
    selected_categories = st.sidebar.multiselect(
        "Select Major Categories", 
        options=all_categories, 
        default=all_categories[:8]
    )
    return selected_categories
