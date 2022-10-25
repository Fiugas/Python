from datetime import datetime
def saveLog(text):
    f = open("log","a")
    now = datetime.now()
    f.write(text + now.strftime("%d/%m/%Y %H:%M:%S")+"\n")
    f.closes