import streamlit as st
import hydralit_components as hc
#https://github.com/flowgeniusmz/hydralit_components

option_data = [
    {'icon': "bi bi-hand-thumbs-up", 'label':"Agree"},
    {'icon':"fa fa-question-circle",'label':"Unsure"},
    {'icon': "bi bi-hand-thumbs-down", 'label':"Disagree"},
    ]

# define what option labels and icons to display
def hy_optionbar_get_option_data():
    option_data1 = [
    {'icon': "bi bi-hand-thumbs-up", 'label':"Agree"},
    {'icon':"fa fa-question-circle",'label':"Unsure"},
    {'icon': "bi bi-hand-thumbs-down", 'label':"Disagree"},
    ]
    return option_data1

# override the theme, else it will use the Streamlit applied theme
over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}
font_fmt = {'font-class':'h2','font-size':'150%'}

# display a horizontal version of the option bar
op = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

# display a version version of the option bar
op2 = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=False)
