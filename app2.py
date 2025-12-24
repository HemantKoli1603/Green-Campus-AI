import streamlit as st

st.markdown("Hellooo cuties")
img_file = st.camera_input("Gimme a photo of you")

if img_file==True:
    st.spinner("Generating environmental insight...")
    st.progress(float(3+3))

st.caption("THis is developd by hemant")
