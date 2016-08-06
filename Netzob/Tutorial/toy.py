from netzob.all import *

mess1 = PCAPImporter.readFile("target_src_v1_session1.pcap").values()
mess2 = PCAPImporter.readFile("target_src_v1_session2.pcap").values()
mess3 = PCAPImporter.readFile("target_src_v1_session3.pcap").values()

messages = mess1 + mess2 + mess3

symbol = Symbol(messages = messages)

#Format.splitDelimiter(symbol, ASCII('#'))

#print symbol._str_debug()
print symbol
