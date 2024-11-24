import os

class Translator:
    '''Primes the name and country of the translator
    Accepts: first - first name (str) / last - last name (str)
    country - country (str)'''

    #Class attribute: Translator DB filename and path
    transDb='translatorsDb.csv'
 
    def __init__(self, first: str, last: str, country: str):
        self.first_name = first
        self.last_name = last
        if country.upper() in ('PORTUGAL','PT'):
            nat='pt'
        elif country.upper() in ('BRASIL','BRAZIL','BR'):
            nat='br'
        else:
            nat='other'
        self.country = nat
    def getCountry(self):
        return self.country
    def getInitials(self):
        return self.first_name[0].upper()+self.last_name[0].upper()
    def saveTranslator(self):
        file=open(self.transDb,'r+')
        innit=self.getInitials()
        transline=f'{innit},{self.first_name},{self.last_name},{self.country}\n'
        print(transline)
        for line in file.readlines():
            if transline.split(',')[0] == line.split(',')[0]:
                print(f'Translator {innit} already saved')
            else:
                file.write(transline)
def checkTranslator(db):
    with open(db,'r') as file:
        for line in file.readlines():
            print(line)

exit = False
# initiating app loop
while not exit:
    opt = 0
    print('#'*60)
    print('Choose option:')
    print('1) Register new translator')
    print('2) Check available translators')
    print('3) Close program')
    print('#'*60)
    try:    
        opt=int(input('Option:  '))
        if opt == 1 and os.path.exists('translatorsDb.csv'):
            first=input('Insert first name: ')
            last=input('Insert last name: ')
            country=input('Insert nationality: ')
            trans=Translator(first,last,country)
            trans.saveTranslator()
            opt=0
        elif opt == 1 and not os.path.exists('translatorsDb.csv'):
            print('translatorsDb.csv not found.')
            print('Creating file')
            with open('translatorsDb.csv','w') as file:
                file.write('Initials,FirstName,LastName,Country\n')
            first=input('Insert first name: ')
            last=input('Insert last name: ')
            country=input('Insert nationality: ')
            trans=Translator(first,last,country)
            trans.saveTranslator()
            opt=0

        elif opt == 2:
            if os.path.exists('translatorsDb.csv'):
                checkTranslator(Translator.transDb)
            else:
                print('translatorsDb.csv not found.')
            opt=0
        elif opt == 3:
            print('Exiting program')
            exit=True
    except ValueError:
        print('Invalid option')
        opt=0
