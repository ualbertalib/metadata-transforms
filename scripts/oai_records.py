#!/usr/bin/env python

import requests
import xml.etree.ElementTree as ET

base = "http://@gillingham2.library.ualberta.ca:8080/fedora/rest/oai?verb=ListRecords"
query = "&metadataPrefix=oai_etdms"
ns = {'OAI-PMH':'http://www.openarchives.org/OAI/2.0/'}
name = 0
while True:
    # setup
    request_url = base + query
    response = requests.get(request_url)
    treeElement = ET.fromstring(response.content)
    elements = treeElement.findall(".//OAI-PMH:resumptionToken", ns)
    # actions
    # exit gracefully if no elements are returned
    if len(elements) == 0:
        break
    token = elements[0].text
    print(token)
    tree = ET.ElementTree(treeElement)
    tree.write(str(name) + ".xml", 'utf-8')
    name += 1 
    if token == "":
        break
    # proxima ronda
    query = "&resumptionToken=" + token
