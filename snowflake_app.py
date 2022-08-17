
import streamlit as s
import pandas as pd
import requests
import snowflake.connector as sfc

# Connection for streamlit and snowflake
my_cnx = sfc.connect(**s.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * fom fruit_load_list")
my_data_rows = my_cur.fetchall()
s.header("The fruit load list contains:")
s.dataframe(my_data_rows)



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

# Make a text input to ask for the required information
fruit_choice = s.text_input('What fruit would you like information about?','Kiwi')
s.write('The user entered ', fruit_choice)

# Import API with fruit-choice from fruity vice
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

# Use API response and transform to dataframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# make dataframe appear on Streamlit
s.dataframe(fruityvice_normalized)

