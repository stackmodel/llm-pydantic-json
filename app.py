import google.generativeai as genai  
from PIL import Image  
from dotenv import load_dotenv  
from pydantic import BaseModel
import streamlit as st  
import os

load_dotenv() # Load environment variables from the .env file

# Set the initial configuration for the Streamlit app
st.set_page_config(page_title="LLM-JSON", initial_sidebar_state="expanded", layout="wide") 
st.title("LLM -> JSON (using Pydantic)") 

# Fetch the Google API key from environment variables
google_genai_key = os.getenv("GOOGLE_API_KEY")

# Configure the Google Gemini API with the loaded API key
genai.configure(api_key=google_genai_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

# Define models for Structured Outputs
class Item(BaseModel):
    product: str
    price: float
    quantity: int

class Receipt(BaseModel):
    store_name: str
    items: list[Item]

with st.sidebar:
    st.title("Upload a Receipt")  # Sidebar title
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])  
    if uploaded_file:
        image = Image.open(uploaded_file)  
        st.image(image, caption='Uploaded Image') 
    if st.button("Reset", type="primary"):
        if 'ocr_extracted_text' in st.session_state:
            del st.session_state['ocr_extracted_text']
        st.rerun()

if uploaded_file:
    
    if st.button("Extract Text as JSON", type="primary"):
        with st.spinner("Processing image..."):  # Show a spinner while processing
            try:
                prompt = """Analyze the image provided and extract all readable text.
                Present the extracted content in a well-organized JSON format.  
                The output should be clear, concise, and easy to interpret."""
                
                inputs = [prompt]
                inputs.append(image)
                response = model.generate_content(inputs,
                                                   generation_config=genai.GenerationConfig(
                                                                        response_mime_type="application/json",
                                                                        response_schema = Receipt))
                st.session_state['ocr_extracted_text'] = response.text
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")

if 'ocr_extracted_text' in st.session_state:
    st.json(st.session_state['ocr_extracted_text'])
    # st.markdown(st.session_state['ocr_extracted_text'])  # Display the extracted text in Markdown format
else:
    st.info("Upload an image and press 'Extract Text'.") 