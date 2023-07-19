import streamlit  # any small spelling mistake it won't relflect on streamlit
streamlit.title('My parents New healthy dinner')   
streamlit.header('🥣 breakfast menu')
streamlit.text('🥗 omega3 and Blueberry oatmeals')
streamlit.text('🐔🥑🍞kale, spinach and Rocket')


import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")



# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)  #here because above the table we want select option
