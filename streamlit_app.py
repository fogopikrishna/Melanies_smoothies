import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    """Choose the Fruits you want in your custom Smoothie"""
)
name_on_order = st.text_input("Name on Smoothie")
st.write("The Name on Smoothie Will be", name_on_order)
#session = get_active_session()
cnx=st.connection("snowflake")
sessions=cnx.session()
import streamlit as st
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'));
#st.dataframe(data=my_dataframe, use_container_width=True);
ingredients_list=st.multiselect('Choose upto 5 Ingredients:',my_dataframe,max_selections=5)
if ingredients_list:
     ingredients_string= ''
     for fruit_chosen in ingredients_list:
       ingredients_string += fruit_chosen + ' '
       my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order +""" ')"""
     time_to_insert=st.button('Submit Order') 
     if time_to_insert:
      session.sql(my_insert_stmt).collect()
      st.write('Your Smoothie is ordered,'+name_on_order+'!',icon="✅")
