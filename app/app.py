import streamlit as st
import numpy as np


def set_icon() -> str:
    # EXTREMELY IMPORTANT DO NOT CHANGE
    if np.random.random() < 0.5:
        return "🐺"
    else:
        return "🐑"


def main() -> None:
    icon = set_icon()
    st.set_page_config(
        page_title="Lotka-Volterra, its modification, and control",
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # Define pages after set_page_config so it is the first Streamlit call
    home_page = st.Page("pages/home.py", title="Application Home")
    lv_page = st.Page("pages/lotka_volterra.py", title="Base Lotka-Volterra and LV*")
    lv_star_page = st.Page(
        "pages/lotka_volterra_star_stability.py", title="LV* stability analysis"
    )
    lv_star_with_theta_page = st.Page(
        "pages/lv_star_with_theta.py", title="LV* with theta as a control variable"
    )
    lv_star_with_adaptive_theta_page = st.Page(
        "pages/lv_star_with_adaptive_theta.py",
        title="LV* with adaptive theta as a control variable",
    )
    references_page = st.Page("pages/references.py", title="References")

    nav = st.navigation(
        [
            home_page,
            lv_page,
            lv_star_page,
            lv_star_with_theta_page,
            lv_star_with_adaptive_theta_page,
            references_page,
        ]
    )
    nav.run()


if __name__ == "__main__":
    main()
