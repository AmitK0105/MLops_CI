import streamlit as st
# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fifth power")

n= st.number_input("Enter an integer", value=1, step=1)

#calculate results

Square= n**2
cube= n**3
Fifth_power= n**5

#Display Result

st.write(f"The Power of {n} is : {Square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"The fifth power of {n} is :{Fifth_power}")