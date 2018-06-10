import urllib.request
import urllib.parse
import urllib.error

def zapisz(nazwa_pliku, tresc):
   open(nazwa_pliku, 'w').write(tresc)

path = input("podaj adres ")
path = "https://" + path + "/"
sock = urllib.request.urlopen(path)

htmlSource = sock.read().decode("utf-8") 
sock.close()
print(htmlSource)
zapisz("str.txt", htmlSource)
