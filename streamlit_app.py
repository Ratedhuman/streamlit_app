# Import necessary libraries
import streamlit as st
import pandas as pd

# Set the title of the application
st.title("My Mom's New Healthy Diner")

# Set a section header for the breakfast menu
st.header('Breakfast Menu')

# Add items to the breakfast menu
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

# Set a section header for the smoothie builder
st.header(" 🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

# Load the CSV file from the provided URL into a DataFrame
# This CSV file contains information about different fruits
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Set the 'Fruit' column as the index of the DataFrame
# This helps us to access rows of data using the fruit names
my_fruit_list = my_fruit_list.set_index('Fruit')

# Create a multiselect widget for selecting fruits
# This widget presents a list of all fruits in the DataFrame
# By default, 'Avocado' and 'Strawberries' are selected
# The selected fruits are stored in the fruits_selected variable
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), default=['Avocado', 'Strawberries'])

# Filter the DataFrame based on the selected fruits
# Only rows that correspond to the selected fruits are retained
# The filtered data is stored in the fruits_to_show variable
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the filtered DataFrame
# This shows the user information about the selected fruits
st.dataframe(fruits_to_show)













