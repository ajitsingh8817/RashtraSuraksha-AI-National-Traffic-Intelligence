from fpdf import FPDF

def generate_pdf(risk):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200,10,"RashtraSuraksha AI Report",ln=True)
    pdf.cell(200,10,f"Predicted Risk Index: {risk}",ln=True)
    pdf.output("Traffic_Report.pdf")