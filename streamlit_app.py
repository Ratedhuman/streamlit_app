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
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Set the 'Fruit' column as the index of the DataFrame
my_fruit_list = my_fruit_list.set_index('Fruit')

# Create a multiselect widget for selecting fruits
# This widget presents a list of all fruits in the DataFrame
# By default, 'Avocado' and 'Strawberries' are selected
selected_fruits = st.multiselect("Pick some fruits:", list(my_fruit_list.index), default=['Avocado', 'Strawberries'])

# Ask app to put the list of selected fruits into a variable called fruits_selected
# Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set
# and assign that data to a variable called fruits_to_show
# Finally, we'll ask the app to used the data in fruits_to_show in the dataframe it displays on the page

#let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
st.dataframe(fruits_to_show)

#filter the DataFrame based on the selected fruits
filtered_df = my_fruit_list.loc[selected_fruits]

# Display the filtered DataFrame
st.dataframe(filtered_df)














