from sommen import maakoptelsommen
from fpdf import FPDF


def main():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_font('Ubuntu Mono', '',
                 '/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf', uni=True)
    pdf.add_page()
    pdf.set_author('Mark de Bruijn')
    pdf.set_font('Ubuntu Mono', size=16)
    pdf.cell(200, 10, txt='{:30} {:16} {:16}'.format(
        'Naam:', 'Begintijd:', 'Eindtijd:'), ln=1, align="C")
    pdf.cell(200, 10, txt='', ln=1, align="L")
    pdf.set_font('Ubuntu Mono', size=18)
    tafels = maakoptelsommen(25)
    spacer = 0
    for a in range(0, len(tafels), 4):
        row = '{:12} {:12} {:12} {:12}'.format(
            tafels[a], tafels[a + 1], tafels[a + 2], tafels[a + 3])

        if spacer == 5:
            pdf.cell(200, 10, txt='', ln=1, align="C")
            spacer = 1
        else:
            spacer += 1
        pdf.cell(200, 10, txt=row, ln=1, align="C")

        if a == 56:
            break

    pdf.image('images/image-super-mario.jpg', x=80,
              y=220, w=50, h=50, type='', link='')
    pdf.output("output/optelsommen.pdf")


if __name__ == '__main__':
    main()
