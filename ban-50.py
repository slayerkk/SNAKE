import smtplib
import email.message


#banner
print ('███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
print ('████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
print ('██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
print ('██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
print ('██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
print ('╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
print ('                                                     ')
print ('██████╗░░█████╗░███╗░░██╗')
print ('██╔══██╗██╔══██╗████╗░██║')
print ('██████╦╝███████║██╔██╗██║')
print ('██╔══██╗██╔══██║██║╚████║')
print ('██████╦╝██║░░██║██║░╚███║')
print ('╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝')
print ('')
#deluxe 
print (''' 
█▀▀▄ █▀▀ █░░ █  █ █░█ █▀▀ 
█░░█ █▀▀ █░░ █  █ ▄▀▄ █▀▀ 
▀▀▀░ ▀▀▀ ▀▀▀  ▀▀▀ ▀ ▀ ▀▀▀ ''')
print('')
#banner by
print ('█▀▀▄ █░░█ 　 █▀▀ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ ')
print ('█▀▀▄ █▄▄█ 　 ▀▀█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ ')
print ('▀▀▀░ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ ')


c = input('coloque o seu email:')
print('')
print (''' Ative a verificaçao de duas etapas, apos isso, ative a opçao senha de apps, crie uma senha para o seu email. Agora coloque a senha.''')

print ('')

d = input ('coloque a senha:')

print('')

print ('''tudo pronto, a senha pode ser usada apenas para usar o seu email. Este método e 100% seguro! ''')

print ('')
print('seu email: {}' .format (c))
print('sua senha de email: {}' .format (d))
print('')
a = input('coloque o numero q vc quer derrubar:')



#email
def enviar_email():
    corpo_email = f' Olá suporte do whatsapp, meu filho sofreu abuso deste numero {a} em seu app!!, muitas crianças vem recebendo nudes e pornografia deste numero!!, ja denunciamos mas nada funciona, infelizmente. tenho print para provar dos abusos que meu filho sofreu!, tem ate uma das fotos pornograficas que meu filho recebeu!, links: https://drive.google.com/file/d/1iJrqn_SkiLs5VmVnIWjnBhqAz5m1beyT/view?usp=sharing // https://drive.google.com/file/d/1wD_qS4y8NMDM0CL8XYv3EbYPxgTZJczq/view?usp=sharing, olhem as deunucias no numero do mesmo, meu filho esta passando por terapia por conta disto!!. Caso o numero nao seja banido, irei abrir um processo contra o whatsapp, pois as denuncias nao funcionam!!'
    
 
    msg = email.message.Message()
    msg['Subject'] = 'Olá suporte do whatsapp!'
    msg['From'] = f'{c}'
    msg['To'] = 'slayerandkr@gmail.com'
    password = f'{d}'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print ('o numero sera banido em breve.')
enviar_email()
#fecho email

#denuncia 
print ('''
█▀▄ █▀▀ █▄░█ █░█ █▄░█ █▀▀ █ █▀▀   █▀█   █▄░█ █░█ █▀▄▀█ █▀▀ █▀█ █▀█   █▀   █▀█ █ █   ▄█ █▀█   █ █ █▀▀ ▀█ █▀▀ █▀  
█▄▀ ██▄ █░▀█ █▄█ █░▀█ █▄▄ █ ██▄   █▄█   █░▀█ █▄█ █░▀░█ ██▄ █▀▄ █▄█   ▄█   █▄█ █▄█    █ █▄█   ▀▄▀ ██▄ █▄ ██▄ ▄█ ▄''')


print ('''
''')
print ('                              ')
#acabou :)
print('')
print('tchau :)')