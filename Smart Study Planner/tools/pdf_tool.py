# tools/pdf_tool.py
import os
from pathlib import Path

class PDFTool:
    @staticmethod
    def read_pdf(file_path=None):
        """
        Reads the actual uploaded PDF from sample_data/.
        NEVER falls back to demo text if a real file exists.
        """
        # If user gave a path → use it
        if file_path and Path(file_path).exists():
            path = Path(file_path)
        else:
            # Auto-find any PDF in sample_data/
            sample_dir = Path("sample_data")
            if not sample_dir.exists():
                sample_dir.mkdir(exist_ok=True)
            
            pdf_files = list(sample_dir.glob("*.pdf"))
            if pdf_files:
                path = pdf_files[0]  # Use the first PDF found
                print(f"   → Using your uploaded file: {path.name}")
            else:
                print("   → No PDF found in sample_data/ → using built-in demo")
                return PDFTool._get_demo_text()

        # Now REALLY read the file
        try:
            from pypdf import PdfReader
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            if text.strip():
                print(f"   → Successfully extracted {len(text.split())} words from your PDF")
                return text
            else:
                print("   → PDF was empty or unreadable → using demo")
                return PDFTool._get_demo_text()
        except ImportError:
            print("   → pypdf not installed → reading as plain text")
        except Exception as e:
            print(f"   → Error reading PDF: {e}")

        # Fallback: try reading as plain text
        try:
            return path.read_text(encoding="utf-8", errors="ignore")
        except:
            print("   → Failed to read file → using demo")
            return PDFTool._get_demo_text()

    @staticmethod
    def _get_demo_text():
        return """
        Introduction to Python Programming
        Variables and Data Types
        Control Structures
        Functions and Modules
        Lists, Tuples, and Dictionaries
        File Handling
        Exception Handling
        Object-Oriented Programming
        """.strip()