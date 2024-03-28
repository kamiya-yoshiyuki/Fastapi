import streamlit as st
import requests
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from PIL import Image

st.title('インフルエンザ 分類')
smiles = st.text_input('smiles を入力')
if st.button('判定'):
    response = requests.post(url='https://infuluenza-classifier.onrender.com/make_predictions', json={'smiles': smiles})
    # print(response.status_code)
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol)
    st.image(img, use_column_width=True)
    
    target = ['効果あり', '不明', '効果なし']

    prediction = response.json()['prediction']

    st.write('## 結果')
    st.write('#### この化合物はインフルエンザに対して「', str(target[int(prediction)]),'」です')

    # st.write('0 : High（効果あり）')
    # st.write('1 : medium（どちらともいえない）')
    # st.write('2 : low（効果なし）')
