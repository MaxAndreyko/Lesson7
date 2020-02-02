import datetime
from docxtpl import DocxTemplate


def get_context(brand, model, fuel, price):
    return{
        'brand_name': brand,
        'model': model,
        'fuel_cons': fuel,
        'price': price,
    }

def from_template(brand, model, fuel, price, template):
    template = DocxTemplate(template)
    context = get_context(brand, model, fuel, price)

    template.render(context)
    template.save(str(datetime.datetime.now().date()) + '_report.docx')

def generate_report(brand, model, fuel, price):
    template = 'report.docx'
    document = from_template(brand, model, fuel, price, template)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

with open('data') as f:
    for line in f:
        new_list = line.split(',')
        generate_report(new_list[0], new_list[1], new_list[2], new_list[3])




