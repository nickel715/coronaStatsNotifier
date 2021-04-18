from mucinfogram import (
    DataSource,
    Parser
)
from prowl import Prowl
import config

data = DataSource.get_infogram_content()
incidence = Parser.find_incidence(data)
updated = Parser.find_updated(data)

print('Incident from {} is {}'.format(updated, incidence))

last_updated_filename = 'last_updated.txt'
open(last_updated_filename, 'a').close()
with open(last_updated_filename, 'r+') as text_file:
    if text_file.read() != updated:
        prowl = Prowl(config.prowlApiKey)
        prowStatus = prowl.send_notification('Neue 7-Tage-Inzidenz von {} für München. Stand: {}'.format(incidence, updated))
        print('Sent notification with status {}'.format(prowStatus))

        text_file.truncate()
        text_file.write(updated)
    else:
        print('Data not updated. No notification sent')
