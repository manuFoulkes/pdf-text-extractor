import os
import pytest
from src.pdf_processor import PDFProcessor

def test_pdf_processor_initialization():
    processor = PDFProcessor()
    assert processor is not None
    assert processor.progress_callback is None

def test_pdf_processor_with_callback():
    def dummy_callback(progress, status):
        pass
    
    processor = PDFProcessor(dummy_callback)
    assert processor.progress_callback is not None
    assert processor.progress_callback == dummy_callback

def test_update_progress():
    progress_value = None
    status_text = None
    
    def test_callback(progress, status):
        nonlocal progress_value, status_text
        progress_value = progress
        status_text = status
    
    processor = PDFProcessor(test_callback)
    processor.update_progress(0.5, "Testing")
    
    assert progress_value == 0.5
    assert status_text == "Testing"
