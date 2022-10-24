import streamlit as st

st.set_page_config(layout="wide")
font = "sans serif"
st.title("DeteX: the detection of pneumonia in the world")
st.markdown("***")
st.sidebar.markdown("# Our solution")

container = st.container()

container.header('Presentation of our solution')
col1, col2 = st.columns(2)
text1 = '<p style="font-family:Rockwell; color:White; font-size: 25px;">Since the beginning of the 90s, pneumonia has been responsible for 60% of inflectional death within all ages.</p>'
text2 = '<p style="font-family:Rockwell; color:White; font-size: 25px; width:100%;">Pneumonia can be very serious and even deadly when it’s not threated in time. Indeed, most people with pneumonia respond well to treatment, however we first need to know you’ve got it. But pneumonia can be tricky a disease to detect without the appropriate tools, and like we said, since most treatment are effective, a quick detection is very likely to save your life. Nowadays technologies such as X-ray and others are crucial to the wellbeing of our society. Moreover, it produced and incredible amount of data and thanks to them the doctor can tell if a people suffer from pneumonia or not. Today our job is to automate the detection of pneumonia. To do so we will produce and document a data scientist report based on machine learning algorithms from labeled x-rays, to facilitate the medical diagnosis of pneumonia cases. Our Project will take the form of an app or a website and the challenge will be to find the right algorithms and approach in order to have the best percentage of detection of pneumonia cases.</p>'
text3 = '<p style="font-family:Rockwell; color:White; font-size: 25px; width:100%;">Here we are providing a solution to detect Pneumonia by using deeplearning, you can test our solution on the next page</p>'
with col1: 
    st.write(text1, unsafe_allow_html=True)
    st.write(text2, unsafe_allow_html=True)

    st.write(text3, unsafe_allow_html=True)
with col2: 
    st.image('images/causes_928px.jpg')
st.markdown("***")
st.header('Find more information about Pneumonia')
container.write("")
text4 = '<p style="font-family:Rockwell; color:White; font-size: 25px; width:100%;">Preventing pneumonia in children is an essential component of a strategy to reduce child mortality. Immunization against Hib, pneumococcus, measles and whooping cough (pertussis) is the most effective way to prevent pneumonia. Adequate nutrition is key to improving children natural defences, starting with exclusive breastfeeding for the first 6 months of life. In addition to being effective in preventing pneumonia, it also helps to reduce the length of the illness if a child does become ill. Addressing environmental factors such as indoor air pollution (by providing affordable clean indoor stoves, for example) and encouraging good hygiene in crowded homes also reduces the number of children who fall ill with pneumonia. In children infected with HIV, the antibiotic cotrimoxazole is given daily to decrease the risk of contracting pneumonia.</p>'
st.write(text4, unsafe_allow_html=True)
text5 = '<p style="font-family:Rockwell; color:White; font-size: 25px; width:100%;">Read more and be active in the fight against pneumonia : </p>'
st.write(text5, unsafe_allow_html=True)
st.write('[stoppneumonia.org](https://www.who.int/news-room/fact-sheets/detail/pneumonia)')