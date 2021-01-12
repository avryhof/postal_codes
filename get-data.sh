#!/bin/bash
locations='US PR VI GU MP AZ'
LOCATION_BASE=http://download.geonames.org/export/zip/
#LOCATION_ADDRESS=http://download.geonames.org/export/zip/${location}.zip
rm *.zip
rm *.txt
wget ${LOCATION_BASE}/US.zip
unzip -o US.zip
wget ${LOCATION_BASE}/PR.zip
unzip -o PR.zip
wget ${LOCATION_BASE}/VI.zip
unzip -o VI.zip
wget ${LOCATION_BASE}/GU.zip
unzip -o GU.zip
wget ${LOCATION_BASE}/MP.zip
unzip -o MP.zip
wget ${LOCATION_BASE}/AZ.zip
unzip -o AZ.zip
rm US.zip PR.zip VI.zip GU.zip MP.zip AZ.zip
