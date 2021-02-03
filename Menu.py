from ManageFiles import ManageFiles


class Menu:
    m = ManageFiles()
    previous = []

    while True:
        print('+----------  Menu  -----------+')
        print('|   1. Search                 |')
        print('|   2. Show search history    |')
        print('|   3. Exit                   |')
        print('+-- --- --- --- --- --- --- --+')
        choice = input('\nSelect: ')
        if choice == '1':
            search = input('Enter your search: ')
            previous.append(search)
            search_url = search.replace(' ', '+')
            print()
            if len(previous) > 5:
                previous.pop(0)
            m.search(search_url)
        elif choice == '2':
            if len(previous) > 0:
                m.prev_results(previous)
            else:
                print('No previous searches has been found')
                input('Press Enter to continue')
        elif choice == '3':
            print('---- Exiting ----')
            break
        else:
            input('Wrong input, press Enter and try again')
