import logging

class TheLog():
    def __init__(self):
        logging.basicConfig(filename='logs.log', format='%(filename)s: %(message)s', level=logging.DEBUG)

    def Erreur(self):
        logging.warning("warning")
    
    def Infolog(self,msg):
        logging.info(str(msg))
        print(str(msg))
        
    def SauvMsg(self,author,msg):
        logging.debug(str(author)+": "+str(msg))
