from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(200,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1, border=1)

    # Set Footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(200, 50, 150)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set Footer
        pdf.ln(275)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(200, 50, 150)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")
