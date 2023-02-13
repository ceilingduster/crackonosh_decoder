#!/usr/bin/python3
import dns.resolver

def decode(DNS_Record):
        oct = []
        oct.append(10 * (DNS_Record[1] - 97) + 100 * (DNS_Record[0] - 97) + DNS_Record[2] - 97)
        oct.append(10 * (DNS_Record[4] - 97) + 100 * (DNS_Record[3] - 97) + DNS_Record[5] - 97)
        oct.append(10 * (DNS_Record[7] - 97) + 100 * (DNS_Record[6] - 97) + DNS_Record[8] - 97)
        oct.append(10 * (DNS_Record[10] - 97) + 100 * (DNS_Record[9] - 97) + DNS_Record[11] - 97)
        return oct

domains = [
"domain1.org",
"domain2.com",
"domain3.net"
]

for domain in domains:
	answer = dns.resolver.query(domain, "TXT")
	for data in answer:
		for txt_string in data.strings:
			print(domain, data, decode(txt_string))
