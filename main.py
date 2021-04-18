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

prowl = Prowl(config.prowlApiKey)
#prowl.send_notification('Neue 7-Tage-Inzidenz von {} für München. Stand: {}'.format(incidence, updated))
