Zero = ['  ***  ',
        ' *   * ',
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
       '  *** ']

Two = ['  ***   ',
        '*    * ',
        '*   *  ',
        '   *   ',
        '  *    ',
        '  *****'
        ]

Three = ['**** ',
        '     *',
        '     *',
        '  ****',
        '     *',
        '     *',
        '***** ']

Four = ['   *  ',
        '  **  ',
        ' * *  ',
        '*  *  ',
        '******',
        '   *  ',
        '   *  ']

Five = ['******',
        '*     ',
        '*     ',
        '******',
        '     *',
        '     *',
        '******']

Six = [' ***  ',
       '*     ',
       '*     ',
       '****  ',
       '*    *',
       '*    *',
       ' ***  ']

Seven = [' *****',
         '     *',
         '    * ',
         '   *   ',
         ' *    ',
         '*     ',
         '*     ']

Eight = ['  *** ',
         '*     *',
         '*     *',
         '  ***  ',
         '*     *',
         '*     *',
         '  ***  ']

Nine = ['  ****',
        '*    *',
        '*    *',
        '  ****',
        '     *',
        '     *',
        '     *']

numlist = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]


def bigdigits(num):
    global numlist
    for c in num:
        for i in numlist[int(c)]:
            print(i.replace('*', f'{int(c)}'))


n = str(input('Digite os números de 0 à 9: ')).strip()
bigdigits(n)

