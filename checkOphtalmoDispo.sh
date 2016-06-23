#!/bin/bash

#set -e
#set -x

doctolib_url_api='https://partners.doctolib.fr/availabilities/12498/2016-06-23?agenda_ids=9765-10984-2316-2317-2318-2319-2320-2322-2323-2324-2325-2328-2329-2330-2326-2566-2321-2379-2314&insurance_type=&limit=15'
#doctolib_url_api='https://partners.doctolib.fr/availabilities/12498/2016-06-23?agenda_ids=2320&insurance_type=&limit=15'
image="/usr/share/icons/Humanity/actions/128/gtk-info.svg"
title="PRENDRE RDV OPTHALMO"
msg="Vite y'a des rendez-vous de dispo : "

function log() {
	echo "$(date "+%Y/%m/%d %H:%M.%S") : $@"
}

function checkDisponibilite() {
	disponibilite="$(curl -s "${doctolib_url_api}" | tidy -iq 2> /dev/null | grep "div class=\"slots\"" | grep -v '<div class="slots"></div>')"

	if [ -n "${disponibilite}" ]
	then
		disponibilite_details="$(echo "${disponibilite}" | sed -e "s/^.*<div class=\"slots\">\(.*\)<\/div>$/\1/g")"
		log "disponibilité trouvé : \n${disponibilite_details}"
		notify-send -i "$image" -t 120000 "${title}" "${msg} ${disponibilite_details}"
	else
		log "pas de dispo"
	fi
}

while true
do
	checkDisponibilite
	sleep 5m
done
