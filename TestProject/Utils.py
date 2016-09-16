import socket

class Client():
    def __init__(self,Adress=("127.0.0.1",5000)):
        self.Adress = Adress
    def sendData(self,Message):
        self.s = socket.socket()
        self.s.connect(self.Adress)
        self.s.send(str(Message))
    def recieveData(self):
        self.s = socket.socket()
        self.s.connect(self.Adress)
        return  self.s.recv(20)

class Server():
    def __init__(self,Adress=('127.0.0.1',5000),MaxClient=1):
        self.s = socket.socket()
        self.s.bind(Adress)
        self.s.listen(MaxClient)

    def WaitForConnection(self):
        self.Client, self.Adr=(self.s.accept())
        back = self.Client.recv(20)
        return back

    def sendData(self, Message):
        self.Client, self.Adr=(self.s.accept())
        self.Client.send(str(Message))

class Utils():
    def __init__(self):
        pass

    def getLocation(self, eingabe):
        eingabe = eingabe.translate(None, "() ") #Klammern enttfernen
        eingabe = eingabe.split(",") #Am Komma aufteilen
        eingabe = [ int(x) for x in eingabe ] #Nummern aus Strings machen
        eingabe = tuple(eingabe) #Wieder ein tuple draus machen
        eingabe = (eingabe + (25, 25)) #Zusammenfuehren
        return eingabe #Ausgeben
