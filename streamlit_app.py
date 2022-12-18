import streamlit
import pandas
import requests

streamlit.title("My Parents New Healthy Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 and Blueberry Oatmeal")
streamlit.text("Kale, Spinach and Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like input about?','Kiwi')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.write('The user entered', fruit_choice)
streamlit.text(fruityvice_response)
streamlit.dataframe(fruityvice_normalized)
