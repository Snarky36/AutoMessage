import fbchat
import fbchat
from fbchat.models import *
from fbchat import Client
import time
client1=Client('your email form mess','your pass')
mesaj="Reminder Transfer Bancar:Suma ce trebuie sa o transferati este de 192(pt cei ce nu au dat banii pentru Vladi)/180 pentru restul"
mesaj1="Banca:Garanti."+'\n'+"Proprietar cont: ANDREI CODRUT ZAHARIE"+'\n'+"CODUL IBAN :RO39UGBI0000352013657RON."
mesaj2="Banca: Raiffeisen BANK S.A. - Sucursala Bucuresti"+'\n'+"Proprietar cont: Zimbru Andrei - George" +'\n'+"Cont: RO37RZBR0000060018468527RON"+'\n'+"BIC(SWIFT): RZBRROBU"
mesaj3="Banca: ING Bank N.V. Amsterdam - Sucursala Bucuresti"+'\n'+ " Proprietar cont: Zimbru Andrei - George " +'\n'+"Cont: RO32INGB0000999908889221RON"+'\n'+"BIC(SWIFT): INGBROBU"
mesaj4="codul BIC in caz ca se fac transferuri din strainatate (sau conturi in alte valute)"
mesaj5="Puteti sa trimiteti banii pana Miercuri, 8.04.2020 la ora 16:00"
g=client1.searchForGroups("REAL Keeping up with 12C",1)
print(g[0].uid)
while(True):
    client1.send(Message(text=mesaj), thread_id=g[0].uid, thread_type=ThreadType.GROUP)
    time.sleep(0.1)
    client1.send(Message(text=mesaj1), thread_id=g[0].uid, thread_type=ThreadType.GROUP)
    time.sleep(0.1)
    client1.send(Message(text=mesaj2), thread_id=g[0].uid, thread_type=ThreadType.GROUP)
    time.sleep(0.1)
    client1.send(Message(text=mesaj3), thread_id=g[0].uid, thread_type=ThreadType.GROUP)
    time.sleep(0.1)
    client1.send(Message(text=mesaj4), thread_id=g[0].uid, thread_type=ThreadType.GROUP)
    time.sleep(0.1)
    client1.send(Message(text=mesaj5), thread_id=g[0].uid, thread_type=ThreadType.GROUP)
    time.sleep(21000)
