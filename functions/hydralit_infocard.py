import streamlit as st
import hydralit_components as hc

theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

def get_infocard_theme(varChoice):
    if varChoice == "good":
        return_theme = theme_good
    elif varChoice == "neutral":
        return_theme = theme_neutral
    elif varChoice == "bad":
        return_theme = theme_bad
    else:
        return_theme = theme_neutral

    return return_theme
