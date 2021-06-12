# US - Exercício do capítulo 4

- **Iniciar programa**
    - [x]  Quando o programa estiver executando crie uma lista de arquivos do diretório corrente que tem a extensão .lst
    - [x]  Filtrar aqueles que possuem a extensão .lst
- **Caso não haja arquivos arquivos que combinem:**
    - [x]  O programa deverá solicitar ao usuário a entrar com um nome de arquivo - adicionando a extensão .lst, se não for digitada
- **Caso existam arquivos**
    - [x]  Devem ser impressos como listas numeradas começando com 1
    - [x]  O usuário deverá ser solicitado a entrar com o número do arquivo que ele quer carregar ou 0

        **Se 0:**

        - [x]  O usuário será solicitado a dar um nome de arquivo para um novo arquivo

        **Se diferente de 0:**

        **Se o arquivo estiver vazio:**

        - [x]  Mostrar mensagem: 'nenhum item está na lista'

        **Se o arquivo não for encontrado:**

        - [x]  Mensagem: "Número inválido"

        **Senão:**

        - [x]  Seus itens (itens do arquivo) devem ser todos lidos.
        - [x]  A lista deverá ser exibida com cada item númerado a partir do 1
        - [x]  Deverá aparecer as opções "Add",  "Delete","Save" (a menos que já tenha sido salvo) e "Quit"
- **Opções do usuário**
    - [x]  Add: adiciona um item no fim da lista, depois a lista é ordenada em ordem alfabética
    - [x]  Delete:  deleta um item em uma posição específicada e existente
    - [x]  Save: salva no arquivo os itens. Aparece somente, se existirem mudanças não salvas. Mostra na tela a quantidade de itens salvos no arquivo, mostrando seu nome.
    - [x]  Quit: fecha o programa.  Caso haja mudanças não salvas, deve ser oferecida mais uma chance para que elas sejam salvas.