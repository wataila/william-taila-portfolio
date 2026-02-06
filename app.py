import streamlit as st

st.sidebar.title('Navigation')
section = st.sidebar.radio('Go to', ['About Me','Work Experience','Projects','Solidworks/CAD Designs','AIAA Spacecraft Design Competition','Education'])
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
    st.markdown("""
    ### Experimental Analysis of Aerodynamic Properties for a NACA 0012 Airfoil
    - **Tools**: Wind Tunnel Testing, Data Acquisition, Python / MATLAB, Aerodynamics
    - **Context**: Academic Laboratory Project
    
    **Overview:**
    Conducted an experimental investigation of the lift and drag characteristics of a NACA 0012 airfoil across a range of angles of attack using wind tunnel testing.
    
    **Key Contributions & Results**
    - Measured lift and drag forces for a NACA 0012 airfoil over multiple angles of attack to characterize aerodynamic performance.
    - Processed raw force and pressure data to compute lift and drag coefficients.
    - Analyzed trends in aerodynamic behavior, including linear lift slope, zero-lift angle, and stall onset.
    - Compared experimental results with theoretical expectations and published airfoil data to assess accuracy and experimental uncertainty.
    - Documented findings through plots, tables, and a formal technical report.
    
    """)
    st.image("assets/Picture1.png", width=400)
    st.text('Plot of the lift coefficient vs the angle of attack with the experimental data.')
    st.image("assets/Picture2.jpg", width=400)
    st.text('Published graph from the NASA Langley Research Center showing the lift coefficient vs the angle of attack for the NACA 0012 aifoil.')
    st.image("assets/Picture3.png", width=400)
    st.text('Experimental drag polar plot showing the drag coefficient vs the lift coefficient.')
    st.image("assets/Picture4.jpg", width=400)
    st.text('Published graph from the NASA Langley Research Center showing the drag coefficient vs the lift coefficient of the NACA 0012 airfoil.')

    st.markdown("""
    **Why This Project Matters:**
    
    This project demonstrates hands-on experimental testing, rigorous data reduction, and validation of experimental results against established aerodynamic theory. Through this work, I developed experience in translating raw experimental measurements into meaningful engineering quantities, evaluating sources of uncertainty, and interpreting trends in physical system behavior. The project also strengthened my technical communication skills through the creation of clear plots, structured analysis, and formal reporting. Collectively, these skills are directly transferable to engineering roles across industries that require experimental validation, data-driven decision-making, and clear communication of technical results.
    
    """)

    st.markdown("""
    ### Educational Fly Fishing Resource Website
    **Tools**: Python, Streamlit, Web UI Design, Data Organization
    
    **Context**: Personal / Independent Project

    **Overview**:
    
    Designed and developed an interactive educational website to teach fly fishing fundamentals, including equipment, techniques, and species-specific knowledge, with a focus on clarity, usability, and structured information delivery.
    
    **Key Contributions & Features**:
    - Built a multi-page web application covering fly types, fly rods, target species, knots, and fly fishing fundamentals.
    - Designed an intuitive user interface to organize technical and instructional content for beginner and intermediate users.
    - Implemented modular page layouts to support scalability and future feature expansion.
    - Applied engineering-style problem decomposition to structure content logically and consistently across the site.
    - Deployed and tested the application locally, iterating on usability and performance.
    
    **Why This Project Matters:**
    
    This project combines my interest in fly fishing with my passion for building structured, educational systems. It allowed me to apply engineering-style problem-solving to software development and content organization while creating a resource that is genuinely useful to others. The project also reflects my interest in developing tools that are both technically sound and user-focused.
    """)

    st.markdown("""
    ### Compressible Flow Tables & Calculator Tool (In Progress)
    
    **Tools**: MATLAB, Python, Numerical Methods, Compressible Flow
    
    **Context**: Personal / Academic Engineering Tool
    
    **Overview**:
    
    Developing a computational resource to generate and visualize compressible flow tables, providing quick access to key flow properties across a range of Mach numbers and thermodynamic conditions.
    
    **Current Features & Development:**
    - Implementing algorithms to compute compressible flow relations, including isentropic flow, normal shock, and oblique shock properties.
    - Automating the generation of tabulated flow properties to replace static reference tables.
    - Building reusable MATLAB and Python functions for rapid engineering calculations.
    - Validating computed results against standard compressible flow tables to ensure numerical accuracy.
    
    **Planned Enhancements:**
    - Interactive user inputs for Mach number and specific heat ratio.
    - Visualization of trends in flow properties using plots and charts.
    - Web-based or GUI interface for improved accessibility.
    
    **Why This Project Matters:**
    
    After taking a compressible flow course, I recognized how time-consuming and inefficient it can be to repeatedly flip through textbook tables to find flow properties for different conditions. This project was motivated by a desire to streamline that process by creating a computational tool that provides fast, accurate access to compressible flow data. Developing this resource reinforces my understanding of compressible flow theory while strengthening my skills in numerical methods, software development, and validation against trusted reference data. The project reflects my interest in building practical tools that improve efficiency for students and engineers, and demonstrates my ability to identify real workflow challenges and design technical solutions to address them.

    """)
elif section == 'Solidworks/CAD Designs':
    st.header('Various SolidWorks Designs')
    st.text('')
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        ### Apple Pencil Holder
        I designed this simple Apple Pencil holder after purchasing an iPad for note-taking, as the built-in holder on my case was inconvenient and made it difficult to remove the pencil quickly. The design features a keychain slot at the top, allowing it to be attached to a carabiner inside my backpack. Additionally, a small bridge near the bottom helps keep the pencil securely in place while still allowing for easy removal.
        """)
        st.image("assets/Screenshot 2026-01-31 190422.png", use_container_width=True)

    with col2:
        st.image("assets/Screenshot 2026-01-31 190504.png", width=350)

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            ### Headphone Desk Holder 
            This headphone desk holder was designed in SolidWorks using precise, measured dimensions to match the geometry of my desk’s top shelf. The structure provides stable support for hanging headphones, while the built-in cable wrap allows for efficient cord management. Accurate dimensioning ensures proper fit, durability, and reliable performance in daily use.
            """)


    with col2:
        st.image("assets/Screenshot 2026-02-01 133906.png")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            ### Turbine Fan Model 
            This turbofan rotor concept was modeled in SolidWorks after studying various aircraft propulsion systems in propulsion class. The design was created to better understand fan-stage geometry, blade arrangement, and rotational symmetry used in jet engines. Modeling this assembly helped reinforce theoretical concepts through hands-on CAD application.            """)


    with col2:
        st.image("assets/Screenshot 2026-02-01 143429.png")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Pencil Holder
        This lattice pencil holder was modeled in SolidWorks by following and adapting an online tutorial to practice advanced CAD techniques. The design was created to better understand helical patterning, surface features, and parametric control in complex geometry. Modeling this part helped reinforce SolidWorks workflow and feature management through hands-on application.
        """)
    with col2:
        st.image("assets/Screenshot 2026-02-05 184013.png")


elif section == 'AIAA Spacecraft Design Competition':
    st.header("Spring 2026 AIAA Spacecraft Design Competition")
    st.markdown("""
    *This section will be updated throughout the Spring 2026 semester as the project progresses.*
    
    This semester (Spring 2026), I am competing in the AIAA Undergraduate Spacecraft Design Competition as part of an 10‑member multidisciplinary team. My subsystem focuses on Mars communication delays and disruptions within NASA’s Moon‑to‑Mars objectives—specifically, developing an architecture capable of maintaining line‑of‑sight between Earth and Mars to enable near‑constant communication throughout the mission period. This includes analyzing geometric blackout conditions, evaluating relay strategies, and identifying methods to mitigate signal interruptions during critical mission phases.
    
    Additionally from this I will become Level 1 & 2 certified in Ansys STK.
    ### Links
    - https://aiaa.org/wp-content/uploads/2025/08/2025-2026-Undergraduate-Team_Space-Design-Competition.pdf
    - https://ntrs.nasa.gov/api/citations/20220013418/downloads/ASCEND-Communication%20Delays%2C%20Disruptions%2C%20and%20Blackouts%20for%20Crewed%20Mars%20Missions.pdf
    """)

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
    - Spacecraft Design
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


