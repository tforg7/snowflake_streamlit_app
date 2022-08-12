
import streamlit as s
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

s.title('My parents New Healty dinner')
s.header('Breakfast Menu')
s.text('🥣 Omega3 & Blueberry Oatmeal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-boiled Free-Range Egg')
s.text('🥑🍞 Avocado Toast')


s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
