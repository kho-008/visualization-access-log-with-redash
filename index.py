import csv
import re
import sys

if len(sys.argv) == 1:
    sys.stdout.write("Usage: %s <access.log> <accesslog.csv>\n"%sys.argv[0])
    sys.exit(0)

log_file_name = sys.argv[1]
csv_file_name = sys.argv[2]

pattern = re.compile(r'(?P<host>\S+).(?P<rfc1413ident>\S+).(?P<user>\S+).\[(?P<datetime>\S+ \+[0-9]{4})]."(?P<httpverb>\S+) (?P<url>\S+) (?P<httpver>\S+)" (?P<status>[0-9]+) (?P<size>\S+) "(?P<referer>.*)" "(?P<useragent>.*)"\s*\Z')

file = open(log_file_name)

with open(csv_file_name, 'w', newline="") as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['host', 'ident', 'user', 'time', 'verb', 'url', 'httpver', 'status', 'size', 'referer', 'useragent'])

    for line in file:
        m = pattern.match(line)
        result = m.groups()
        csv_out.writerow(result)