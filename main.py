import streamlit as st 

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title ="Menu" ,
        options = ["Home","About","Contact"],
        icons =["house-heart-fill","calendar2-heart-fill","envelope-heart-fill"],
        default_index = 0,
    )


if selected == "Home":
    st.title(f"welcome to the {selected} page")

if selected == "About":
    st.title(f"welcome to the {selected} page")

if selected == "Contact":
    st.title(f"welcome to the {selected} page")


