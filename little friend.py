
#nome
print('''
██╗░░░░░██╗████████╗████████╗██╗░░░░░███████╗  
██║░░░░░██║╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝  
██║░░░░░██║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░  
██║░░░░░██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░  
███████╗██║░░░██║░░░░░░██║░░░███████╗███████╗  
╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝  

███████╗██████╗░██╗███████╗███╗░░██╗██████╗░
██╔════╝██╔══██╗██║██╔════╝████╗░██║██╔══██╗
█████╗░░██████╔╝██║█████╗░░██╔██╗██║██║░░██║
██╔══╝░░██╔══██╗██║██╔══╝░░██║╚████║██║░░██║
██║░░░░░██║░░██║██║███████╗██║░╚███║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░''')
print('')
 #banner
print('''███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██                     █▀▀▄ █──█ ▄ 　 ░█▀▀▀█ ░█─── ─█▀▀█ ░█──░█ ░█▀▀▀ ░█▀▀█ 
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██                     █▀▀▄ █▄▄█ ─ 　 ─▀▀▀▄▄ ░█─── ░█▄▄█ ░█▄▄▄█ ░█▀▀▀ ░█▄▄▀ 
████▄─┘██▌░░░░░░░▐██└─▄████                     ▀▀▀─ ▄▄▄█ ▀ 　 ░█▄▄▄█ ░█▄▄█ ░█─░█ ──░█── ░█▄▄▄ ░█─░█
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
''')
print('')
#aviso
print('''
░█████╗░██╗░░░██╗██╗░██████╗░█████╗░██╗
██╔══██╗██║░░░██║██║██╔════╝██╔══██╗██║
███████║╚██╗░██╔╝██║╚█████╗░██║░░██║██║
██╔══██║░╚████╔╝░██║░╚═══██╗██║░░██║╚═╝
██║░░██║░░╚██╔╝░░██║██████╔╝╚█████╔╝██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░░╚════╝░╚═╝''')
print('')
print('''os comandos 1,2 & 3 estao em desenvolvimento, os outros sao execuatos pelo menu, voce pode usar todos, mas nao dentro do menu.''')
print('')
print('')
escolha = -1

#escolhas

while escolha < 1 or escolha > 4:
    escolha = int(input("""O que você deseja fazer?
[ 1 ] = DoS (by: palahsu)
[ 2 ] = sqlmap
[ 3 ] = brutalforce
[ 4 ] = rapidscan
Sua escolha: """))
    print(''' ''')
    print('')
    print('')
    
# escolha

if escolha == 1:
    exec(open('DDOS1.py', encoding="utf-8").read(), globals())
    

elif escolha == 2:
    exec(open('SQLI.py', encoding="utf-8").read(), globals())

elif escolha == 3:
    exec(open('brute.py', encoding="utf-8").read(), globals())

elif escolha == 4:
    exec(open('RPD1.py', encoding="utf-8").read(), globals())

    
else:
    print('''
█▀▀█ ▀▀█▀▀ █▀▀ 　 █▀▄▀█ █▀▀█ ░▀░ █▀▀ 　 ▄ ▀▄ 
█▄▄█ ░░█░░ █▀▀ 　 █░▀░█ █▄▄█ ▀█▀ ▀▀█ 　 ░ ░█ 
▀░░▀ ░░▀░░ ▀▀▀ 　 ▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀ ▄▀''')

#opa dev q ta usando o meu script, me da uma nota la pelo insta: @slayerkkk_
#sou iniciante ainda, me fale oq posso melhorar! :)