from fpdf import FPDF
import pandas as pd

df = pd.read_csv('../data/topics.csv')
# create pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    # add page
    pdf.add_page()
    # design the page
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(200, 100, 0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=0)
    pdf.line(10, 25, 200, 25)

    for i in range(row['Pages'] - 1):
        pdf.add_page()


# create a file
pdf.output('output.pdf')
