Zero = ['  ***  ',
        ' *   * ',
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  '
        ]
One = ['   *  ',
       '  **  ',
       '   *  ',
       '   *  ',
       '   *  ',
       '   *  ',
       '  *** ']
Two = ['  ***  ',
       '*     *',
       '*    * ',
       '   *   ',
       '  *    ',
       '*      ',
       '*******'
        ]
Three = ['  ***  ',
         ' *    *',
         '      *',
         '   *** ',
         '      *',
         ' *    *',
         '  ***  '
         ]
Four = ['   *  ',
        '  **  ',
        ' * *  ',
        '*  *  ',
        '******',
        '   *  ',
        '   *  ']
Five = ['*******',
        '*     ',
        '*     ',
        '****** ',
        '      *',
        '      *',
        '****** ']
Six = [' ***  ',
       '*     ',
       '*     ',
       '****  ',
       '*    *',
       '*    *',
       ' ***  ']
Seven = ['  *****',
         '      *',
         '     * ',
         '   *   ',
         '  *    ',
         '*      ',
         '*      ']
Eight = ['  ***  ',
         '*     *',
         '*     *',
         '  ***  ',
         '*     *',
         '*     *',
         '  ***  ']
Nine = ['   ****',
        ' *    *',
        ' *    *',
        '   ****',
        '      *',
        '      *',
        '      *']

digitlist = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]


inputDigits = str(input('Digite os números de 0 à 9: ')).strip()

# um digito é composto por 7 linhas (rows)
for row in range(7):
    line = ""
    for column in range(len(inputDigits)):
       #  pega o n número da string, que é o input
       number = int(inputDigits[column])
        # pega o digito da lista de digitos de acordo com o número do input
       digit = digitlist[number]
       # pega uma parte do digito e substitui a string de '*' pelo número atual do input
       line += digit[row].replace('*', f'{number}') + "     "
    print(line)



