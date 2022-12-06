from fpdf import FPDF


class PDFView(FPDF):
    
    def create_pdf(self):
        self.add_page()
        self.add_font("Sans", style="", fname="ui/fonts/NotoSans-Regular.ttf", uni=True)
        self.set_font("Sans", size=12)

    def write_to_pdf(self, text: str):
        self.write(h=12, txt=text)

    def output_pdf(self):
        self.output('list_book.pdf')
        
