import json
import urllib
from helper import *
FEEDER_PROCESS_URL="http://172.16.13.61:6100/feeder_processes"

def getFeederProcessStatus(reference_date):
  url = FEEDER_PROCESS_URL+"?reference_date="+reference_date
  response = urllib.urlopen(url)
  data = json.loads(response.read())
  #TODO: Retornar quais feeders ficaram faltando no dia.

  return data['meta']['total']