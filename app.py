import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="Ura Nage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style></style>", unsafe_allow_html=True)

local_css("style/style.css")

# LOAD ASSETS
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_d8fsgrye.json")
img_manga = Image.open("images/ura_1.jpg")
img_ander = Image.open("images/ura_2.jpg")

# HEADER SECTION
with st.container():
    st.subheader("Hi, dit gaat het worden!")
    st.title("Dingen die ik leuk vind")
    st.write("Ik doe een beetje taalanalyse")
    st.write(" Ik kijk veel youtube (https://youtube.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Wat ik doe")
        st.write("##")
        st.write(
            """
            Ik doe een beetje taalanalyse. Die probeer ik op een makkelijke manier online te zetten. 
            Ik denk ook veel over judo. Daarom heet de website zo. Het is mijn favoriete worp. Niet bepaald
            mijn beste, maar je kunt er wel makkelijk mee winnen. Je kunt namelijk:
            - mee vallen
            - je eigen gewicht gebruiken
            - het gewicht van de ander gebruiken.
            """
        )
        st.write("[Dit is een gaaf voorbeeld >](https://www.youtube.com/watch?v=hv6bq3iuIi4)" )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# PROJECTS
with st.container():
    st.write("---")
    st.header("Projecten")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_manga)
        with text_column:
            st.subheader("Chatbots")
            st.write(
                """
                Een makkelijke chatbot met python. BoW en TF-IDF
                """
            )
            st.markdown("[Leesvoer](https://codecademy.com)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ander)
    with text_column:
        st.subheader("Je kunt het ook zo doen")
        st.write(
            """
            Deze ziet er misschien minder mooi uit, maar werkt ook prima.
            """
        )
        st.markdown("[Nog meer leesvoer](https://codecademy.com)")

# contact
with st.container():
    st.write("---")
    st.header("Mail me maar!")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! wel mailadres veranderen!
    # met "<input type="hidden" name="_captcha" value="false"> " zet je de automatische captcha uit
    contact_form = """
    <form action="https://formsubmit.co/timberczy@disroot.org" method="POST">
     <input type="hidden" name="_captcha" value="false"> 
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

