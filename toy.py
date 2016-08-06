from netzob.all import *

mess1 = PCAPImporter.readFile("/home/mike/Proto-parser/heavy_swings.pcapng").values()
#mess2 = PCAPImporter.readFile("/home/mike/Proto-parser/maims.pcapng").values()
#mess3 = PCAPImporter.readFile("/home/mike/Proto-parser/eye.pcapng").values()
#mess4 = PCAPImporter.readFile("/home/mike/Proto-parser/eye_rot.pcapng").values()

#messages = mess1 + mess2 + mess3 + mess4
messages = mess1

symbol = Symbol(messages = messages)

Format.splitDelimiter(symbol, HexaString('c4'))

print symbol._str_debug()
#print symbol
