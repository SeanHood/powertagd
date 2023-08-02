#!/usr/bin/env python

import json

devices = ['deviceid1', 'deviceid2']

states = {
    "total_power_active": {
        "topic": "total_power_active",
        "class": "power",
        "unit": "W"
    },
    "voltage_p1": {
        "topic": "voltage_p1",
        "class": "voltage",
        "unit": "V"
    },
    "total_power_apparent": {
        "topic": "total_power_active",
        "class": "apparent_power",
        "unit": "VA"
    },
    "power_factor": {
        "topic": "power_factor",
        "class": "power_factor",
        "unit": "%"
    },
    "current_p1": {
        "topic": "voltage_p1",
        "class": "current",
        "unit": "A"
    }
}


for device_id in devices:
    for state,s in states.items():

        uniq_id = "powertag_%s_%s" % (device_id, s['class'])

        payload = {
            "state_topic": "powertagd/%s/%s" % (device_id, s['topic']),
            "value_template": "{{ value_json.%s }}" % state,
            "device": {
                "identifiers": device_id,
                "name": "Acti9 PowerTag - %s" % device_id,
                "model": "A9MEM1520",
                "manufacturer": "Schneider"
            },
            "uniq_id": uniq_id,
            "unit_of_meas": s['unit'],
            "device_class": s['class']
        }

        cmd = "mosquitto_pub -h mqtt.t.snhd.co -t homeassistant/sensor/%s/config -m '%s'" % (uniq_id, json.dumps(payload))

        print(cmd)