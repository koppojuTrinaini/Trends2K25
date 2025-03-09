import streamlit as st  

# Page Configuration
st.set_page_config(page_title="Landing Page", page_icon="🌍", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
        .big-font { font-size:35px !important; font-weight: bold; color: #2E7D32; }
        .small-font { font-size:20px !important; color: #666; }
        .center-text { text-align: center; }
        .stButton>button { background-color: #2E7D32; color: white; font-size: 20px; }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 class='center-text'>🚀 Welcome to Our Landing Page</h1>", unsafe_allow_html=True)
st.markdown("<p class='center-text small-font'>A simple and elegant landing page built with Streamlit.</p>", unsafe_allow_html=True)

# Call-to-Action Button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Get Started 🚀"):
    st.success("Thank you for joining us!")
st.markdown("</div>", unsafe_allow_html=True)

# Features Section
st.markdown("---")
st.subheader("✨ Features")
st.write("- Simple and Clean UI")
st.write("- Mobile Responsive Design")
st.write("- Fast and Lightweight")
st.write("- Customizable with Python")

# About Section
st.markdown("---")
st.subheader("📌 About Us")
st.write("We help businesses create interactive and engaging web applications using Python and Streamlit.")

# Contact Section
st.markdown("---")
st.subheader("📩 Contact Us")
st.write("📧 Email: contact@yourwebsite.com")
st.write("🌐 Website: [YourWebsite](https://yourwebsite.com)")
st.write("📍 Location: Hyderabad, India")

# Footer
st.markdown("---")
st.markdown("<p class='center-text small-font'>© 2025 Your Company. All Rights Reserved.</p>", unsafe_allow_html=True)
