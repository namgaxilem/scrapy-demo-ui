import pymupdf

def modify_attribute_pdf():
    file_path = "docs-scrapy-org-en-latest.pdf"
    doc = pymupdf.open(file_path)
    print("is_encrypted", doc.is_encrypted)
    
    print("xmp_metadata before", doc.get_xml_metadata())
    doc.set_xml_metadata('dcm')
    print("xmp_metadata after", doc.get_xml_metadata())
    
    print("metadata before", doc.metadata)
    doc.set_metadata({ 'title': "Nam Nguyen is author" })
    # doc.set_metadata({ 'crawler_title': "Nam Nguyen is author" })
    # doc.set_metadata({ 'crawler_url': "https://example.com" })
    print("metadata after", doc.metadata)

    doc.save(file_path, incremental=True, encryption=0)
   

modify_attribute_pdf()