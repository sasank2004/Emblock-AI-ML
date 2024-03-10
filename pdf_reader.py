import PyPDF2
import sys

# Open the PDF file
pdf_file = open("C:/Users/sasan/Downloads/SCon.pdf", 'rb')
pdf_out = open("C:/Users/sasan/chatbot_project/outputf.txt", 'w')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from all pages (adjust page range as needed)
text = ""
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()  # Add extracted text from each page

# Close the PDF file
pdf_file.close()

original_stdout = sys.stdout
# Print the extracted text
with open("C:/Users/sasan/chatbot_project/outputf.txt", 'w') as f:
    sys.stdout = f
    print(text)
    sys.stdout = original_stdout