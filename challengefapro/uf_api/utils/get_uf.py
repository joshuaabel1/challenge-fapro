import requests
from bs4 import BeautifulSoup
from decimal import Decimal

month_array = {
    "1": "Ene",
    "2": "Feb",
    "3": "Mar",
    "4": "Abr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Ago",
    "9": "Sept",
    "10": "Oct",
    "11": "Nov",
    "12": "Dic",
}


def get_uf_html(url):
    response = requests.get(url)
    
    if not response.status_code == 200:
        return None
    
    return response.text


def extract_uf_value(html, month, day):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"id": "table_export"})

    if not table:
        return None

    rows = table.find_all("tr")
    headers = [th.text.strip() for th in rows[0].find_all("th")]

    month_name = month_array[month.lstrip("0")]
    month_index = headers.index(month_name)

    day_row = rows[int(day)]
    cells = day_row.find_all("td")
    value_text = cells[month_index - 1].text.strip()

    if not value_text:
        return None

    value_text = value_text.replace(".", "").replace(",", ".")
    uf_value = Decimal(value_text)

    uf_value_str = '{:,.2f}'.format(uf_value)
    uf_value_str = uf_value_str.replace(".", "X").replace(",", ".").replace("X", ",")

    return uf_value_str



def get_uf_value(date):
    year, month, day = date.split("-")
    month_name = month_array[month.lstrip("0")]

    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"
    html = get_uf_html(url)

    if not html:
        return None

    uf_value = extract_uf_value(html, month, day)

    return uf_value


