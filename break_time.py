import webbrowser
import time
i=0
print("program started at :"+time.ctime())
while i < 24:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=eRDojLoCDpQ")
    i=i+2
