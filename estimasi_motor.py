import pickle
import streamlit as st
model = pickle.load(open('estimasi_motorbike.sav','rb'))

st.title ('estimasi harga motor di europa')

price = st.number_input('Input Harga Motor')
mileage = st.number_input('input KM Motor')
power = st.number_input('Input Power Motor')
model = st.number_input('Input model Motor')
fuel = st.number_input('Input fuel Motor')
date = st.number_input('Input tahun Motor')
version = st.number_input('Input version Motor')
gear = st.number_input('Input gear Motor')

predict = ''
if st.button('Estimasi Harga'):
    predict = model.predict (
    [[price,mileage,power]]
)
st.write ('estimasi harga mobil dalam ponds :', predict)
st.write ('estimasi harga mobil dalam IDR (Juta) :',predict*19000)

