import streamlit as st
import hydralit_components as hc

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
