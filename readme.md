![pydantic_1](https://github.com/user-attachments/assets/7ad6afd2-3988-4104-b998-960e9cabc456)


**LLM -> JSON (using Pydantic)**

This is a simple Streamlit app that uses a Google Gemini Flash Multimodal LLM to extract text from a receipt image and outputs the result as a structured JSON format using Pydantic.

**Features**

-  Upload a receipt image (JPG, JPEG, PNG).
-  Extract readable text from the image using Google Gemini Flash Multimodal LLM.
-  Present the extracted content in a structured JSON format.
-  Use Pydantic models to ensure the output is clean and accurate.
-  Easy-to-use Streamlit interface for interacting with the app.

**Setup Instructions**

1. Clone the repository
```
git clone https://github.com/stackmodel/llm-pydantic-json.git
cd llm-pydantic-json
```
2. install Dependencies:

    - Make sure you have Python 3.7 or higher installed. Then, create a virtual environment and install the dependencies:
      
      ```
      python -m venv env
      source env/bin/activate  # For Linux/macOS
      .\env\Scripts\activate   # For Windows
      pip install -r requirements.txt
      ```
3. Rename .env.example to .env file and populate the google gemini api key.
   You can obtain your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

4. Run the app using the following command: ```streamlit run app.py```
   This will launch the app in your browser. Upload the sample.png file.


