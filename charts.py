import streamlit as st
import plotly.express as px

def plot_top_10_majors(filtered_df):
    st.subheader("Top 10 Majors by Median Earnings (Filtered Categories)")
    top_10 = filtered_df.nlargest(10, 'Median')
    fig1 = px.bar(
        top_10, 
        x='Median', 
        y='Major', 
        orientation='h', 
        color='Major_category', 
        title="Top 10 Majors by Median Earnings",
        text_auto='.2s'
    )
    fig1.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig1, use_container_width=True)

def plot_employment_vs_earnings(filtered_df):
    st.subheader("Earnings vs. Unemployment Rate")
    fig2 = px.scatter(
        filtered_df, 
        x='Unemployment_rate', 
        y='Median', 
        size='Total', 
        color='Major_category', 
        hover_name='Major', 
        title="Median Earnings vs Unemployment Rate",
        labels={"Unemployment_rate": "Unemployment Rate", "Median": "Median Earnings ($)"}
    )
    fig2.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig2, use_container_width=True)

def plot_gender_vs_earnings(filtered_df):
    st.subheader("Gender Breakdown vs. Earnings")
    fig3 = px.scatter(
        filtered_df, 
        x='ShareWomen', 
        y='Median', 
        size='Total', 
        color='Major_category', 
        hover_name='Major', 
        title="Median Earnings vs Share of Women",
        labels={"ShareWomen": "Share of Women (0.0 to 1.0)", "Median": "Median Earnings ($)"}
    )
    fig3.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig3, use_container_width=True)
