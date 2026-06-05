import streamlit as st
from data import load_data
from filters import get_category_filters
from charts import plot_top_10_majors, plot_employment_vs_earnings, plot_gender_vs_earnings

# Configuration
st.set_page_config(page_title="College Majors Dashboard", layout="wide")

# Load data
df = load_data()

st.title("🎓 US College Majors Dashboard")
st.markdown("An interactive dashboard analyzing 173 US college majors based on median earnings, employment rates, and gender breakdown.")

# Get sidebar filters
selected_categories = get_category_filters(df)

if not selected_categories:
    st.warning("Please select at least one major category from the sidebar.")
    st.stop()

# Filter data
filtered_df = df[df['Major_category'].isin(selected_categories)]

# -----------------
# Visualization 1: Top 10 Majors by Median Earnings
# -----------------
plot_top_10_majors(filtered_df)

st.markdown("---")

col1, col2 = st.columns(2)

# -----------------
# Visualization 2: Employment vs Unemployment Rate
# -----------------
with col1:
    plot_employment_vs_earnings(filtered_df)

# -----------------
# Visualization 3: Gender Breakdown
# -----------------
with col2:
    plot_gender_vs_earnings(filtered_df)

st.markdown("---")
st.markdown("Data Source: [FiveThirtyEight College Majors Dataset](https://github.com/fivethirtyeight/data/tree/master/college-majors)")
