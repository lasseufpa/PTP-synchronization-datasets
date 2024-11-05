import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from io import BytesIO
import base64

# Set up page configuration
st.set_page_config(page_title="LASSE - PTP Synchronization", page_icon=":stopwatch:", layout="wide")

# Function to load Lottie animations from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to apply local CSS styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply custom CSS
local_css("style/style.css")

# Load Lottie animation from a local file
with open("./clock-animation.json", "r") as file:
    lottie_coding = json.load(file)

# Load images
img_testbed_demo = Image.open("images/testbed-demo.jpg")
testbed_img = Image.open("images/testbed.png")
logo_img = Image.open("images/LASSE_logo.png")
team_member_1 = Image.open("images/aldebaro.jpeg")
team_member_2 = Image.open("images/jose.jpeg")
team_member_3 = Image.open("images/joao.jpeg")
team_member_4 = Image.open("images/igorfreire.jpeg")
team_member_5 = Image.open("images/camila.jpeg")
team_member_6 = Image.open("images/douglas.jpeg")
team_member_7 = Image.open("images/rodrigo.jpeg")
team_member_8 = Image.open("images/dhomini.png")
team_member_9 = Image.open("images/ilan.png")

# Convert images to Base64 for embedding
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# Add custom CSS to make images circular
circular_image_css = """
<style>
.team-member {
    border-radius: 50%;
    margin: auto;
    display: block;
    width: 150px; /* Adjust width as needed */
    height: 150px; /* Adjust height as needed */
}
</style>
"""

# Add logo at the top
with st.container():
    col1, col2, col3 = st.columns([5, 1, 5])
    with col2:
        st.image(logo_img, use_column_width=True)

# Introduction section
with st.container():
    st.subheader("Welcome :satellite_antenna:")
    st.title("Here you can find accurate nanoseconds precision PTP datasets from FPGA-based testbed")
    st.write("We are the Telecommunications, Automation and Electronics Research and Development Center")
    st.write("[Discover >](https://www.lasse.ufpa.br)")

# Project section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our project")
        st.write("##")
        st.write(
            """
            We aim to enhance the time synchronization over 6G networks and beyond. Our expertise
            comprises several use cases such as:
            - PTP networks with and without assisted nodes
            - Over-the-air synchronization
            - AI and synchronization algorithms
            - and so on.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Datasets section
with st.container():
    st.write("---")
    fh_img, fh_txt = st.columns(2)
    with fh_txt:
        st.header("Fronthaul PTP datasets")
        st.write("##")
        st.write(
            """
            Check out the data we used in our works. Useful features are:
            - Traffic type (e.g. TDD)
            - Synchronization period
            - Number of RRUs
            - and so on

            We encourage you to discover the project [repository](https://github.com/lasseufpa/ptp-dal)
            """
        )
        
        # Adjusted button for larger display
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center;">
                <a href="https://lasseufpa.github.io/PTP-synchronization-datasets/" target="_blank">
                    <button style="
                        background-color: #F47721; /* Solid orange background */
                        color: white; /* White text */
                        padding: 20px 60px; /* Increased padding for a larger button */
                        font-size: 24px; /* Larger font size */
                        border: none; /* No border */
                        border-radius: 12px; /* Rounded corners */
                        cursor: pointer; /* Pointer cursor */
                        transition: all 0.3s ease; /* Smooth transition */
                        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* Shadow for a smooth look */
                        text-align: center;
                    ">
                        Go to datasets catalog
                    </button>
                </a>
            </div>
            <style>
                /* Hover style for the button */
                a button:hover {
                    background-color: #ff8c42; /* Slightly lighter orange on hover */
                    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3); /* Larger shadow on hover */
                    transform: scale(1.05); /* Slightly larger on hover */
                }
            </style>
        """, unsafe_allow_html=True)

    with fh_img:
        st.image(testbed_img)

# Testbed demo section
with st.container():
    st.write("---")
    st.header("Testbed demo")
    st.write("##")
    img_column, txt_column = st.columns((1, 2))
    with img_column:
        st.image(img_testbed_demo)
    with txt_column:
        st.subheader("PTP-Synchronized Ethernet Fronthaul Testbed Demonstration")
        st.write(
            """
            This video demonstrates the fronthaul testbed developed at the Federal \
            University of Pará in collaboration with Ericsson Research for investigations \
            on Ethernet-based fronthaul networks for 5G. We focus on the distribution \
            of clock synchronization over the network using the IEEE 1588 precision \
            time protocol (PTP). We also show the setup for evaluating the fronthaul \
            together with a full real-time LTE stack implemented through the Open Air \
            Interface (OAI) software.
            """
        )
        st.markdown("[Watch](https://youtu.be/MPmGM559IGI?si=ccfjHCKOwTDZZrpp)")

# Define CSS para imagens circulares com borda laranja
circular_image_css = """
<style>
.team-member {
    border-radius: 50%;
    border: 3px solid #F47721; /* Borda laranja */
    margin: auto;
    display: block;
    width: 150px;
    height: 150px;
}
</style>
"""

# Apply CSS for circular images
st.markdown(circular_image_css, unsafe_allow_html=True)     


# Team section
with st.container():
    st.write("---")
    st.header("Meet Our Team")
    st.write("##")

    # Display team members using HTML for custom styling
    member_column_1, member_column_2, member_column_3 = st.columns(3)
    with member_column_1:
        st.markdown(
            f""" 
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(team_member_1)}" class="team-member" alt="Dr. Aldebaro Klautau">
            <h2>
               &nbsp;&nbsp;Aldebaro Klautau
            </h2>
            <div class="social-links">
                <a href="https://www.linkedin.com/in/aldebaro-klautau-82a6586/" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" alt="LinkedIn">
                <a href="https://github.com/aldebaro" target="_blank" rel="noopener noreferrer">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
        </a>
            </div>
        </div>
        """,
            unsafe_allow_html=True
        )
    with member_column_2:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(team_member_2)}" class="team-member" alt="Jose Neto">
                <h2>
                        &nbsp;&nbsp;&nbsp;&nbsp;José Neto
                </h2> 
                <div class="social-links">
                <a href="https://www.linkedin.com/in/jose-de-deus-neto/" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" alt="LinkedIn">
                     <a href="https://github.com/josedsneto" target="_blank" rel="noopener noreferrer">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
        </a>
            </div>
        </div>
        """,
            unsafe_allow_html=True
        )
    with member_column_3:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(team_member_3)}" class="team-member" alt="Joao Ferreira">
                <h2>
                    &nbsp;&nbsp;João Ferreira
                </h2>
                <div class="social-links">
                <a href="https://www.linkedin.com/in/jvictorferreira3301/" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" alt="LinkedIn">
                     <a href="https://github.com/jvictorferreira3301" target="_blank" rel="noopener noreferrer">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
        </a>
            </div>
        </div>
        """,
            unsafe_allow_html=True
        )
    
    st.write("##")

    # Additional rows for new team members
    member_column_4, member_column_5, member_column_6 = st.columns(3)
    with member_column_4:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(team_member_4)}" class="team-member" alt="Team Member 4">
                <h2>
                    &nbsp;&nbsp;Igor Freire
                </h2>
                <div class="social-links">
                <a href="https://www.linkedin.com/in/igorauad/" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" alt="LinkedIn">
                <a href="https://github.com/igorauad" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
                </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with member_column_5:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(team_member_5)}" class="team-member" alt="Team Member 5">
                <h2>
                    &nbsp;&nbsp;Camila Novaes
                </h2>
                <div class="social-links">
                <a href="https://br.linkedin.com/in/canovaes" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" alt="LinkedIn">
                <a href="https://github.com/camilanovaes" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
                </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with member_column_6:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(team_member_6)}" class="team-member" alt="Team Member 6">
                <h2>
                    &nbsp;&nbsp;Douglas Maia
                </h2>
                <div class="social-links">
                <a href="https://linkedin.com/in/douglas-maia-33439921b" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" alt="LinkedIn">
                <a href="https://github.com/m-dougl" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
                </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("##")

    # Third row for last two members
    member_column_7, member_column_8, member_column_9 = st.columns(3)
    with member_column_7:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(team_member_7)}" class="team-member" alt="Team Member 7">
                <h2>
                    &nbsp;&nbsp;Rodrigo Dutra
                </h2>
                <div class="social-links">
                <a href="https://www.linkedin.com/in/rodrigo-gomes-dutra-b2b0b412a/" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" alt="LinkedIn">
                <a href="https://github.com/rodgdutra" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
                </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with member_column_8:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(team_member_8)}" class="team-member" alt="Team Member 8">
                <h2>
                   &nbsp;&nbsp;Dhomini Picanço
                </h2>
                <div class="social-links">
                <a href="https://br.linkedin.com/in/dhomini-bezerra-pican%C3%A7o-456270192" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" alt="LinkedIn">
                <a href="https://github.com/dhominicx" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
                </a>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        with member_column_9:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64(team_member_9)}" class="team-member" alt="Team Member 9">
                    <h2>
                        &nbsp;&nbsp;Ilan Sousa
                    </h2>
                    <div class="social-links">
                    <a href="https://github.com/ilansousa" target="_blank" rel="noopener noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" height="24" alt="GitHub">
                </a>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

# Contact section
with st.container():
    st.write("---")
    st.header("Contact us!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/lasse@ufpa.br" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
