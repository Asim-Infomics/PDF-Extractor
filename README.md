# PDF-Extractor
This extractor is a lightweight OCR-based Streamlit application designed to extract data from scanned PDF documents—typically utility or billing invoices. 

# 📄 Extract '923' Numbers from PDF Bills using OCR

A simple Streamlit app that extracts phone numbers starting with `923` and associated recipient names from scanned PDF bills using OCR (Tesseract). The results can be downloaded as an Excel file.

---

## 🧰 Features

- Upload scanned PDF bills.
- Automatically convert PDF pages to images.
- Perform OCR using `pytesseract`.
- Extract phone numbers starting with `923` and recipient names.
- Display results in a table.
- Download extracted data as an Excel file (`.xlsx`).
- Progress bar and estimated time tracker for large PDFs.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pdf-923-number-extractor.git
cd pdf-923-number-extractor
```

### 2. Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

You need to install Tesseract on your system:

- **Windows**: Download from [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- **Linux**:  
  ```bash
  sudo apt install tesseract-ocr
  ```

Make sure the path to `tesseract` is correctly configured if not in your system path.

### 5. Install Poppler (for `pdf2image`)

- **Windows**: Download from [http://blog.alivate.com.au/poppler-windows/](http://blog.alivate.com.au/poppler-windows/) and add the `bin/` folder to your PATH.
- **Linux**:  
  ```bash
  sudo apt install poppler-utils
  ```

---

## 📦 Run the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
pdf-923-number-extractor/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🧪 Example Data Pattern

The app extracts:

- Phone numbers like `923001234567`
- Names appearing after the word `Recipient`

---

## 📥 Output Format

Results are exported in an Excel file with the following columns:

| Page | Name      | Phone         |
|------|-----------|---------------|
| 1    | John Doe  | 923001234567  |
| 2    | Not Found | Not Found     |

---

## ✍️ Instructions (also in app sidebar)

1. Upload a PDF file containing scanned bills.
2. The app will extract numbers starting with '923' and associated names from each page.
3. Missing data will be marked as "Not Found."
4. You can download the results as an Excel file.

---

## 🧑‍💻 Author

**Asim Mehmood**  
MPhil Researcher | Bioinformatics & Software Developer  
GitHub: [@Asim-Infomics](https://github.com/Asim-Infomics))

---

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
