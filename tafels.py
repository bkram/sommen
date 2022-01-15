import random

from fpdf import FPDF


def shuffle(array):
    random.shuffle(array)
    return array


def maaktafels():
    sommen = []
    for counter in range(1, 11):
        for table in range(1, 11):
            sommen.append('{:2} x {:2} ='.format(counter, table))
    return shuffle(sommen)


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
    pdf.set_font('Ubuntu Mono', size=20)
    tafels = maaktafels()
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

    pdf.image('image-animal-crossing.jpg', x=80,
              y=220, w=50, h=50, type='', link='')
    pdf.output("tafels.pdf")
    # pdf.output()


if __name__ == '__main__':
    main()