import streamlit as st

st.title("🎛️ NPS Streamlit Widgets Demo")

# --- Text Input ---
name = st.text_input("What's your name?")

# --- Number Input ---
age = st.number_input("How old are you?", min_value=0, max_value=100, step=1)

# --- Slider ---
height = st.slider("Your height (cm)", 100, 250, 170)

# --- Text Area ---
bio = st.text_area("Tell us about yourself:")

# --- Checkbox ---
agree = st.checkbox("I agree to the terms and conditions")

# --- Radio Buttons ---
gender = st.radio("Gender", ["Male", "Female", "Other"])

# --- Select Box ---
country = st.selectbox("Choose your country", ["USA", "Canada", "UK", "Thailand", "Other"])

# --- Multi-select ---
hobbies = st.multiselect("Select your hobbies", ["Reading", "Gaming", "Traveling", "Coding", "Cooking"])

# --- Date Input ---
dob = st.date_input("Your Date of Birth")

# --- Time Input ---
wake_time = st.time_input("When do you wake up?")

# --- File Uploader ---
uploaded_file = st.file_uploader("Upload a file")

# --- Color Picker ---
fav_color = st.color_picker("Pick your favorite color", "#00f900")

# --- Button ---
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old, and you selected {gender}.")
    st.write("📋 Your Bio:", bio)
    st.write("🌍 Country:", country)
    st.write("📅 DOB:", dob)
    st.write("🕒 Wake Time:", wake_time)
    st.write("🎨 Favorite Color:", fav_color)
    st.write("✅ Agreement:", agree)
    st.write("🎯 Hobbies:", hobbies)
    if uploaded_file:
        st.write("📁 Uploaded File Name:", uploaded_file.name)

# --- Display Code Section ---
with st.expander("🔍 See the code"):
    st.code(open(__file__, encoding="utf-8").read(), language='python')

