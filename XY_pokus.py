import streamlit as st
# "/Users/eliskakafkova/Library/Mobile Documents/com~apple~CloudDocs/Datová analýza/04_Python/projekt/XY_pokus.py"
# streamlit run XY_pokus.py

col1, col2 = st.columns([2, 1])
with col1:
    st.metric("Příjem", "250 000 Kč", "+10 %")
with col2:
    st.metric("Náklady", "180 000 Kč", "-5 %")

with st.expander("Zobrazit více"):
    st.write("Toto je rozbalitelná sekce.")

    st.title("Moje první aplikace")
    st.write("Toto je jednoduchá Streamlit aplikace.")
    st.title("Název")

st.header("Hlavní nadpis")

st.subheader("Podnadpis")

st.text("Obyčejný text")

st.markdown("**Markdown** podpora")



