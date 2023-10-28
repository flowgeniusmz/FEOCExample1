import streamlit as st
from  functions.login import get_loginform, check_authentication
from functions.pagesetup import set_title_nodiv, set_title
from streamlit_modal import Modal
import streamlit.components.v1 as components
from functions.modals import modal_actions_sendemail, modal_home_demorequest
from functions.pageswitch import switchpage_ActionsPanel, switchpage_AnalyticsPanel, switchpage_AIPanel, switchpage_CentralPerformancePanel, switchpage_SensorPanel
from functions.styles import theme_expander_header_content, theme_fa_icons
from streamlit_lottie import st_lottie



st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

#if 'authenticated' not in st.session_state:
#    get_loginform()
#elif not st.session_state.authenticated:
#    get_loginform()
#else:
if check_authentication():

    set_title("FEOC", "Home")
    containera = st.container()
    with containera:
        st.markdown("#### Welcome to the Faulkner Emission Solutions Platform!")
        st.markdown("Introducing the **Faulkner Emission Offset Certificates (FEOCs)** - our benchmark for emission offset. These certificates not only validate and track environmental contributions but, with the aid of state-of-the-art AI technology, ensure their authenticity, accuracy, and completeness. Jump in, explore, and be the change you wish to see in the world! We are thrilled to have you join our mission. Whether you're an Emitter, a Provider, a Purchaser, or simply a champion for the environment, this platform aims to unify our collective efforts towards a greener planet.")
        #st.divider()
        st.markdown("**Emitters**")
        st.markdown("""```
                    You are the linchpin of emission reduction, driving us towards a sustainable future. Your investments empower Providers to innovate and bring forth solutions that battle against emissions.
                    """)
        st.markdown("**Providers**")
        st.markdown("""```
                    With your groundbreaking solutions, you are lighting the path to a brighter, cleaner future. By collaborating with Emitters, we are making strides in environmental conservation.
                    """)
        st.markdown("**Purchasers**")
        st.markdown("""```
                    By choosing to back reduced emission products, you set a commendable standard. Every purchase you make takes us one step closer to a cleaner, better world.
                    """)
        st.link_button("Visit Our Website", "https://faulknercapitalholdings.com/", type="primary", use_container_width=True)
        #modal1 = modal_home_demorequest()
        st.divider()
    containerb = st.container()
    with containerb:
        containerb1 = st.container()
        with containerb1:
            st.markdown("#### Navigating Your Faulkner Emission Offset Certificate")
            st.markdown("Your **Faulkner Emission Offset Certificate (FEOC)** - provides you with many capabilities related to your project. You can click the items below to navigate to them or use the side bar on the left.")
            #st.divider()
        
        containerb2 = st.container()
        with containerb2:
            theme_expander_header_content()
            theme_fa_icons()
            cc1 = st.columns(5)
            with cc1[0]:
                containerb21 = st.container()
                with containerb21:
                    st.markdown("""**Central Performance Panel** <i class="fas fa-tachometer-alt" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                    st.markdown("View an overview related to your FEOC.")
                    switchpage_CentralPerformancePanel()
            with cc1[1]:
                containerb22 = st.container()
                with containerb22:
                    st.markdown("""**Action Panel** <i class="fas fa-play-circle" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                    st.markdown("""Perform certificate-related actions.""")
                    #st.button("Click to view", key="btnAnalyticsPanel", type="primary", use_container_width=True, on_click=switch_page("Analytics Panel"))
                    switchpage_AnalyticsPanel()
            with cc1[2]:
                containerb23 = st.container()
                with containerb23:
                    st.markdown("""**Analytics Panel** <i class="fas fa-chart-line" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                    st.markdown("View **real-time** dashboards.")
                    switchpage_ActionsPanel()
            with cc1[3]:
                containerb24 = st.container()
                with containerb24:
                    st.markdown("""**AI Panel** <i class="fas fa-brain" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                    st.markdown("Interact with AI Autonomous Agents.")
                    switchpage_AIPanel()
            with cc1[4]:
                containerb25 = st.container()
                with containerb25:
                    st.markdown("""**Sensor Panel** <i class="fas fa-wave-square" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                    st.markdown("Interact with the IoT sensors.")
                    switchpage_SensorPanel()
                
    st.divider()
