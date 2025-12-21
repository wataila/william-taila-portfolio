import streamlit as st

st.sidebar.title('Navigation')
section = st.sidebar.radio('Go to', ['About Me','Work Experience','Projects','Solidworks/CAD Designs'])
if section =='About Me':
    st.set_page_config(
        page_title="William Taila | Aerospace Engineering",
        page_icon="✈️",
        layout="wide"
    )

    st.title("William Taila")
    st.subheader("Aerospace Engineering | Design | Analysis")

    st.markdown("""
    ### About Me
    I’m an Aerospace Engineering student at Illinois Institute of Technology (IIT), focused on aircraft design, optimization, and hands-on engineering projects.

    ### Featured Projects
    - **Twin-Engine STOL Bush Plane Concept**
    - **Optimization Methods in Python (GD, Newton, BFGS)**
    - **Fly Fishing Engineering Website**

    ### Skills
    - Python, MATLAB
    - SolidWorks, AutoCAD
    - Aircraft Performance & Structures

    ### Links
    - [LinkedIn](https://www.linkedin.com/in/william-taila-594545305/)
    """)
    st.text('hello world')

elif section == 'Work Experience':
    st.text('hello worl')


elif section == 'Projects':
    st.text('hello wor')


elif section == 'Solidworks/CAD Designs':
    st.text('hello wrld')
