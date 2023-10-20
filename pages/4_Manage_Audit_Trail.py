import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview
import extra_streamlit_components as stx
from functions.audit_data import load_audit_data
from functions.supabase_queries import run_query, supabase_get_audit
from functions.filter_dataframe import filter_dataframe
import time
import hydralit_components as hc




st.set_page_config(layout="wide")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Manage Audit Trail")
    set_page_overview("Viewing the Audit Trail", "The audit trail provides the ability for management to view any activity, interaction, log, etc. involved with a FEOC.")
    

    container1=st.container()
    with container1:
        tab_list = [
            stx.TabBarItemData(id=1, title="Audit Log", description="View auditable activity"),
            stx.TabBarItemData(id=2, title="Audit AI", description="Use chat AI for audit"),
            stx.TabBarItemData(id=3, title="Other Audit", description="Miscellaneous audit actions")
        ]
        tab_chosen_id = stx.tab_bar(data=tab_list, default=1)
        
        if tab_chosen_id=="1":
            st.markdown("#### Audit Log CSV")
            dfAudit = load_audit_data()
            # for 1 (index=5) from the standard loader group
            #with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=5):
                #time.sleep(5)
            # for 4 replications of the same loader (index=2) from the standard loader group
            with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=[2,2,2,2]):
                time.sleep(5)
            # for 3 loaders from the standard loader group
            #with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=[3,0,5]):
                #time.sleep(5)
            dfAuditFilter = filter_dataframe(dfAudit)
            dfAudit_Display = st.dataframe(dfAudit,use_container_width=True, hide_index=False)
        elif tab_chosen_id=="2":
            st.markdown("#### Audit Log Supabase Connection")
            dfAudit2 = supabase_get_audit()
            dfAudit2Filter = filter_dataframe(dfAudit2)
            dfAudit2_Display = st.dataframe(dfAudit2Filter, use_container_width=True, hide_index=False)
            #dfAudit2_Display = st.dataframe(dfAudit2, use_container_width=True, hide_index=False)
        elif tab_chosen_id=="3":
            st.markdown("#### Audit Chat")
            
            

        else:
            st.write("Unknown")
 
    
