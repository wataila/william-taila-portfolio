import streamlit as st

st.sidebar.title('Navigation')
section = st.sidebar.radio('Go to', ['About Me','Work Experience','Projects','Solidworks/CAD Designs','Education'])
if section =='About Me':
    st.set_page_config(
        page_title="William Taila | Aerospace Engineering",
        page_icon="✈️",
        layout="wide"
    )
    col1, col2 = st.columns([4, 5])  # left narrow, right wide

    with col2:
        st.image("assets/IMG_1309.jpg", width=400)

    with col1:
        st.title("William Taila")
        st.subheader("Aerospace Engineering Student")
        st.write("""
        U.S. Citizen | Based In Dallas, TX | Chicago & Los Angeles No Relocation Assistance Needed | Open To Relocation
        """)

    st.markdown("""
    ### About Me
    I am a third year aerospace engineering student at Illinois Institute of Technology pursing both a bachelors and masters degree both of which I will be graduating with in the spring of 2027

    ### Links
    - [LinkedIn](https://www.linkedin.com/in/william-taila-594545305/)
    """)


elif section == 'Work Experience':
    st.text('hello worl')


elif section == 'Projects':
    st.text('hello wor')


elif section == 'Solidworks/CAD Designs':
    st.text('hello wrld')

elif section == 'Education':
    import streamlit as st

    st.header("Education")

    st.markdown("""
    **Illinois Institute of Technology** — *Chicago, IL*  

    **Master of Engineering in Aerospace Engineering (Accelerated Program)**  
    GPA: 4.0 / 4.0

    **Bachelor of Science in Aerospace Engineering**  
    GPA: 3.4 / 4.0
    
    Deans List: Fall 2023 | Spring 2024 | Fall 2025

    *Expected Graduation: May 2027*
    """)

    st.markdown("**Relevant Coursework:**")
    st.markdown("""
    - Aerodynamics 
    - Propulsion  
    - Advanced Dynamics 
    - Aerospace Laboratory 1 & 2
    - Computational Mechanics  
    - Data Driven Modeling
    - Fluid Mechanics  
    - Engineering Analysis
    """)

    st.markdown("**Involvment:**")
    st.markdown("""
    - AIAA - Treasurer 
    - Engieners Without Borders 
    - Rocketry 
    - Propulsion Club
    """)

