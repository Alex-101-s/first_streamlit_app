import streamlit  # any small spelling mistake it won't relflect on streamlit
streamlit.title('My parents New healthy dinner')   
streamlit.header('🥣 breakfast menu')
streamlit.text('🥗 omega3 and Blueberry oatmeals')
streamlit.text('🐔🥑🍞kale, spinach and Rocket')


import pandas 
my_fruit_list = pandas.read("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
