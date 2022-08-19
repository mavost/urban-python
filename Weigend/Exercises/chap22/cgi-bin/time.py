#!/Python36-32/python.exe

#----------------------------------------------------
# Dateiname:  time.py 
# CGI-Skript, das html-Seite mit aktueller Uhrzeit ausgibt
#
# Objektorientierte Programmierung mit Python
# Kap. 22
# Michael Weigend 17. 10. 09
# update: Mvs 2017-12-07
#----------------------------------------------------
TEMPLATE = """Content-type: text/html; char-set=utf-8

<!DOCTYPE html>
<html>
  <meta http-equiv="content-type" content="charset=UTF-8" />
  <body>
    <h2>Current CET </h2>
      It is {} hours und {} {}.<br><br>
      <a href="../index.html">back...</a>
  </body>
</html>""" #1
    
import cgitb
cgitb.enable()
from time import localtime
time = localtime()
h = time[3]
m = time[4]
if m == 1:
    m_text = "minute"
else:
    m_text = "minutes"

print(TEMPLATE.format(h, m, m_text))
