import random

artigos = ['o', 'a', 'um', 'uns', 'umas', 'uma']
sujeitos = ['gato', 'cão', 'homem', 'mulher', 'bode', 'coelho']
verbos = ['amar', 'caminhar', 'trocar', 'morrer', 'cair', 'andar']
adverbios = ['silenciosamente', 'bem', 'mal', 'vagarosamente', 'temerariamente', 'pesarosamente']

for _ in range(5):
     print(f'{artigos[random.randint(0, 5)]}', end=' ')
     print(f'{sujeitos[random.randint(0, 5)]}', end=' ')
     print(f'{verbos[random.randint(0, 5)]}', end=' ')
     print(f'{adverbios[random.randint(0, 5)]}')

