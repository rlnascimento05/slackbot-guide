import json
import urllib
from helper import *
import system_status
FEEDER_PROCESS_URL="http://172.16.13.61:6100/feeder_processes"

def watch:
  systems = SYSTEMS_TO_WATCH()
  statuses = []
  for url in systems:
    statuses.append(getCurrentStatus(url))

  return statuses

def getCurrentStatus(url):
  response = urllib.urlopen(url)
  data = json.loads(response.read())

  return data

def SYSTEMS_TO_WATCH():
  return [
    'fund-clients-service-qa.aws.guideinvestimentos.com.br:7005/service_status',
    'fund-data-service-qa.aws.guideinvestimentos.com.br:7000/service_status'
  ]