
import streamlit as s
import pandas as pd
import requests
import snowflake.connector as sfc
from urllib.error import URLError

# Import CSV and chage index
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

s.title('My parents New Healty dinner')
s.header('Breakfast Menu')
s.text('🥣 Omega3 & Blueberry Oatmeal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-boiled Free-Range Egg')
s.text('🥑🍞 Avocado Toast')


s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
## Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = s.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

## Show only the df for the selected fruits
fruits_to_show = my_fruit_list.loc[fruits_selected]
s.dataframe(fruits_to_show)


# Section with Fruity Vice
s.header("Fruityvice Fruit Advice!")

# This structure allows to separate the code that is loaded once from the code that should be repeated each time a new value is entered.
try:
  # Make a text input to ask for the required information
  fruit_choice = s.text_input('What fruit would you like information about?')
  
  if not fruit_choice:
      s.error('Please select a fruit to get information.')  
  else:
    # Import API with fruit-choice from fruity vice
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    # Use API response and transform to dataframe
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # make dataframe appear on Streamlit
    s.dataframe(fruityvice_normalized)
    
except URLError as e
  s.error()

  
  
# Section code to stop running the previous part every time we run the connection
s.stop()


# Connection for streamlit and snowflake
my_cnx = sfc.connect(**s.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
s.header("The fruit load list contains:")
s.dataframe(my_data_rows)

# Picking fruit to add to the table in db snowflake
picked_fruit = s.text_input("Pick a fruit to add in the list", "passionfruit")
my_cur.execute(" insert into fruit_load_list values ('from streamlit') ");
s.write("Thanks for adding ", picked_fruit)

