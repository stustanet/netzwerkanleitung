from pathlib import Path
import re

# generates the tex file for the max bill out of the Stusta file
# replaces the below defined strings and pictures statically
# works for english and german

path_ger=Path('Netzwerkanleitung.tex')
path_eng=Path('Netzwerkanleitung_EN.tex')

# list of stuff that need to be replaced
replacements=[
    (' Studentenstadt Freimann:',' Max-Bill-Straße 67:'), # Address
    ('10.150.xxx.254','10.149.xxx.1'), # Gateway
    ('10.150.243.254','10.149.243.1'), # Gateway example
    ('{254}','{1}'), # Gateway number
    ('10.150.127.2','10.149.8.2'), # DNS 1
    ('10.150.125.2','10.156.33.53'), # DNS 2
    ('10.150.','10.149.'), # rest of IPs
    ('http://wpad.stusta.mhn.de/proxy.pac', 'http://wpad.mb67.stusta.mhn.de/proxy.pac'), # proxy script
    ('http://proxy.stusta.mhn.de:3128', 'http://proxy.mb67.stusta.mhn.de:3128'), # manual proxy
    ('{stusta.mhn.de}', '{mb67.swh.mhn.de}'),
    ('{Bilder/IP_Gerneric}', '{Bilder/IP_Gerneric_mb}'),
    ('{Bilder/IP_Windows}', '{Bilder/IP_Windows_mb}'),
    ('{Bilder/IP_Ubuntu_neu}', '{Bilder/IP_Linux_mb_neu}'),
    ('{Bilder/IP_MAC}', '{Bilder/IP_MAC_mb}'),
    ('{Bilder/Firefox_neu_proxy}', '{Bilder/Firefox_proxy_mb_neu}'),
    ('{Bilder/Proxy_Edge}','{Bilder/Proxy_Edge_mb}'),
    ('{Bilder/IP_Gerneric_EN}', '{Bilder/IP_Gerneric_EN_mb}'),
    ('{Bilder/IP_Windows_EN}','{Bilder/IP_Windows_EN_mb}'),
    ('{Bilder/IP_Mac_EN}', '{Bilder/IP_Mac_EN_mb}'),
    ('{Bilder/firefox_en_stusta}', '{Bilder/firefox_en_mb}'),
    ('{Bilder/Proxy_Edge_EN}', '{Bilder/Proxy_Edge_EN_mb}')
]

with open(path_ger, encoding='utf-8') as file:
    source_ger=file.read()

with open(path_eng, encoding='utf-8') as file:
    source_eng=file.read()

for stusta,mb in replacements:
    source_ger=source_ger.replace(stusta,mb) # replace stusta occurences
    source_eng = source_eng.replace(stusta, mb)  # replace stusta occurences

#pictures=re.findall(r'({Bilder/[^\}]+)\}', source_ger) # find all pictures

#for picture in pictures:
#    if picture == '{Bilder/StuStaNet_Logo':
#        continue
#    source_ger=source_ger.replace(picture, picture+'_mb') # change pictures to _mb variant

with open("Netzwerkanleitung_mb.tex", "w", encoding='utf-8') as text_file:
    text_file.write(source_ger)

with open("Netzwerkanleitung_EN_mb.tex", "w", encoding='utf-8') as text_file:
    text_file.write(source_eng)
