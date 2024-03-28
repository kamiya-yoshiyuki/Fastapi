import streamlit as st
import requests
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from PIL import Image

st.title('インフルエンザ 分類')
smiles = st.text_input('smiles を入力')
if st.button('判定'):
    response = requests.post(url='https://infuluenza-classifier.onrender.com/make_predictions', json={'smiles': smiles})
    
    if response.status_code == 200:
        mol = Chem.MolFromSmiles(smiles)
        img = mol_to_image(mol)  # ここで `mol_to_image()` 関数を呼び出しています
        st.image(img, use_column_width=True)
        
        target = ['効果あり', '不明', '効果なし']
        prediction = response.json()['prediction']
        
        st.write('## 結果')
        st.write(f'この化合物はインフルエンザに対して「{target[int(prediction)]}」です')
    else:
        st.error('予測の取得中にエラーが発生しました。')

def mol_to_image(mol):
    img = Chem.Draw.MolToImage(mol, size=(300, 300))
    return img
