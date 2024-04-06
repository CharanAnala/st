import streamlit as st
import os
from pathlib import Path
import shutil
import base64

# Function to create a zip file from a folder
def create_zip(folder_path):
    zip_path = shutil.make_archive(str(folder_path), 'zip', folder_path)
    return zip_path

# Function to remove the temporary zip file
def remove_zip(zip_path):
    os.remove(zip_path)

# Streamlit app layout
def main():
    st.title("Folder Upload and Download App")

    # Upload folder
    uploaded_folder = st.file_uploader("Upload a folder", type=None)

    if uploaded_folder is not None:
        folder_path = Path("uploaded_folder")
        folder_path.mkdir(parents=True, exist_ok=True)
        for file in uploaded_folder:
            with open(os.path.join(str(folder_path), file.name), "wb") as f:
                f.write(file.getvalue())

        # Create a download link for the uploaded folder
        st.markdown(get_download_link(folder_path), unsafe_allow_html=True)

# Function to generate download link
def get_download_link(folder_path):
    zip_path = create_zip(folder_path)
    with open(zip_path, 'rb') as f:
        zip_data = f.read()

    remove_zip(zip_path)

    # Prepare the download link
    zip_b64 = base64.b64encode(zip_data).decode()
    href = f'<a href="data:application/zip;base64,{zip_b64}" download="{folder_path.stem}.zip">Click here to download the folder</a>'
    return href

if __name__ == "__main__":
    main()
