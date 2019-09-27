import json
import requests
from helper import *
import system_status
FEEDER_PROCESS_URL="http://172.16.13.61:6100/feeder_processes"

def watch():
  statuses = []
  for url in SYSTEMS_TO_WATCH:
    status = system_status.SystemStatus(url,getCurrentStatus(url))
    statuses.append(status)

  return statuses

def getCurrentStatus(url):
  response = requests.head(url)
  return response.status_code

SYSTEMS_TO_WATCH = [
    'http://fund-clients-service-qa.aws.guideinvestimentos.com.br:7005/service_status',
    'http://fund-data-service-qa.aws.guideinvestimentos.com.br:7000/service_status'
  ]