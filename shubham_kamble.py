import streamlit as st
import os

def main():

    cover_photo_path = "cover_image.png"
    st.image(cover_photo_path, use_column_width=True)

    #st.title("Shubham Dipak Kamble's Portfolio")

    
    st.sidebar.subheader("Contact Information")
        # ... (rest of the sidebar content) ...

    st.sidebar.markdown("<style>div.sidebar-content { position: sticky; top: 0; }</style>", unsafe_allow_html=True)

    st.sidebar.subheader("Contact Information")
    st.sidebar.markdown("Email: shubhamkamble7003@gmail.com\n\nContact No: 7972799088\n\nLocation: Pune, India")

    st.sidebar.markdown("### Bio")
    st.sidebar.markdown("I am a data analyst specializing in creating impactful visualizations using Power BI. I am proficient in utilizing tools such as MySQL for data manipulation and have a solid grasp of Python for data analysis. I am enthusiastic about generative AI tools and skilled in building web applications using Streamlit and ChatGPT.")
    st.sidebar.markdown("### Profile Links")
    st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/shubham-kamble-9b0867172/)")
    st.sidebar.markdown("[YouTube](https://www.youtube.com/@shubhamkamble6914/featured)")
    st.sidebar.markdown("[Google Cloud](https://www.cloudskillsboost.google/public_profiles/5903b42b-5480-45dd-8f48-397969e4baac)")
    st.sidebar.markdown("[GitHub](https://github.com/sdk1728)")

    st.subheader("Professional Experience")
    st.markdown("**Data Analyst Intern**")
    st.markdown("Yoshops.com")
    st.markdown("01/2023 to 03/2023")
    st.markdown("""• Conducted web scraping on multiple E-commerce websites such as Reliance Digital, Vijay Sales, Amazon, Flipkart, and
                    HRX to collect valuable data.
                    • Analysed the collected data to understand the sales trends and customer reviews.
                    • Developed a visually appealing and insightful Power-Bi dashboard to present the analysed data to stakeholders.
                    • Successfully communicated the key findings and recommendations to improve product sales and customer experience.""")


    st.subheader("Power Bi Dashboards")

    show_power_bi = st.checkbox("Toggle Power Bi Dashboards")
    if show_power_bi:

        st.markdown("**IPL 2023 PERFORMANCE ANALYSIS DASHBOARD**")
        st.image("1_IPL_2023_performance.png", use_column_width=True)
        st.markdown("[Project Link](https://app.powerbi.com/groups/me/reports/2264d214-3110-4b1c-bf21-bb71f449c8a3/ReportSection92d02be10568c4b08406?experience=power-bi)")

        st.markdown("**GLOBAL HEALTH TRENDS DASHBOARD**")
        st.image("2_Global_health_trends.png", use_column_width=True)
        st.markdown("[Project Link](https://app.powerbi.com/groups/me/reports/2264d214-3110-4b1c-bf21-bb71f449c8a3/ReportSection92d02be10568c4b08406?experience=power-bi)")

        st.markdown("**HR ANALYTICS DASHBOARD**")
        st.image("3_hr_dashboard.png", use_column_width=True)
        st.markdown("[Project Link](https://app.powerbi.com/groups/me/reports/a5679804-a04e-4ae0-b8c6-3caa1a2ecf7f/ReportSection56017c59a2cb935d47d6?experience=power-bi)")

        st.markdown("**CSK 2023 PERFORMANCE DASHBOARD**")
        st.image("4_csk_dashboard.png", use_column_width=True)
        st.markdown("[Project Link](https://app.powerbi.com/groups/me/reports/329f5904-59b2-4a42-ab0d-858898d7aa27/ReportSectioncc1ec483652de470007e?experience=power-bi)")

        st.markdown("**SALES ANALYSIS DASHBOARD**")
        st.image("5_Sales_analysis.png", use_column_width=True)
        st.markdown("[Project Link](https://app.powerbi.com/groups/me/reports/bcf7e1fb-f61d-4769-a01a-785e53a20435/ReportSection?experience=power-bi)")

        st.markdown("**AURANGABAD COLLEGES DASHBOARD**")
        st.image("6_Aurangabad_colleges.png", use_column_width=True)
        st.markdown("[Project Link](https://app.powerbi.com/groups/me/reports/bcf7e1fb-f61d-4769-a01a-785e53a20435/ReportSection?experience=power-bi)")

        st.markdown("**CUSTOMER CHURN ANALYSIS DASHBOARD**")
        st.image("7_Customer_churn_analysis.png", use_column_width=True)
        st.markdown("[Project Link](https://app.powerbi.com/groups/me/reports/bf05165c-724b-4fe3-b5ff-56ec4cceb4a3/ReportSection4ebc994c71084f50b69c?experience=power-bi)")

        st.markdown("**EMPLOYEE DIVERSITY & ANCLUSION ANALYSIS**")
        st.image("9_Employee_diversion.png", use_column_width=True)
        st.markdown("[Project Link](https://app.powerbi.com/groups/me/reports/3fe216eb-95ec-4905-9a86-6d7314717649/ReportSection305ebf502eb07cc690fc?experience=power-bi&clientSideAuth=0)")


    st.subheader("Python Projects")
    show_python_projects = st.checkbox("Toggle Python Projects")
    if show_python_projects:
        st.markdown("**1. CAR RESALE PRICE PREDICTION**")
        st.image("Car_resale_app.png", use_column_width=True)
        st.markdown("[Project Link](https://github.com/sdk1728/CAR_RESALEpPRICE_PREDICTOR)")

        st.markdown("**2. AMAZON SALES ANALYSIS WEB APP**")
        st.image("amazon_sales.png", use_column_width=False)
        st.markdown("[Project Link](https://amazonsales.streamlit.app/)")

        st.markdown("**3. SPOTIFY EXPLORATORY DATA ANALYSIS**")
        st.image("spotify_data_analysis.png", use_column_width=False)
        st.markdown("[Project Link](https://github.com/sdk1728/spotify_data_analysis)")

        st.markdown("**4. RESEARCH ON CARDIAC DISEASE**")
        st.image("Cardiac_disease.png", use_column_width=False)
        st.markdown("[Project Link](https://github.com/sdk1728/Data_analyst_projects/blob/main/Analyzing%20Research%20on%20Cardiac%20Diseases.ipynb)")

    






if __name__ == "__main__":
    main()