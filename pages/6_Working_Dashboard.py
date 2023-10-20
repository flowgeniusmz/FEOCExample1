import streamlit as st
import hydralit_components as hc
from functions.hydralit_infocard import get_infocard_theme
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview, set_title_no_divider
import datetime


st.set_page_config(layout="wide", initial_sidebar_state="collapsed",)

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    
        
    #Set initial page layout
    #set_title_no_divider("FEOC", "Working Dashboard")
    #set_page_overview("Overview", "This section of the management portal focuses on experimental features")
    #set navbar
    menu_data = [
        {'icon': "far fa-copy", 'label':"Left End"},
        {'id':'Copy','icon':"🐙",'label':"Copy"},
        {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
        {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
        {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
        {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
        {'icon': "far fa-copy", 'label':"Right End"},
        {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
    ]
    over_theme = {'txc_inactive': '#FFFFFF'}
    menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        login_name='Logout',
        hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
    )
    set_title("FEOC", "Working")
    set_page_overview("Overview", "This section of the management portal focuses on experimental features")

    #get the id of the menu item clicked
    st.info(f"{menu_id}")
    st.divider()

    
    #get infocard themes
    infocard_theme_good = get_infocard_theme("good")
    infocard_theme_neutral = get_infocard_theme("neutral")
    infocard_theme_bad = get_infocard_theme("bad")

    #set next page layout -- container with columns
    container1 = st.container()
    with container1:
        cc = st.columns(4)
        with cc[0]:
            hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good',bar_value=77, title_text_size="1rem", content_text_size=".9rem", icon_size="1rem")
        with cc[1]:
            hc.info_card(title='Some BAD BAD', content='This is really bad',bar_value=12,theme_override=infocard_theme_bad, title_text_size="1rem", content_text_size=".9rem", icon_size="1rem")
        with cc[2]:
            hc.info_card(title='Some NEURAL', content='Oh yeah, sure.', sentiment='neutral',bar_value=55, title_text_size="1rem", content_text_size=".9rem", icon_size="1rem")
        with cc[3]:
            hc.info_card(title='Some NEURAL',content='Maybe...',key='sec',bar_value=5,theme_override=infocard_theme_neutral, title_text_size="1rem", content_text_size=".9rem", icon_size="1rem")

    # divide sections
    st.divider()

    # hydralit option bar

    container2=st.container()
    with container2:
        option_data = [
            {'icon': "bi bi-hand-thumbs-up", 'label':"Agree"},
            {'icon':"fa fa-question-circle",'label':"Unsure"},
            {'icon': "bi bi-hand-thumbs-down", 'label':"Disagree"},
        ]
        op = hc.option_bar(option_definition=option_data, title="Feedback Response", key="PrimaryOption", horizontal_orientation=True)

    #divide sections
    st.divider()
    #hyralit progress bar

    container3 = st.container()
    with container3:
        # can apply customisation to almost all the properties 0f the progress ba
        override_theme_1 = {'bgcolor': '#EFF8F7','progress_color': 'green'}
        override_theme_2 = {'bgcolor': 'green','content_color': 'white','progress_color': 'red'}
        override_theme_3 = {'content_color': 'red','progress_color': 'orange'}

        # can just use 'good', 'bad', 'neutral' sentiment to auto color the bar
        hc.progress_bar(25,'Something something')
        hc.progress_bar(35,'Something something',sentiment='good')
        hc.progress_bar(95,'Something something',sentiment='neutral')
        hc.progress_bar(47,'Something something',sentiment='bad')

        # customise the the theming for a neutral content
        hc.progress_bar(5,'Something something - 1a',key='pa1',override_theme=override_theme_1)
        hc.progress_bar(35,'Something something - 2a',key='pa2',sentiment='good',override_theme=override_theme_2)
        hc.progress_bar(95,'Something something - 3a',key='pa3',sentiment='neutral')
        hc.progress_bar(47,'Something something - 4a',key='pa4',sentiment='bad',override_theme=override_theme_3)