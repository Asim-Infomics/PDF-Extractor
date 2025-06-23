import streamlit as st
import pytesseract
from pdf2image import convert_from_path
import re
from PIL import Image
import tempfile
import pandas as pd
import time
from io import BytesIO

# Streamlit app
st.title("Extract Numbers Starting with '923' from PDF Bills")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.info("Processing the uploaded PDF file...")

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    # Convert PDF to images
    pdf_images = convert_from_path(tmp_file_path, dpi=300)
    total_pages = len(pdf_images)

    # Initialize progress bar and time tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    start_time = time.time()

    # Initialize a list to store data per page
    extracted_data = []

    # Process each page
    for page_number, image in enumerate(pdf_images, start=1):
        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        # Extract numbers starting with '923' and names
        numbers = re.findall(r'\b923\d+\b', text)
        names = re.findall(r'Recipient\s+([a-zA-Z\s]+)', text)

        # Pair name and number for the page
        number = numbers[0] if numbers else "Not Found"
        name = names[0] if names else "Not Found"

        # Append data to the list
        extracted_data.append({
            "Page": page_number,
            "Name": name,
            "Phone": number
        })

        # Update progress bar
        progress_percentage = int((page_number / total_pages) * 100)
        elapsed_time = time.time() - start_time
        estimated_total_time = (elapsed_time / page_number) * total_pages
        remaining_time = max(estimated_total_time - elapsed_time, 0)

        progress_bar.progress(progress_percentage)
        status_text.write(f"Processing Page {page_number}/{total_pages} - {progress_percentage}% completed")
        status_text.write(f"Estimated time remaining: {remaining_time:.2f} seconds")

    # Convert extracted data to a DataFrame
    df = pd.DataFrame(extracted_data)

    # Display the results
    if not df.empty:
        st.success("Extraction Complete!")
        # st.write("Extracted Data:")
        # st.table(df)

        # Convert DataFrame to an Excel file
        def convert_df_to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Extracted Data')
            processed_data = output.getvalue()
            return processed_data

        # Get the original uploaded file name (without extension)
        original_filename = uploaded_file.name.rsplit(".", 1)[0]  # Removes .pdf extension

        # Create download button with dynamic file name
        st.download_button(
            label="📥 Download Extracted Data (XLSX)",
            data=convert_df_to_excel(df),
            file_name=f"{original_filename}_extracted.xlsx",  # Use original name
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


# Instructions
st.sidebar.title("Instructions")
st.sidebar.info(
    """
    1. Upload a PDF file containing scanned bills.
    2. The app will extract numbers starting with '923' and associated names from each page.
    3. Missing data will be marked as "Not Found."
    4. The extracted data will be displayed below.
    """
)

# import streamlit as st
# import pytesseract
# from pdf2image import convert_from_path
# import re
# from PIL import Image
# import tempfile
# import pandas as pd
# from io import BytesIO
# # Streamlit app
# st.title("Extract Numbers Starting with '923' from PDF Bills")

# # File uploader
# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# if uploaded_file:
#     st.info("Processing the uploaded PDF file...")

#     # Save the uploaded file to a temporary location
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         tmp_file.write(uploaded_file.read())
#         tmp_file_path = tmp_file.name

#     # Convert PDF to images
#     pdf_images = convert_from_path(tmp_file_path, dpi=300)

#     # Initialize a list to store data per page
#     extracted_data = []

#     # Process each page
#     for page_number, image in enumerate(pdf_images, start=1):
#         # Perform OCR on the image
#         text = pytesseract.image_to_string(image)

#         # Extract numbers starting with '923' and names
#         numbers = re.findall(r'\b923\d+\b', text)
#         names = re.findall(r'Recipient\s+([a-zA-Z\s]+)', text)

#         # Pair name and number for the page
#         number = numbers[0] if numbers else "Not Found"
#         name = names[0] if names else "Not Found"

#         # Append data to the list
#         extracted_data.append({
#             "Page": page_number,
#             "Name": name,
#             "Phone": number
#         })

#         # Show progress
#         st.write(f"Processed Page {page_number}: Name - {name}, Phone - {number}")

#     # Convert extracted data to a DataFrame
#     df = pd.DataFrame(extracted_data)

#     # Display the results
#     if not df.empty:
#         st.success("Extraction Complete!")
#         st.write("Extracted Data:")
#         st.table(df)

#         # Convert DataFrame to an Excel file
#         def convert_df_to_excel(df):
#             output = BytesIO()
#             with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
#                 df.to_excel(writer, index=False, sheet_name='Extracted Data')
#             processed_data = output.getvalue()
#             return processed_data

#         # Create download button
#         st.download_button(
#             label="📥 Download Extracted Data (XLSX)",
#             data=convert_df_to_excel(df),
#             file_name="extracted_data.xlsx",
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )
#     else:
#         st.warning("No data was found in the uploaded file.")
#     # Instructions
# st.sidebar.title("Instructions")
# st.sidebar.info(
#     """
#     1. Upload a PDF file containing scanned bills.
#     2. The app will extract numbers starting with '923' and associated names from each page.
#     3. Missing data will be marked as "Not Found."
#     4. The extracted data will be displayed below.
#     """
# )
