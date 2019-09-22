# concert-finder
a simple Python script/CLI tool to find upcoming concerts on Biletix

## To run
first, clone the repo
```sh
git clone https://github.com/omerbselvi/concert-finder.git
```
make sure you have python3 and virtualenv package on your device.
then;
```sh
virtualenv --python=python3 <folder-name>
source <folder-name>/bin/activate
pip install -r requirements.txt
python find_concert.py -h
```
### Usage
```sh
(venv) omer.selvi:concert-finder/ (master) $ python find_concert.py -h                                                                                                                                                      [12:47:34]
Usage: find_concert.py [options]

Options:
  -h, --help            show this help message and exit
  -c CATEGORY, --category=CATEGORY
                        Select a category: ['alternatif', 'blues',
                        'dans_elektronik', 'dunya_muzik', 'heavy_metal',
                        'jazz', 'klasik', 'latin_tango', 'newage', 'party',
                        'pop', 'rap_hiphop', 'rock', 'turksanat_halkmuzik',
                        'other']
  -s SEARCH, --search=SEARCH
                        Search events on biletix
  --city=CITY           Search by selected city

```
### Sample output
```sh
(venv) omer.selvi:concert-finder/ (master✗) $ python find_concert.py -s metal --city istanbul

Checking for mac64 chromedriver:77.0.3865.40 in cache
Driver found in /Users/omer.selvi/.wdm/chromedriver/77.0.3865.40/mac64/chromedriver
Searching by category/search: metal
26/Eyl/Per - %100 Metal İftiharla Sunar Overkill - İstanbul - KüçükÇiftlik Park - http://www.biletix.com/etkinlik/Y0XAN/TURKIYE/tr
29/Eyl/Paz - Mantar - İstanbul - Moda Kayıkhane - http://www.biletix.com/etkinlik/Y0XAT/TURKIYE/tr
15/Ara/Paz - Amorphis - İstanbul - %100 Studio - http://www.biletix.com/etkinlik/Y0XBE/TURKIYE/tr
12/Eki/Cmt - Pentagram - İstanbul - Dorock XL Kadıköy - http://www.biletix.com/etkinlik/YWL4G/TURKIYE/tr
28/Eyl/Cmt - Musa Göçmen Senforock Orkestrası - Metallica Şarkıları - İstanbul - Grand Pera Emek Sahnesi  - http://www.biletix.com/etkinlik/YBQ08/TURKIYE/tr
15/Kas/Cum - Moonspell - Rotting Christ - İstanbul - Moda Kayıkhane - http://www.biletix.com/etkinlik/Y0XAU/TURKIYE/tr
16/Eki/Çar - Musa Göçmen Senforock Orkestrası - Metallica Şarkıları - İstanbul - Grand Pera Emek Sahnesi  - http://www.biletix.com/etkinlik/YBQ12/TURKIYE/tr
21/Eyl/Cmt - Septicflesh - İstanbul - %100 Studio - http://www.biletix.com/etkinlik/Y5H88/TURKIYE/tr
09/Eki/Çar - Murder King - İstanbul - IF Performance Hall Beşiktaş - http://www.biletix.com/etkinlik/YE872/TURKIYE/tr
15/Eki/Sal - Right in Tool - Tool Tribute Band - İstanbul - Dorock XL Kadıköy - http://www.biletix.com/etkinlik/YWL4B/TURKIYE/tr
26/Eki/Cmt - Apocalyptica Plays Metallica By Four Cellos - İstanbul - Volkswagen Arena - http://www.biletix.com/etkinlik/YK3AG/TURKIYE/tr
31/Eki/Per - Yürüyebilen Şapşik Robot Atölyesi - İstanbul - Fenerbahçe Düşyeri Sahne - http://www.biletix.com/etkinlik/YYS06/TURKIYE/tr
30/Kas/Cmt - New Model Army - İstanbul - %100 Studio - http://www.biletix.com/etkinlik/Y5L61/TURKIYE/tr
10/Mar/Sal - Dark Night: She Past Away, Second Still, Box and the Twins - İstanbul - %100 Studio - http://www.biletix.com/etkinlik/Z5G04/TURKIYE/tr
14 concerts found based on your selected category/query: metal - istanbul
```
```sh
(venv) omer.selvi:concert-finder/ (master✗) $ python find_concert.py -s "can gox" --city istanbul                                                       [13:04:28]

Checking for mac64 chromedriver:77.0.3865.40 in cache
Driver found in /Users/omer.selvi/.wdm/chromedriver/77.0.3865.40/mac64/chromedriver
Searching by category/search: can gox
19/Eki/Cmt - Can Gox - İstanbul - Dorock XL Kadıköy - http://www.biletix.com/etkinlik/YWL4J/TURKIYE/tr
21/Eyl/Cmt - Dorock XL Kadıköy Konserleri - İstanbul - Çeşitli Mekanlar - http://www.biletix.com/etkinlik-grup/107308187/TURKIYE/tr
21/Eyl/Cmt - Emaar Hayal Kahvesi Konserleri - İstanbul - Hayal Kahvesi Emaar - http://www.biletix.com/etkinlik-grup/173148434/TURKIYE/tr
10/Eki/Per - Sanat Performance Açıkhava Konserleri  - İstanbul - Çeşitli Mekanlar - http://www.biletix.com/etkinlik-grup/127659605/TURKIYE/tr
21/Eyl/Cmt - Moda Kayıkhane Konserleri - İstanbul - Moda Kayıkhane - http://www.biletix.com/etkinlik-grup/129157757/TURKIYE/tr
27/Eyl/Cum - Müzik Boğazdan Gelir - İstanbul - Çeşitli Mekanlar - http://www.biletix.com/etkinlik-grup/106278191/TURKIYE/tr
21/Eyl/Cmt - Beyrut Performans Konserleri - İstanbul - Beyrut Performans - http://www.biletix.com/etkinlik-grup/107414925/TURKIYE/tr
21/Eyl/Cmt - IF Performance Hall Ataşehir - İstanbul - Çeşitli Mekanlar - http://www.biletix.com/etkinlik-grup/120236962/TURKIYE/tr
8 concerts found based on your selected category/query: can gox - istanbul
```
```sh
(venv) omer.selvi:concert-finder/ (master✗) $ python find_concert.py -c heavy_metal                                                                     [13:03:20]

Checking for mac64 chromedriver:77.0.3865.40 in cache
Driver found in /Users/omer.selvi/.wdm/chromedriver/77.0.3865.40/mac64/chromedriver
Searching by category/search: heavy_metal
26/Eyl/Per - %100 Metal İftiharla Sunar Overkill - İstanbul - KüçükÇiftlik Park - http://www.biletix.com/etkinlik/Y0XAN/TURKIYE/tr
26/Eyl/Per - Overkill - Çeşitli Şehirler - Çeşitli Mekanlar - http://www.biletix.com/etkinlik-grup/203751880/TURKIYE/tr
27/Eyl/Cum - Overkill - İzmir - SoldOut Performance Hall - http://www.biletix.com/etkinlik/Y0XAZ/TURKIYE/tr
28/Eyl/Cmt - Overkill - Ankara - Milyon Performance Hall - http://www.biletix.com/etkinlik/Y0XAO/TURKIYE/tr
28/Eyl/Cmt - Thundermother - İstanbul - KadıköySahne - http://www.biletix.com/etkinlik/YK3AK/TURKIYE/tr
09/Eki/Çar - Murder King - İstanbul - IF Performance Hall Beşiktaş - http://www.biletix.com/etkinlik/YE872/TURKIYE/tr
13/Eki/Paz - Murder King - Ankara - 6:45 KK Ankara - http://www.biletix.com/etkinlik/YE907/TURKIYE/tr
16/Eki/Çar - Murder King - Eskişehir - SPR Pub - http://www.biletix.com/etkinlik/YE894/TURKIYE/tr
18/Eki/Cum - Murder King - İzmir - Volume Alsancak - http://www.biletix.com/etkinlik/YE896/TURKIYE/tr
20/Eki/Paz - Benediction - İzmir - Bios Bar Alsancak - http://www.biletix.com/etkinlik/Y8T30/TURKIYE/tr
25/Eki/Cum - Apocalyptica Plays Metallica By Four Cellos - İzmir - İzmir Arena - http://www.biletix.com/etkinlik/YK3AF/TURKIYE/tr
25/Eki/Cum - Apocalyptica Plays Metallica By Four Cellos - Çeşitli Şehirler - Çeşitli Mekanlar - http://www.biletix.com/etkinlik-grup/201900162/TURKIYE/tr
26/Eki/Cmt - Apocalyptica Plays Metallica By Four Cellos - İstanbul - Volkswagen Arena - http://www.biletix.com/etkinlik/YK3AG/TURKIYE/tr
27/Eki/Paz - Apocalyptica Plays Metallica By Four Cellos - Ankara - Milyon Performance Hall - http://www.biletix.com/etkinlik/YK3AH/TURKIYE/tr
08/Kas/Cum - Dr. Skull - Ankara - Jolly Joker Ankara - http://www.biletix.com/etkinlik/Y0XAY/TURKIYE/tr
13/Ara/Cum - Amorphis - İzmir - SoldOut Performance Hall - http://www.biletix.com/etkinlik/Y0XBC/TURKIYE/tr
13/Ara/Cum - Amorphis - Çeşitli Şehirler - Çeşitli Mekanlar - http://www.biletix.com/etkinlik-grup/213085197/TURKIYE/tr
14/Ara/Cmt - Amorphis - Ankara - Milyon Performance Hall - http://www.biletix.com/etkinlik/Y0XBD/TURKIYE/tr
15/Ara/Paz - Amorphis - İstanbul - %100 Studio - http://www.biletix.com/etkinlik/Y0XBE/TURKIYE/tr
19 concerts found based on your selected category/query: heavy_metal -
```

