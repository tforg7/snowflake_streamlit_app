
import streamlit as s
import pandas as pd

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


