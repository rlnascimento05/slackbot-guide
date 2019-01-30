import json
import urllib
from helper import *
import feeder_status
FEEDER_PROCESS_URL="http://172.16.13.61:6100/feeder_processes"

def getFeederProcessStatus(reference_date):
  url = FEEDER_PROCESS_URL+"?reference_date="+reference_date
  response = urllib.urlopen(url)
  data = json.loads(response.read())
  #TODO: Retornar quais feeders ficaram faltando no dia.

  status_feeder = feeder_status_factory(CURRENT_FEEDER_PROCESSES())
  for iten in data['data']:
    attributes = iten['attributes']
    key = attributes['origin']+'/'+attributes['interface']
    if key in status_feeder.keys():
      status_feeder[key].status = attributes['status']
      status_feeder[key].error  = attributes['error']

  return status_feeder

def feeder_status_factory(current_feeder): #TODO: Think of a better name
  status = {origin+'/'+interface : feeder_status.FeederStatus(origin, interface)
      for origin, interface in (feeder.split('/') 
        for feeder in current_feeder)}

  return status

def CURRENT_FEEDER_PROCESSES():
  return [
    'forwards/positions',
    'equities/lending',
    'options/positions',
    'equities/positions',
    'direct_treasury/collaterals',
    'direct_treasury/positions',
    'equities/collaterals',
    'current_account/collaterals'
  ]