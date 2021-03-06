import requests
import zipfile
import io
import pdfkit
from datetime import datetime
from memory_profiler import profile
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)


def upload(link):
    response = requests.get(link)

    try:
        z = zipfile.ZipFile(io.BytesIO(response.content))
    except zipfile.BadZipFile as e:
        print('Неверный формат файла')
        logging.info(f'Неверный формат файла - {e}')
    except zipfile.LargeZipFile as e:
        print('Размер файла превышает 2 Gb')
        logging.info(f'Размер файла превышает 2 Gb - {e}')

    file_name = link.split('/')[-1].split('.')[0]

    z.extractall()

    logging.info(f'Название файла {file_name}.zip')
    logging.info(f'Дата {datetime.now()}')


WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'


# options = {
#     'enable-local-file-access': 'true',
# }


# fp = open('sample.log', 'w+')
# @profile
def html_to_pdf(file):
    start_time = datetime.now()

    conf = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    pdfkit.from_file(file, 'index.pdf', configuration=conf)

    total_time = datetime.now() - start_time
    logging.info(f'Время затраченное на конвертацию {total_time}')


if __name__ == '__main__':
    upload('https://github.com/Spartacusc/test/blob/main/zipfile.zip?raw=true')

    html_to_pdf('testtest.html')
    # html_to_pdf('index.html')
