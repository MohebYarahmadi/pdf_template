from fpdf import FPDF
import pandas as pd

df = pd.read_csv('../data/topics.csv')
# create pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

def footer(ln):
    pdf.ln(ln)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
    
def draw_line(ox, oy, count=25, height=12, blank=False):
    y = oy
    length = 200
    if blank:
        pdf.line(ox, oy, length, oy)
        y += height
    
    for i in range(count):
            pdf.line(ox, y, length, y)
            y += height
        

for index, row in df.iterrows():
    # add page
    pdf.add_page()
    
    # design the page
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(200, 100, 0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    draw_line(10, 25, 26, 12)
    
    
    # footer
    footer(265)

    # additional pages for each topic
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        footer(277)
        draw_line(10, 12, 26, 12, blank=True)

# create a file
pdf.output('output.pdf')
