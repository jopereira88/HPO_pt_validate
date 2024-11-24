# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import sys

def get_translator(init,db='translatorsDb.csv'):
    '''Checks if the initials of the translator are in the database
    Returns the name and country of the translator'''
    try:    
        tdb=pd.read_csv(db)
    
        for i in range(len(tdb)):
            if tdb[i:][tdb['Initials']==init].empty == False :
                last=tdb.loc[tdb['Initials']==init, ['LastName']].to_numpy()
                first=tdb.loc[tdb['Initials']==init, ['FirstName']].to_numpy()
                country=tdb.loc[tdb['Initials']==init, ['Country']].to_numpy()
                country=str(country[0,0])
                name=str(first[0,0])+' '+str(last[0,0])
            else:
                print('Initials not found')
                raise ValueError
        return name, country
    except ValueError:
        print('Select a valid translator')
    except FileNotFoundError:
        print('File not found')
        print('Select a valid file')

def validationloop_csv(dataframe,translator=tuple):
    '''creates the validation loop for the translation dataframe
    Accepts a .csv file (with a ; separator) and the translator details tuple
    Returns a list of lists corresponding to the .csv cells'''    
    try:
        lines=[]
        dataset=open(dataframe,'r')
        for line in dataset.readlines():
            line=str(line.strip())
            list_line=line.split(';')
            lines.append(list_line)
        for l in range(1,len(lines)):
            if lines[l][6] != 'CANDIDATE':
                print(lines[l][2],'| ',lines[l][4],'| ',lines[l][5])
                choice1=str(input('Need to correct? (y/n, q to quit other keys to pass)'\
                                  ))
                if  choice1.upper() == 'Y':
                    lines[l][5] = str(input('Insert corrected term: '))
                    lines[l][6] = 'CANDIDATE'
                    lines[l][7] = translator[0]
                    lines[l][8] = translator[1]
                    lines[l][10]= str(datetime.date.today())
                    print(lines[l])
                elif choice1.upper() == 'N':
                    lines[l][6] = 'CANDIDATE'
                    lines[l][7] = translator[0]
                    lines[l][8] = translator[1]
                    lines[l][10]= str(datetime.date.today())
                    print(lines[l])
                elif choice1.upper() == 'Q':
                    return lines
                else:
                    continue
        return lines
    except FileNotFoundError:
        print('file not found')
        sys.exit()
def linewriter(dataframe,lines=list):
    '''Writes to the csv file the updated lines'''
    with open(f'{dataframe}','w') as output:
        for i in range(len(lines)):
            output.write( f'{lines[i][0]};{lines[i][1]};{lines[i][2]};{lines[i][3]}\
                         ;{lines[i][4]};{lines[i][5]};{lines[i][6]};{lines[i][7]}\
                             ;{lines[i][8]};{lines[i][9]};{lines[i][10]}\n')


############################################################# CODE ##############################################################################

if __name__ == '__main__':
    dataframe=sys.argv[1]
    initials=sys.argv[2]

# dataframe='HPO_pt_1.csv'
# initials='JP'
translator=get_translator(initials)
lines=validationloop_csv(dataframe,translator)
linewriter(dataframe,lines)

