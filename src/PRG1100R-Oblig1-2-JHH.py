def main():

    kolonner = 7

    student_fil = open('Studenter.txt', 'r')
    linjer = sum(1 for line in student_fil)
    student_fil.close()

    rad = linjer // kolonner

    studenter = [[''for c in range(kolonner)] for r in range (rad)]

    student_fil = open('Studenter.txt', 'r', encoding='utf-8')

    for r in range(rad):
        for c in range(kolonner):
            studenter[r][c] = student_fil.readline().rstrip('\n')

    student_fil.close()
    ferdig = True
    while ferdig == True:
        print('### HOVEDMENY ###')
        print('1. Alle studenter med alle studentopplysninger')
        print('2. Alle studenter på samme studium som deg selv')
        print('3. Alle studenter som er født samme år som deg')
        print('4. Alle studenter med fornavn, etternavn og e-postadresse')
        print('5. Alle studenter på studiet "Bach IT og IS"')
        print('6. Alle kvinnelige studenter på "Bach IT og IS"')
        print('7. Alle mannlige studenter på "Årsstudium IT og IS"')
        print('8. Alle studenter født etter 1.1.1990')
        print('9. Alle studenter født på 1980-tallet')
        print('10. Alle kvinnelige studenter på "Bach IT og IS" født mellom 1.1.1988 og 31.12.1997')
        print('11. Alle mannlige studenter med etternavn som starter på A')
        print('12. Alle studenter med studentnr som starter på 146')
        print('13. Antallet studenter på hvert studium')
        print('14. Antallet mannlige og kvinnelige studenter på hvert studium')
        print('15. Informasjon om den yngste studenten')
        print('16. Informasjon om den eldste studenten på hvert studium')
        print('17. Informasjon om den yngste og den eldste studenten på hvert studium')
        print('18. Alle studenter organisert etter studium og i tillegg alfabetisert på etternavn')
        print()

        valg = input('Velg funksjon(1-18): ')
        print()

        if valg == '1':
            funk1(studenter, rad)
        if valg == '2':
            funk2(studenter, rad)
        if valg == '3':
            funk3(studenter, rad)
        if valg == '4':
            funk4(studenter, rad)
        if valg == '5':
            funk5(studenter, rad)
        if valg == '6':
            funk6(studenter, rad)
        if valg == '7':
            funk7(studenter, rad)
        if valg == '8':
            funk8(studenter, rad)
        if valg == '9':
            funk9(studenter, rad)
        if valg == '10':
            funk10(studenter, rad)
        if valg == '11':
            funk11(studenter, rad)
        if valg == '12':
            funk12(studenter, rad)
        if valg == '13':
            funk13(studenter, rad)
        if valg == '14':
            funk14(studenter, rad)
        if valg == '15':
            funk15(studenter, rad)
        if valg == '16':
            funk16(studenter, rad)
        if valg == '17':
            funk17(studenter, rad)
        if valg == '18':
            funk18(studenter, rad)
      
def funk1(studenter, rad):
    
    c=0
    print('Alle studenter med alle opplysninger: ')
    print('--' * 25)
    print()
    for r in range(rad):
        print('Studentnr:   ', studenter[r][c])
        print('Fornavn:     ', studenter[r][c+1])
        print('Etternavn:   ', studenter[r][c+2])
        print('E-post:      ', studenter[r][c+3])
        print('Fødselsdato: ', studenter[r][c+4])
        print('Kjønn:       ', studenter[r][c+5])
        print('Studie:      ', studenter[r][c+6])
        print('--' * 25)
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny: ')
    if nytt_valg == '':
        ferdig = False

def funk2(studenter, rad):

    c=1
    print('Alle studenter som går på samme studium som meg: ')
    print('--' * 25)
    print()
    for r in range(rad):
        if studenter[r][c+5] == 'Bach IT og IS':
            if studenter[r][c-1] != '146556':
                print(' - ', studenter[r][c-1], studenter[r][c], studenter[r][c+1])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False
        
def funk3(studenter, rad):

    c=1
    print('Alle studenter som er født samme år som meg: ')
    print('--' * 25)
    print()
    for r in range(rad):
        if '1994' in studenter[r][c+3]:
            print(' - ', studenter[r][c-1], studenter[r][c], studenter[r][c+1])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False

def funk4(studenter, rad):

    c=1
    print('Alle studenter med fornavn, etternavn og e-post: ')
    print('--' * 25)
    print()
    for r in range(rad):
        print ('Fornavn:   ', studenter[r][c])
        print ('Etternavn: ', studenter[r][c+1])
        print ('E-post:    ', studenter[r][c+2])
        print('--' * 25)
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False
        

def funk5(studenter, rad):

    c=6
    print('Alle studenter på studiet "Bach IT og IS": ')
    print('--' * 25)
    print()
    for r in range(rad):
        if studenter[r][c] == 'Bach IT og IS':
            print(' - ', studenter[r][c-6], studenter[r][c-5], studenter[r][c-4])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False

def funk6(studenter, rad):

    c=5
    print('Alle kvinnelige studenter på "Bach IT og IS": ')
    print('--' * 25)
    print()
    for r in range(rad):
        if studenter[r][c] == 'K' and studenter[r][c+1] == 'Bach IT og IS':
            print(' - ', studenter[r][c-5], studenter[r][c-4], studenter[r][c-3])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False

def funk7(studenter, rad):

    c=5
    print('Alle mannlige studenter på "Årsstudium IT og IS": ')
    print('--' * 25)
    print()
    for r in range(rad):
        if studenter[r][c] == 'M' and studenter[r][c+1] == 'Årsstudium IT og IS':
            print(' - ', studenter[r][c-5], studenter[r][c-4], studenter[r][c-3])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False

def funk8(studenter, rad):

    c=1
    print('Alle studenter født etter 1.1.1990: ')
    print('--' * 25)
    print()
    for r in range(rad):
        if studenter[r][c+3][:4] > '0101' and studenter[r][c+3][4:] >= '1990':
            print(' - ', studenter[r][c-1], studenter[r][c], studenter[r][c+1], ', med fødselsdato: ', studenter[r][c+3][:2],studenter[r][c+3][2:4],studenter[r][c+3][4:])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False

def funk9(studenter, rad):

    c=1
    print('Alle studenter født på 1980-tallet: ')
    print('--' * 25)
    print()
    for r in range(rad):
        if studenter[r][c+3][4:] >= '1980' and studenter[r][c+3][4:] <= '1989':
            print(' - ', studenter[r][c-1], studenter[r][c], studenter[r][c+1])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False

def funk10(studenter, rad):

    c=1
    print('Alle kvinnelige studenter på "Bach IT og IS" født mellom 1.1.1988 og 31.12.1997: ')
    print('--' * 45)
    print()
    for r in range(rad):
        if studenter[r][c+4] == 'K' and studenter[r][c+5] == 'Bach IT og IS':
            if studenter[r][c+3][:4] > '0101' and studenter[r][c+3][4:] >= '1988':
                if studenter[r][c+3][:4] < '3112' and studenter[r][c+3][4:] <= '1997':
                    print(' - ', studenter[r][c-1], studenter[r][c], studenter[r][c+1], ', med fødselsdato: ', studenter[r][c+3][:2],studenter[r][c+3][2:4],studenter[r][c+3][4:])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False
 


def funk11(studenter, rad):

    c=1
    print('Alle mannlige studenter med etternavn som starter på A: ')
    print('--' * 25)
    print()
    for r in range(rad):
        if studenter[r][c+4] == 'M':
            if studenter[r][c+1][:1] == 'A':
                print(' - ', studenter[r][c-1], studenter[r][c], studenter[r][c+1])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False

#Studentfila må lagres uten bom i Notepad++ for å vise første studenten i funk12

def funk12(studenter, rad):

    c=1
    print('Alle studenter med studentnummer som starter på 146: ')
    print('--' * 25)
    print()
    for r in range(rad):
        if studenter[r][c-1][:3] == '146':
            print(' - ', studenter[r][c-1], studenter[r][c], studenter[r][c+1])
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False



def funk13(studenter, rad):

    c=1

    antall_bachelor = 0
    antall_aarstudium = 0
    print('Antallet studenter på hvert studium: ')
    print('--' * 25)
    print()
    for r in range(rad):
        studium = studenter[r][c+5]
        if studium == 'Bach IT og IS':
            antall_bachelor += 1
        if studium == "Årsstudium IT og IS":
            antall_aarstudium += 1

    

    print('Bach IT og IS: ')
    print(antall_bachelor, 'studenter')
    print()
    print('Årrsstudium IT og IS: ')
    print(antall_aarstudium, 'studenter')
    
    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False

    
    
def funk14(studenter, rad):

    c=1

    antall_kvinner_bach = 0
    antall_menn_bach = 0
    antall_kvinner_aars = 0
    antall_menn_aars = 0
    print('Antallet mannlige og kvinnelige studenter på hvert studium: ')
    print('--' * 35)
    print()
    for r in range(rad):
        kjønn = studenter[r][c+4]

        if studenter[r][c+5] == 'Bach IT og IS':
            if kjønn == 'K' and studenter[r][c+5]:
                antall_kvinner_bach += 1
            if kjønn == "M" and studenter[r][c+5]:
                antall_menn_bach += 1
    

        if studenter[r][c+5] == 'Årsstudium IT og IS':
            if kjønn == 'K' and studenter[r][c+5]:
                antall_kvinner_aars += 1
            if kjønn == "M" and studenter[r][c+5]:
                antall_menn_aars += 1

    print('Bach IT og IS: ')
    print(antall_kvinner_bach, 'kvinnelige studenter')
    print(antall_menn_bach, 'mannlige studenter')
    print()
    print('Årrsstudium IT og IS: ')
    print(antall_kvinner_aars, 'kvinnelige studenter')
    print(antall_menn_aars, 'mannlige studenter')

    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False
    
   

def funk15(studenter, rad):

    c=1
    yngst = 0
    print('Informasjon om den yngste studenten: ')
    print('--' * 25)
    print()
    for r in range(rad):
        dato_yngst = int(studenter[r][c+3][4:] + studenter[r][c+3][2:4] + studenter[r][c+3][:2])
        
        if dato_yngst > yngst:
            yngst = dato_yngst
            yngst_studnr = studenter[r][c-1]
            yngst_fornavn = studenter[r][c]
            yngst_etternavn = studenter[r][c+1]
            yngst_aar = studenter[r][c+3][4:]
            yngst_mnd = studenter[r][c+3][2:4]
            yngst_dag = studenter[r][c+3][:2]
    
    print(yngst_studnr, yngst_fornavn, yngst_etternavn, ', med fødselsdato: ', yngst_dag, yngst_mnd, yngst_aar)

    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False


def funk16(studenter, rad):

    c=1
    eldst_bach = 9999999999999999
    eldst_aars = 9999999999999999
    print('Informasjon om den eldste studenten på hvert studium: ')
    print('--' * 35)
    print()

    for r in range(rad):

        dato_eldst = int(studenter[r][c+3][4:] + studenter[r][c+3][2:4] + studenter[r][c+3][:2])
        if studenter[r][c+5] == 'Bach IT og IS':
            
            if dato_eldst < eldst_bach:
                eldst_bach = dato_eldst
                eldst_studnr_bach = studenter[r][c-1]
                eldst_fornavn_bach = studenter[r][c]
                eldst_etternavn_bach = studenter[r][c+1]
                eldst_aar_bach = studenter[r][c+3][4:]
                eldst_mnd_bach = studenter[r][c+3][2:4]
                eldst_dag_bach = studenter[r][c+3][:2]

        if studenter[r][c+5] == 'Årsstudium IT og IS':
         
            if dato_eldst < eldst_aars:
                eldst_aars = dato_eldst
                eldst_studnr_aars = studenter[r][c-1]
                eldst_fornavn_aars = studenter[r][c]
                eldst_etternavn_aars = studenter[r][c+1]
                eldst_aar_aars = studenter[r][c+3][4:]
                eldst_mnd_aars = studenter[r][c+3][2:4]
                eldst_dag_aars = studenter[r][c+3][:2]
                
    print('Bach IT og IS: ')
    print(eldst_studnr_bach, eldst_fornavn_bach, eldst_etternavn_bach, ', med fødselsdato: ', eldst_dag_bach, eldst_mnd_bach, eldst_aar_bach)
    print()
    print('Årsstudium IT og IS: ')
    print(eldst_studnr_aars, eldst_fornavn_aars, eldst_etternavn_aars, ', med fødselsdato: ', eldst_dag_aars, eldst_mnd_aars, eldst_aar_aars)

    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False
   
def funk17(studenter, rad):

    c=1
    eldst_bach = 9999999999999999
    eldst_aars = 9999999999999999
    yngst_bach = 0
    yngst_aars = 0

    for r in range(rad):

        dato_yngst = int(studenter[r][c+3][4:] + studenter[r][c+3][2:4] + studenter[r][c+3][:2])
        dato_eldst = int(studenter[r][c+3][4:] + studenter[r][c+3][2:4] + studenter[r][c+3][:2])
        
        if studenter[r][c+5] == 'Bach IT og IS':
        
            if dato_yngst > yngst_bach:
                yngst_bach = dato_yngst
                yngst_studnr_bach = studenter[r][c-1]
                yngst_fornavn_bach = studenter[r][c]
                yngst_etternavn_bach = studenter[r][c+1]
                yngst_aar_bach = studenter[r][c+3][4:]
                yngst_mnd_bach = studenter[r][c+3][2:4]
                yngst_dag_bach = studenter[r][c+3][:2]
            
            if dato_eldst < eldst_bach:
                eldst_bach = dato_eldst
                eldst_studnr_bach = studenter[r][c-1]
                eldst_fornavn_bach = studenter[r][c]
                eldst_etternavn_bach = studenter[r][c+1]
                eldst_aar_bach = studenter[r][c+3][4:]
                eldst_mnd_bach = studenter[r][c+3][2:4]
                eldst_dag_bach = studenter[r][c+3][:2]

        if studenter[r][c+5] == 'Årsstudium IT og IS':
        
            if dato_yngst > yngst_aars:
                yngst_aars = dato_yngst
                yngst_studnr_aars = studenter[r][c-1]
                yngst_fornavn_aars = studenter[r][c]
                yngst_etternavn_aars = studenter[r][c+1]
                yngst_aar_aars = studenter[r][c+3][4:]
                yngst_mnd_aars = studenter[r][c+3][2:4]
                yngst_dag_aars = studenter[r][c+3][:2]
            
            if dato_eldst < eldst_aars:
                eldst_aars = dato_eldst
                eldst_studnr_aars = studenter[r][c-1]
                eldst_fornavn_aars = studenter[r][c]
                eldst_etternavn_aars = studenter[r][c+1]
                eldst_aar_aars = studenter[r][c+3][4:]
                eldst_mnd_aars = studenter[r][c+3][2:4]
                eldst_dag_aars = studenter[r][c+3][:2]
    
   
    print('Bach IT og IS: ')
    print(eldst_studnr_bach, eldst_fornavn_bach, eldst_etternavn_bach, ', med fødselsdato: ', eldst_dag_bach, eldst_mnd_bach, eldst_aar_bach, 'er eldst')
    print(yngst_studnr_bach, yngst_fornavn_bach, yngst_etternavn_bach, ', med fødselsdato: ', yngst_dag_bach, yngst_mnd_bach, yngst_aar_bach, 'er yngst')
    print()
    print('Årsstudium IT og IS: ')
    print(eldst_studnr_aars, eldst_fornavn_aars, eldst_etternavn_aars, ', med fødselsdato: ', eldst_dag_aars, eldst_mnd_aars, eldst_aar_aars, 'er eldst')
    print(yngst_studnr_aars, yngst_fornavn_aars, yngst_etternavn_aars, ', med fødselsdato: ', yngst_dag_aars, yngst_mnd_aars, yngst_aar_aars, 'er yngst')

    print()
    nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
    if nytt_valg == '':
        ferdig = False
def funk18(studenter, rad):

        y=1
        bytte = True
        while bytte:
            bytte = False
            for r in range(0, len(studenter) -y, 1):
                if studenter[r][2] > studenter[r+1][2]:
                    bytte = True
                    midlertidig = studenter[r]
                    studenter[r] = studenter[r+1]
                    studenter[r+1] = midlertidig
            y += 1

        print('Bach IT og IS: ')
        print()
        for elev in studenter:
            if elev[6] == 'Bach IT og IS':
                print(' - ', elev[0], elev[2], elev[1])
        print()
        print('Årsstudium IT og IS: ')
        print()
        for elev in studenter:
            if elev[6] == 'Årsstudium IT og IS':
                print(' - ', elev[0], elev[2], elev[1])
        print()
        nytt_valg = input('Trykk enter for å gå tilbake til hovedmeny')
        if nytt_valg == '':
            ferdig = False
        
    
main()
    


        
        
        
        
        
        
    
    
        
