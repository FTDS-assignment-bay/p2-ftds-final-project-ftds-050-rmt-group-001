import streamlit as st
import pandas as pd
from PIL import Image

prod_img = {'Galaxy Z Fold7': 'Fold7.png',
            'Galaxy S25 Ultra': 's25-u.png',
            'Galaxy S25 FE': 's25-fe.avif',
            'Samsung Galaxy Fold 6':'fold6.webp',
            'Galaxy Z Flip7 FE': 'Flip7.png',
            'Samsung Galaxy S24 Ultra 5G': 's24-u.webp',
            'Samsung Galaxy S23 Ultra 5G': 's23-u.png',
            'Galaxy S25': 's25.png',
            'Galaxy S23': 's23.avif',
            'Galaxy Z Fold 4': 'fold4.png',
            'Samsung Galaxy Z Flip 6': 'flip6.png',
            'Galaxy S24 5G': 's24.webp',
            'Galaxy S23+ 5G': 's23+.png',
            'Galaxy Z Flip5 5G': 'flip5.png',
            'Galaxy S22 Ultra 5G': 's22-u.webp',
            'Galaxy Note 20 Ultra 5G': 'note20-u.webp',
            'Galaxy Note 10 Plus': 'note10+.png',
            'Samsung S22+': 's22+.webp',
            'Galaxy Z Flip 4': 'flip4.webp',
            'Samsung Galaxy S23 FE': 's23-fe.webp'}
            


def run():
    st.title("📱 Samsung Review Summarizer")
    
    # Load df
    df = pd.read_csv('src/clean.csv')

    with st.form(key='Form Parameters'):
        input_name = st.selectbox("**Choose your preferred model**", df['model_name'].unique(), index=None, help='We only provide 20 Samsung Flagship model starting from 2022-2025')
    
        submit = st.form_submit_button('Proceed ✅')

        if submit:
            if input_name == None:
                st.write("❌ Please select the product first!!")
            else:
                img_path = 'src/' + prod_img[input_name]
                st.image(img_path, caption=input_name)
                model_data = pd.read_json('src/inference_results.json')
                selected = model_data[input_name]

                # Extract specs dict
                specs_dict = selected['specs']

                specs_df = pd.DataFrame(
                    specs_dict.items(),
                    columns=["Specification", "Value"]
                ).reset_index(drop=True)

                st.subheader("📱 Specifications")
                st.dataframe(specs_df, hide_index=True)
                st.write("Strengths:", ", ".join(selected["strength"]))
                st.write("Weaknesses:", ", ".join(selected["weakness"]))

if __name__ == '__main__':
    run()
