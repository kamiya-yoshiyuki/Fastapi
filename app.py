import streamlit as st
import requests

st.title('インフルエンザ 分類')
smiles = st.text_input('smiles を入力')
response = requests.post(url='http://127.0.0.1:8000/make_predictions', json={'smiles': smiles})
# print(response.status_code)
st.write(smiles)

target = ['効果あり', '不明', '効果なし']

prediction = response.json()['prediction']

st.write('## prediction')
st.write('#### この化合物はインフルエンザに対して「', str(target[int(prediction)]),'」です')

# st.write('0 : High（効果あり）')
# st.write('1 : medium（どちらともいえない）')
# st.write('2 : low（効果なし）')