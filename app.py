import streamlit as st

st.sidebar.title('Navigation')
section = st.sidebar.radio('Go to', ['About Me','Work Experience','Projects','Solidworks/CAD Designs'])
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
        st.subheader("Aerospace Engineering | Design • Structures • Analysis")
        st.write("""
        Junior Aerospace Engineering student at Illinois Institute of Technology
        pursuing a BS–MS degree with a minor in Business.
        """)

    st.title("William Taila")

    st.markdown("""
    ### About Me
    I’m an Aerospace Engineering student at Illinois Institute of Technology (IIT), focused on aircraft design, optimization, and hands-on engineering projects.

    ### Links
    - [LinkedIn](https://www.linkedin.com/in/william-taila-594545305/)
    """)
    st.text('hello world')
    st.image("assets/IMG_1309.jpg", width=400)

elif section == 'Work Experience':
    st.text('hello worl')


elif section == 'Projects':
    st.text('hello wor')


elif section == 'Solidworks/CAD Designs':
    st.text('hello wrld')
