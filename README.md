# deviceaudit

Purpose:
This script will poll the Log Decoder (specified at runtime) for the IPs or Hosts you add into a CSV input file (FILENAME). The output will show when the device last logged if found otherwise, it will show "NO" as in no logs have been seen from that device/event source. This is a valuable script I've used to help bridge the gap of what the customer believes is in their environment and what is actually logging to the SIEM.
Use:

Run as: ./deviceaudit.py -f <FILENAME>

FILENAME here is a single column list of hosts or IPs you want to check.
