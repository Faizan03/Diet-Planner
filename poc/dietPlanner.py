from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
import pycountry
from langchain_core.prompts import load_prompt
import os

load_dotenv()

st.header("Diet Planner")

model= ChatGroq(model="llama-3.3-70b-versatile")


countries = [country.name for country in pycountry.countries]

sex=st.selectbox("Select your sex",["Male","Female"])
age=st.slider("Select age", 0, 120, 25)

country=st.selectbox("Select your country", countries)
height=st.number_input("Enter your height (cm)", min_value=0.0, step=0.1)
current_weight=st.number_input("Enter your current weight (kg)", min_value=0.0, step=0.1)
target_weight= st.number_input("Enter your target weight (kg)", min_value=0.0, step=0.1)
workout_days=st.slider("Select workout days per week", 0, 7, 3)
diet_type=st.selectbox("Select your diet type", ["Vegetarian", "Vegan", "Non-Vegetarian"])
diabetic=st.selectbox("Do you have diabetes?", ["Yes", "No"])
lactose_intolerant=st.selectbox("Are you lactose intolerant?", ["Yes", "No"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
template=load_prompt(os.path.join(BASE_DIR, "diet_plan_template.json"))

prompt=template.invoke( {"age": age,
"country":country,
"current_weight":current_weight,
"diabetic":diabetic,
"diet_type":diet_type,
"height":height,
"lactose_intolerant":lactose_intolerant,
"sex":sex,
"target_weight":target_weight,
"workout_days":workout_days}
)

if st.button("Give diet plan"):
    
    output=model.invoke(prompt)
    
    st.write(output.content)