file = open("pelda.txt", mode = 'w', encoding="UTF-8-sig" )
nev:str = input('Mi a neved? ')
file.write(f'Hello {nev}!\n')