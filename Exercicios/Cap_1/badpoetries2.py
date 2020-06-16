
def poetrygenerate(l=5):
    import random

    artigos = ['o', 'a', 'um', 'uns', 'umas', 'uma']
    sujeitos = ['gato', 'cão', 'homem', 'mulher', 'bode', 'coelho']
    verbos = ['amar', 'caminhar', 'trocar', 'morrer', 'cair', 'andar']
    adverbios = ['silenciosamente', 'bem', 'mal', 'vagarosamente', 'temerariamente', 'pesarosamente']

    for _ in range(l):
         print(f'{artigos[random.randint(0, 5)]}', end=' ')
         print(f'{sujeitos[random.randint(0, 5)]}', end=' ')
         print(f'{verbos[random.randint(0, 5)]}', end=' ')
         print(f'{adverbios[random.randint(0, 5)]}')


n = int(input('Digite a quantidade de linhas entre 1 e 10: '))
poetrygenerate(n)
