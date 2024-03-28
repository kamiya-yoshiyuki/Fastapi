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
        
        if mol is not None:  # mol オブジェクトが None でない場合にのみ処理を続行する
            img = mol_to_image(mol)
            st.image(img, use_column_width=True)
            
            target = ['効果あり', '不明', '効果なし']
            prediction = response.json()['prediction']
            
            st.write('## 結果')
            st.write(f'この化合物はインフルエンザに対して「{target[int(prediction)]}」です')
        else:
            st.error('SMILES文字列が不正で、化学構造を生成できませんでした。')
    else:
        st.error('予測の取得中にエラーが発生しました。')

def mol_to_image(mol):
    img = Chem.Draw.MolToImage(mol, size=(300, 300))
    return img
