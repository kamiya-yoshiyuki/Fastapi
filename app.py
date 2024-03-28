import streamlit as st
import requests
import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from PIL import Image

st.title('インフルエンザ 分類')
smiles = st.text_input('smiles を入力')

if st.button('判定'):
    response = requests.post(url='https://infuluenza-classifier.onrender.com/make_predictions', json={'smiles': smiles})
    
    if response.status_code == 200:
        mol = Chem.MolFromSmiles(smiles)
        
        if mol is not None:
            img = Chem.Draw.MolToImage(mol)
            st.image(img, caption='SMILESから生成された分子画像', use_column_width=True)
            
            target = ['効果あり', '不明', '効果なし']
            prediction = response.json()['prediction']
            
            st.write('## 結果')
            st.write(f'この化合物はインフルエンザに対して「{target[int(prediction)]}」です')
        else:
            st.error('指定された SMILES 文字列は不正です。')
    else:
        st.error('予測の取得中にエラーが発生しました。')

