import os
import argparse



parser = argparse.ArgumentParser(description='Удаление файла')
parser.add_argument('-n', '--name', default='Anon', help='Имя пользователя')
parser.add_argument('-p', '--path', help='Путь файла')
parser.add_argument('-nQ', '--noQ', action='store_true', help='Давай без вопросов')
args = parser.parse_args()
print(f'Привет, {args.name}!')
print(args)

if os.path.exists(args.path):
    if args.noQ:
        os.remove(args.path)
        exit(0)
    else:
        ag = input(f'\n{args.name}, вы хотите удалить этот файл?? Y/N ').capitalize()
        if ag[0] == 'Y':
            os.remove(args.path)
        else:
            print('Ок, не буду трогать его.')
else:
    print("\n Извините, но этого файла не существует, проверьте команду.")