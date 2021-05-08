
def terulet():
    terulet: int = 0
    print('=====================================================')
    print('Területszámítás')
    print('Melyik síkidommal akarja végrehajtani a számítást?')
    print('1. Négyzet')
    print('2. Téglalap')
    valasztott: int = 0
    while valasztott <= 0 or valasztott > 2:
        print('')
        valasztott: int = int(input('Írd le mit választottál: '))
        if valasztott <= 0:
            print('')
            print('Az adat nem megfelelő.')
            continue
        if valasztott > 2:
            print('')
            print('Az adat nem megfelelő.')
            continue
    print('')
    print('=====================================================')

    if valasztott == 1:
        print('')
        print('Négyzet területszámítása')
        a: int = 0
        while a <= 0:
            print('')
            a: int = int(input('Írd le a négyzet oldalát cm-ben: '))
            if a <= 0:
                print('')
                print('Az adat nem megfelelő a számoláshoz.')
                continue
            terulet = a * a
            print('')
            print(f'A négyzet területe: {terulet}cm2 ')
            print('')

    if valasztott == 2:
        print('')
        print('Téglalap területszámítás')
        print('')
        a: int = 0
        b: int = 0
        while a <= 0 or b <= 0:
            a: int = int(input('Írd le a téglalap a oldalát: '))
            if a <= 0:
                print('Az a adat nem megfelelő a számoláshoz.')
                continue
            b: int = int(input('Írd le a téglalap b oldalát: '))
            if b <= 0:
                print('A b adat nem megfelelő a számoláshoz.')
                continue
        terulet = a * b
        print('')
        print(f'A téglalap területe: {terulet}cm2')
        print('=====================================================')


def main():
    terulet()


if __name__ == "__main__":
    main()
