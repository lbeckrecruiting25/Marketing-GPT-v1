import pandas as pd
import streamlit as st

# Load the content calendar
def load_content_calendar():
    file_path = "/mnt/data/Its the Final Countdown.xlsx"
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name="Content Calendar")
    df["date"] = pd.to_datetime(df["date"])
    return df

# Function to get content templates
def get_template(platform, theme):
    templates = {
        "LinkedIn": {
            "Cyber & Risk": "Is your SaaS startup secure? Enterprise clients expect SOC 2, HIPAA, or ISO 27001 before signing contracts. Proactive compliance is a competitive advantage. #CyberSecurity #SaaSCompliance",
            "Finance & Accounting": "Why most SaaS startups struggle with cash flow: Burn rate, runway forecasting, and financial visibility are key to investor confidence. Do you have a solid finance strategy? #SaaSFinance #StartupFunding",
        },
        "Twitter": {
            "Cyber & Risk": "SaaS founders: Enterprise clients expect SOC 2, HIPAA, or ISO 27001 before signing contracts. Compliance isn’t just a checkbox—it’s a revenue driver. #CyberSecurity #SaaSCompliance",
            "Finance & Accounting": "Runway is everything. If your burn rate is $50K/month with $200K in the bank, you have 4 months left. A fractional CFO can help extend that runway. Need a cash flow tracker? #SaaSFinance #StartupGrowth",
        }
    }
    return templates.get(platform, {}).get(theme, "No template available for this selection.")

# Streamlit UI
def content_creator():
    st.title("HiveBridge Content Selection Tool")
    
    # Load calendar
    df = load_content_calendar()
    
    # Select topic
    selected_row = st.selectbox("Select a content topic:", df.index)
    selected_data = df.iloc[selected_row]
    
    # Show details
    st.write("### Selected Content Details")
    st.write(f"**Platform:** {selected_data['platform']}")
    st.write(f"**Theme:** {selected_data['theme']}")
    st.write(f"**Topic:** {selected_data['topic']}")
    
    # Generate content
    template = get_template(selected_data['platform'], selected_data['theme'])
    content = st.text_area("Generated Content", template, height=200)
    
    # Edit content
    if st.button("Save & Export"):
        with open("/mnt/data/generated_content.txt", "w") as f:
            f.write(content)
        st.success("Content saved successfully!")

# Run Streamlit app
if __name__ == "__main__":
    content_creator()
