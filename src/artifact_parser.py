from pathlib import Path

from bs4 import BeautifulSoup
from pypdf import PdfReader

def extract_pdf_text(file_path):
    path = Path(file_path)
    
    reader = PdfReader(path)
    
    pages = []
    
    for page in reader.pages:
        text = page.extract_text()
        
        if text:
            pages.append(text)
    
    return "\n".join(pages)

def extract_html_text(file_path):
    path = Path(file_path)
    html = path.read_text()
    
    soup = BeautifulSoup(html, "html.parser")
    
    text = soup.get_text(separator="\n", strip=True)
    
    start = text.find("About Alta Fox Capital")
    end = text.find("Back to Top")
    
    job_description = text[start:end]

    return job_description
    
    
if __name__ == "__main__":
    jd = extract_html_text("artifacts/job_descriptions/Software Developer — Alta Fox Capital.html")
    resume = extract_pdf_text("artifacts/resumes/Sayeed J. Software Engineer Resume 1.24.pdf")
    
    # print(jd) 
    print(resume)
    
    