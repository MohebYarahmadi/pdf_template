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
    
def draw_lines(ox, oy, count=25, height=12, blank=False):
    y = oy
    length = 200
    if blank:
        pdf.line(ox, oy, length, oy)
        y += height
    
    for i in range(count):
            pdf.line(ox, y, length, y)
            y += height

def gen_lines():
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
        

for index, row in df.iterrows():
    # add page
    pdf.add_page()
    
    # design the page
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(23, 23, 23)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    # draw_lines(10, 25, 26, 12)
    gen_lines()
    
    
    # footer
    footer(265)

    # additional pages for each topic
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        footer(277)
        # draw_lines(10, 12, 26, 12, blank=True)
        gen_lines()

# create a file
pdf.output('output.pdf')
