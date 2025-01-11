import streamlit as st

col3, col4,col5, =st.columns(3)
with col3:
    st.image(r"logo.png", width=170)

with col4:
    st.markdown('<div style="text-align: center; font-size: 40px; font-weight: bold;">MobilitySense</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; font-size: 30px;">Detecting your motion</div>', unsafe_allow_html=True)

tab1,tab2,tab3=st.tabs(["Home","Scan","About Me"])
with tab1:
    st.markdown('<div style="text-align: center; font-size: 30px; font-weight: bold;">Home</div>', unsafe_allow_html=True)
    col1, col2, = st.columns(2)

    with col1:
        st.markdown('<span style="font-size: 18px;">Road safety is everyones responsibility, but it begins with understanding the language of the road: traffic signs. These silent signals guide drivers, reduce confusion, and prevent accidents. Yet, many accidents occur due to misinterpretation or ignorance of these crucial signs. Every year, countless lives are impacted by traffic incidents that could have been prevented. A significant number of these accidents happen because drivers fail to recognize or understand traffic signs. Speed limits, caution warnings, and stop signals—when overlooked, these simple signs can lead to life-altering consequences. Our platform is designed to tackle this challenge head-on. By using advanced image recognition technology, we help you instantly identify traffic signs from pictures. Whether youre a student preparing for a driving test, a professional driver ensuring compliance, or simply curious about the signs around you, our tool is here to empower you with knowledge for safer driving.</span>', unsafe_allow_html=True)

    with col2:
        st.image("https://www.mckinsey.com/~/media/mckinsey/industries/automotive%20and%20assembly/our%20insights/the%20future%20of%20mobility%20is%20at%20our%20doorstep/the-future-of-mobility-5050-1536x1536.jpg")

with tab2:
    st.markdown('<div style="text-align: center; font-size: 30px; font-weight: bold;">Scan</div>', unsafe_allow_html=True)
    col1, col2,=st.columns(2)
    with col1:
        from PIL import Image

        # Create an image uploader widget
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Open and display the image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
    with col2:
        st.write("Results:")


with tab3:
    st.markdown('<div style="text-align: center; font-size: 30px; font-weight: bold;">About Me</div>', unsafe_allow_html=True)
    st.markdown('<span style="font-size: 18px;">Hi! Im Kriti Hingarh, I currently study in the 11th grade in Aditya Birla World Academy in Mumbai.  I have several hobbies such as horse riding, swimming and playing badminton, I also love teaching mathematics to my peers. As someone passionate about mathematics and aiming to pursue applied math at university, I see this project as an exciting opportunity to bridge theory and application. Traffic sign recognition involves working with machine learning algorithms and datasets, offering hands-on experience in areas like data analysis, pattern recognition, and optimization—key components of applied math. By developing this tool, I can not only contribute to road safety but also strengthen my understanding of real-world mathematical applications. This project aligns with my academic goals and provides a platform to explore the intersection of math, technology, and societal impact.</span>', unsafe_allow_html=True)




