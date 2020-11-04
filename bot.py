import random
import tweepy
import time

#config

CONSUMER_KEY = 'm30H4enVRMBYXTri4Ewc9umHV'
CONSUMER_SECRET = 'ecySdT65iFLsxwrfuG2FbuANsjAFsm7rvBE6JdU6npGobKdgx6'
ACCESS_KEY = '1304773355837456384-UWwHIzMBU4wocXCnclzxFOanpDM7pa'
ACCESS_SECRET = 'bzZDYPkmaZZlQRri1uWormMmrrhVJ0qhr4c2HLAFPHTeQ'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#lists
lista_triste = ['Já te falaram que vai ficar tudo bem? <3 Tudo passa algum dia, até o que parece que não vai, acredita em mim! :)', ' Pra que desanimar e ficar triste, se isso só piora? Perdoe, saiba que todo mundo erra, até você! Errar uma vez, ou duas, não significa que você vai sempre errar :)',' A tristeza é mais uma armadilha usada para te afastar de tudo que você pode conseguir. É quando você está triste que você deve mostrar a sua força e seguir em frente! ;)', ' Por mais que você esteja triste, lembre dos momentos bons que você já teve, a vida é mais alegria do que tristeza! Os momentos ruins vêm para lembrar que não somos invencíveis e que temos que valorizar ainda mais a nossa vida! :)' , ' Eu confesso que não tenho momentos tristes e muito menos felizes, porque afinal eu sou um bot né?! Mas espero que você melhore logo :3',' A felicidade está nas simples coisas do dia a dia! Uma visita, ou uma ligação para um amigo, ou para alguém que precisa de ajuda, pode parecer simples demais, mas ajuda vocês dois! :)', ' Às vezes a gente complica demais a vida, exigimos muito dela e de nós mesmos. Deixe as preocupações de lado e vá viver com quem te ama! <3', ' Ajudar as pessoas é um dos melhores remédios contra a tristeza. Ver que você está ajudando e sendo útil é melhor que ganhar um presente! Às vezes até quem parece bem, precisa de ajuda.' , ' A internet está cheia de pessoas que só sabem comentar sobre coisas negativas. Às vezes é preciso desconectar para conectar de novo ;)']




lista_cansado = [' Pensa que tudo vai valer a pena lá na frente! Se você ir trabalhando de pouco em pouco, algum dia você chega lá, você só precisa se esforçar! :)',' Trabalhar não precisa ser cansativo. Por que você não coloca uma música, ou um podcast que você gosta para te incentivar a continuar trabalhando? Espero que você termine logo! :)', ' A sensação de dever cumprido é muito boa! Acho melhor você terminar tudo que tem pra fazer agora e ficar livre depois hehe : < ) ', ' Como sou um robô, faço meu trabalho de uma forma muito automática, queria sentir preguiça alguma vez na vida :( Mesmo assim, desejo que você termine logo o que tem pra fazer ;)', ' Trabalhar é ser útil! Pode ser cansativo às vezes, mas tudo na sociedade depende do trabalho. O trabalho de formiguinha que você faz, vai trazer resultados lá na frente!  ;)' ]






lista_vazio = [' Cuidado com o tipo de coisa que você consome! Será que isso faz bem pra você? Tente consumir coisas positivas e que te deixam mais feliz :)', ' A internet está cheia de pessoas que só sabem comentar sobre coisas negativas. Às vezes é bom desconectar para conectar de novo ;)', ' Será que você não está focando em coisas que não são tão importantes na vida? O dinheiro, o trabalho e o estudo são importantes na vida, mas lembre-se que essas coisas não substituem outras. Existem coisas mais importantes, como seus amigos e família! :)', ' Você não precisa de nada ou de ninguém para ser feliz! A felicidade não está em coisas e nem em pessoas, mas sim, na forma como você vive.', ' Por que você não tenta conversar com sua família? Pode parecer bem bobo, mas a sua família vai te entender, independente do que você estiver passando, ela vai estar lá pra você. Ou, você pode conversar com algum amigo seu e pedir conselhos. Sempre ajuda! :)']





FILE = 'last_seen_id.txt'

def retrieve_last_seen_id(FILE):
    f_read = open(FILE,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, FILE):
    f_write = open(FILE, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():

    last_seen_id = retrieve_last_seen_id(FILE)

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode = 'extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id,FILE)
        if '#triste' in mention.full_text.lower():
            print('enviado')
            api.update_status('@' + mention.user.screen_name + random.choice(lista_triste), mention.id)
        if '#cansado' in mention.full_text.lower():
            print('enviado')
            api.update_status('@' + mention.user.screen_name + random.choice(lista_cansado), mention.id)
        if '#vazio' in mention.full_text.lower():
            print('enviado')
            api.update_status('@' + mention.user.screen_name + random.choice(lista_vazio), mention.id)


while True:
    reply_to_tweets()
    time.sleep(3)
