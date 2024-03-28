import streamlit as st
import requests
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from PIL import Image

from pathlib import Path
from tempfile import NamedTemporaryFile
# import matplotlib.pyplot as plt
from rdkit.Chem import inchi
#from rdkit.Chem.Draw import IPythonConsole


st.title('RDKit を使用した化学構造の描画')

# SMILES入力フィールドの表示
smiles = st.text_input('SMILES を入力してください')

# SMILESが入力された場合
if smiles:
    # RDKitを使用して入力されたSMILESから分子を生成
    mol = Chem.MolFromSmiles(smiles)

    # 分子が正しく生成された場合
    if mol is not None:
        # 分子の描画
        img = Draw.MolToImage(mol)

        # 画像をStreamlitアプリに表示
        st.image(img, caption='化学構造', use_column_width=True)
    else:
        st.error('入力されたSMILESが不正です。')

#st.title('SMILESからの分子画像表示')

# SMILESを入力するテキストボックスを作成
#smiles = st.text_input('SMILESを入力してください')

#if st.button('画像を表示'):
    # 入力されたSMILESから分子を作成
 #   mol = Chem.MolFromSmiles(smiles)
    
  #  if mol is not None:
        # 分子の描画
   #     img = Draw.MolToImage(mol)
        
        # 画像をStreamlitアプリに表示
    #    st.image(img, caption='SMILESから生成された分子画像', use_column_width=True)
    #else:
    #    st.error('指定されたSMILESは無効です。')
#st.title('インフルエンザ 分類')
#smiles = st.text_input('smiles を入力')

#if st.button('判定'):
 #   response = requests.post(url='https://infuluenza-classifier.onrender.com/make_predictions', json={'smiles': smiles})
    
 #   if response.status_code == 200:
  #      mol = Chem.MolFromSmiles(smiles)
        
   #     if mol is not None:
  #          img = Chem.Draw.MolToImage(mol)
  #          st.image(img, caption='SMILESから生成された分子画像', use_column_width=True)
            
    #        target = ['効果あり', '不明', '効果なし']
      #      prediction = response.json()['prediction']
            
     #       st.write('## 結果')
          #  st.write(f'この化合物はインフルエンザに対して「{target[int(prediction)]}」です')
        #else:
        #    st.error('指定された SMILES 文字列は不正です。')
    #else:
       # st.error('予測の取得中にエラーが発生しました。')

