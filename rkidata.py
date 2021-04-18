import requests
import pandas as pd

RKI_XLSX = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Fallzahlen_Kum_Tab.xlsx?__blob=publicationFile'
MUC_STATS = 'https://www.muenchen.de/rathaus/Stadtverwaltung/Referat-fuer-Gesundheit-und-Umwelt/Infektionsschutz/Neuartiges_Coronavirus.html'
XPATH = '//*[@class="InfographicEditor-Contents-Item"][14]//span[@data-text="true"]'

response = requests.get(RKI_XLSX)
data = pd.read_excel(response.content)
