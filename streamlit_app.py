

import streamlit  # any small spelling mistake it won't relflect on streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents New healthy dinner')   
streamlit.header('🥣 breakfast menu')
streamlit.text('🥗 omega3 and Blueberry oatmeals')
streamlit.text('🐔🥑🍞kale, spinach and Rocket')


# import pandas as pd
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')  #Choose the Fruit Name Column as the Index



# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])  #befor we just ran streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
#streamlit.dataframe(my_fruit_list)  #here because above the table we want select option before we did this

streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized


streamlit.header("Fruityvice Fruit Advice!")
try:
 # Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("please select a fruit to get information")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
      
except URLError as e:
    streamlit.error()
        
       
streamlit.write('The user entered ', fruit_choice)

# import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)
# streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
# write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)



# import snowflake.connector
streamlit.header("The fruit load list contains")
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()


if streamlit.button('Get fruit load list'):
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
        my_data_rows = get_fruit_load_list()
# streamlit.header("The fruit load list contains")
        streamlit.dataframe(my_data_rows)


# streamlit.stop()

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.exceute("insert into fruit_load_list values ('from streamlit')")
        return "thanks for adding " + new_fruit


add_my_fruit = streamlit.text_input('what fruit would you like to add')
if streamlit.button('Add fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)








