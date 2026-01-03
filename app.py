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
        U.S. Citizen | Based In Dallas, TX | Chicago & Los Angeles No Relocation Assistance Needed | Open To Relocation d
        """)

    st.markdown("""
    ### About Me
    I am a third-year aerospace engineering student at the Illinois Institute of Technology, pursuing both a bachelor’s and a master’s degree, with plans to graduate in the spring of 2027. My master’s program focuses on dynamics and navigation systems, while my studies more broadly cover the design, analysis, and optimization of aerospace structures and systems. I have experience with computational modeling, fluid mechanics, propulsion systems, and structural analysis, and I enjoy applying these skills to real-world engineering challenges. Outside the classroom, I am passionate about aerospace innovation, building projects, and exploring new technologies. I also enjoy outdoor activities like hiking and fly fishing, which provide a creative balance to my technical work. My goal is to contribute to cutting-edge aerospace projects, combining engineering expertise with problem-solving creativity to make meaningful impacts in the field.
    
    ### Objective
    I am seeking an internship opportunity with a company where I can build a long-term future while gaining hands-on engineering experience and learning from experienced engineers through mentorship. I am motivated to apply my technical and analytical skills to real-world projects while continuing to grow professionally.
    
    ### Tools
    - MATLAB 
    - Python
    - Solidworks
    - Microsoft Office

    ### Links
    - [LinkedIn](https://www.linkedin.com/in/william-taila-594545305/)
    """)


elif section == 'Work Experience':
    st.markdown("""
    ### Work Expereince
    ### Undergraduate Research Assistant 
    **Illinois Institute of Technology** — *Chicago, IL*  
    *August 2024 — December 2024*
    - Conducted CFD simulations and data analysis to assess airflow performance and identify flow anomalies relevant to component wear
    - Applied design and validation principles to evaluate structural limits and optimize test geometries for improved durability
    - Performed parametric studies to evaluate the impact of geometric variations on flow characteristics and component performance
    - Developed MATLAB scripts to automate post-processing of simulation data, reducing analysis time and improving accuracy
    - Interpreted simulation results to support engineering decisions and guide design refinement
    - Generated technical documentation summarizing methods, results, and conclusions for weekly progress reports and design reviews
    - Collaborated with faculty and research team members to ensure consistency between modeling assumptions and physical constraints
    
    ### Dock Hand 
    **Theodosia Marina and Resort** — *Theodosia, MO*  
    *May 2022 — August 2022*
    - Operated and maintained marine systems, ensuring mechanical reliability and safety compliance across 100+ vessels
    - Assisted with troubleshooting and repair coordination, reducing downtime and increasing operational throughput by 20%
    - Supported docking, mooring, and vessel maneuvering operations under varying environmental conditions
    - Conducted routine inspections of equipment and waterfront infrastructure to identify maintenance needs
    - Assisted customers with vessel handling and marina operations in a professional, safety-focused manner
    - Maintained a clean, organized, and operational dock environment during peak seasonal demand
    - Demonstrated strong teamwork, situational awareness, and reliability in a physically demanding work environment
    
    ### Volunteer 
    **The Samaritan Inn** — *McKinney, TX*  
    *August 2019 — May 2023*
    - Volunteered in support of homeless shelter operations and community assistance programs
    - Conducted outreach by distributing flyers to advertise donation drives for clothing and furniture
    - Engaged with local businesses and community members to raise awareness of shelter needs
    - Helped secure over $2,500 in donations across multiple years of volunteering
    - Assisted with organizing, sorting, and managing donated clothing and household items
    - Supported shelter staff with logistics and coordination during donation campaigns
    - Demonstrated long-term commitment, initiative, and community leadership through consistent service
    
    """)


elif section == 'Projects':
    st.text('hello')


elif section == 'Solidworks/CAD Designs':
    st.text('hello')

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


