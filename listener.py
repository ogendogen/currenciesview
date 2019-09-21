import sys
import time
import logging
import json
import os
import pymysql
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    obj_json = None
    with open(event.src_path, "r") as fileHandler:
        s_json = fileHandler.read()
        obj_json = json.loads(s_json)
    
    os.remove(event.src_path)
    
    if obj_json is None:
        print("Error loading json")
    
    SaveToSQL(obj_json)

def SaveToSQL(obj_json):
    db = pymysql.connect("127.0.0.1", "root", "***", "currencies")
    cursor = db.cursor()
    if "TargetCurrencies" in obj_json:
        curr = obj_json["TargetCurrencies"]
        query = ("INSERT INTO `currencies_gav` SET currency = %s, date = %s, CAD = " + str(curr["CAD"]) +
        ", HKD = " + str(curr["HKD"]) + ", ISK = " + str(curr["ISK"]) + ", PHP = " + str(curr["PHP"]) + ", DKK = " + str(curr["DKK"]) +
        ", HUF = " + str(curr["HUF"]) + ", CZK = " + str(curr["CZK"]) + ", GBP = " + str(curr["GBP"]) + ", RON = " + str(curr["RON"]) +
        ", SEK = " + str(curr["SEK"]) + ", INR = " + str(curr["INR"]) + ", BRL = " + str(curr["BRL"]) + ", RUB = " + str(curr["RUB"]) +
        ", HRK = " + str(curr["HRK"]) + ", JPY = " + str(curr["JPY"]) + ", THB = " + str(curr["THB"]) + ", CHF = " + str(curr["CHF"]) +
        ", EUR = " + str(curr["EUR"]) + ", MYR = " + str(curr["MYR"]) + ", BGN = " + str(curr["BGN"]) + ", TRY = " + str(curr["TRY"]) +
        ", CNY = " + str(curr["CNY"]) + ", NOK = " + str(curr["NOK"]) + ", NZD = " + str(curr["NZD"]) + ", ZAR = " + str(curr["ZAR"]) +
        ", USD = " + str(curr["USD"]) + ", MXN = " + str(curr["MXN"]) + ", SGD = " + str(curr["SGD"]) + ", AUD = " + str(curr["AUD"]) +
        ", ILS = " + str(curr["ILS"]) + ", KRW = " + str(curr["KRW"]) + ", PLN = " + str(curr["PLN"]))
        cursor.execute(query, (str(obj_json["Currency"]), str(obj_json["Date"])))
    else:
        api = obj_json["API"]
        apiv4 = obj_json["APIV4"]
        query = ("INSERT INTO `currencies_lav` SET currency1 = %s, date1 = %s, CAD1 = " + str(api["rates"]["CAD"]) +
        ", HKD1 = " + str(api["rates"]["HKD"]) + ", ISK1 = " + str(api["rates"]["ISK"]) + ", PHP1 = " + str(api["rates"]["PHP"]) + ", DKK1 = " + str(api["rates"]["DKK"]) +
        ", HUF1 = " + str(api["rates"]["HUF"]) + ", CZK1 = " + str(api["rates"]["CZK"]) + ", GBP1 = " + str(api["rates"]["GBP"]) + ", RON1 = " + str(api["rates"]["RON"]) +
        ", SEK1 = " + str(api["rates"]["SEK"]) + ", INR1 = " + str(api["rates"]["INR"]) + ", BRL1 = " + str(api["rates"]["BRL"]) + ", RUB1 = " + str(api["rates"]["RUB"]) +
        ", HRK1 = " + str(api["rates"]["HRK"]) + ", JPY1 = " + str(api["rates"]["JPY"]) + ", THB1 = " + str(api["rates"]["THB"]) + ", CHF1 = " + str(api["rates"]["CHF"]) +
        ", EUR1 = " + str(api["rates"]["EUR"]) + ", MYR1 = " + str(api["rates"]["MYR"]) + ", BGN1 = " + str(api["rates"]["BGN"]) + ", TRY1 = " + str(api["rates"]["TRY"]) +
        ", CNY1 = " + str(api["rates"]["CNY"]) + ", NOK1 = " + str(api["rates"]["NOK"]) + ", NZD1 = " + str(api["rates"]["NZD"]) + ", ZAR1 = " + str(api["rates"]["ZAR"]) +
        ", USD1 = " + str(api["rates"]["USD"]) + ", MXN1 = " + str(api["rates"]["MXN"]) + ", SGD1 = " + str(api["rates"]["SGD"]) + ", AUD1 = " + str(api["rates"]["AUD"]) +
        ", ILS1 = " + str(api["rates"]["ILS"]) + ", KRW1 = " + str(api["rates"]["KRW"]) + ", PLN1 = " + str(api["rates"]["PLN"]) + ", CAD2 = " + str(apiv4["rates"]["CAD"]) +
        ", HKD2 = " + str(apiv4["rates"]["HKD"]) + ", ISK2 = " + str(apiv4["rates"]["ISK"]) + ", PHP2 = " + str(apiv4["rates"]["PHP"]) + ", DKK2 = " + str(apiv4["rates"]["DKK"]) +
        ", HUF2 = " + str(apiv4["rates"]["HUF"]) + ", CZK2 = " + str(apiv4["rates"]["CZK"]) + ", GBP2 = " + str(apiv4["rates"]["GBP"]) + ", RON2 = " + str(apiv4["rates"]["RON"]) +
        ", SEK2 = " + str(apiv4["rates"]["SEK"]) + ", INR2 = " + str(apiv4["rates"]["INR"]) + ", BRL2 = " + str(apiv4["rates"]["BRL"]) + ", RUB2 = " + str(apiv4["rates"]["RUB"]) +
        ", HRK2 = " + str(apiv4["rates"]["HRK"]) + ", JPY2 = " + str(apiv4["rates"]["JPY"]) + ", THB2 = " + str(apiv4["rates"]["THB"]) + ", CHF2 = " + str(apiv4["rates"]["CHF"]) +
        ", EUR2 = " + str(apiv4["rates"]["EUR"]) + ", MYR2 = " + str(apiv4["rates"]["MYR"]) + ", BGN2 = " + str(apiv4["rates"]["BGN"]) + ", TRY2 = " + str(apiv4["rates"]["TRY"]) +
        ", CNY2 = " + str(apiv4["rates"]["CNY"]) + ", NOK2 = " + str(apiv4["rates"]["NOK"]) + ", NZD2 = " + str(apiv4["rates"]["NZD"]) + ", ZAR2 = " + str(apiv4["rates"]["ZAR"]) +
        ", USD2 = " + str(apiv4["rates"]["USD"]) + ", MXN2 = " + str(apiv4["rates"]["MXN"]) + ", SGD2 = " + str(apiv4["rates"]["SGD"]) + ", AUD2 = " + str(apiv4["rates"]["AUD"]) +
        ", ILS2 = " + str(apiv4["rates"]["ILS"]) + ", KRW2 = " + str(apiv4["rates"]["KRW"]) + ", PLN2 = " + str(apiv4["rates"]["PLN"]) + ", currency2 = %s, date2 = %s")
        cursor.execute(query, (str(api["base"]), str(api["date"]), str(apiv4["base"]), str(apiv4["date"])))
    try:
        db.commit()
        print("SQL INSERT success")
    except:
        db.rollback()
        
    db.close()

if __name__ == "__main__":
    print("Watchdog started")
    patterns = "*.json"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created

    path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()