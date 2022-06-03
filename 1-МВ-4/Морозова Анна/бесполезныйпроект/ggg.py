import os
import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse')
parser.add_argument('-n', '--name', nargs='?', default='Solnyshko', help="Here's your name")
parser.add_argument('-p', '--path', help="Here's the path to your file")
parser.add_argument('-nQ', '--noQ', action="store_true", help="No more questions, mate")
parser.add_argument('-cF', '--crFile', action="store_true", help="Do u want to create file? ")
args = parser.parse_args()
# --------------------------------------------------------------------------------
def createfile():
    quest = input(f'\n{args.name}, вы хотите создать этот файл?\n').capitalize()
    if quest[0] == 'Y':
        name = input("введите что-нибудь\n")
        with open(args.path, "w+") as f:
            f.write(name)
    else:
        print('Посмотрите!')
# --------------------------------------------------------------------------------
def removefile ():
    ag = input(f'\n{args.name}, вы хотите удалить этот файл??\n').capitalize()
    if ag[0] == 'Y':
        os.remove(args.path)
    else:
        print('Ок, я ничего не сделаю')
# --------------------------------------------------------------------------------

print(f'Привет, {args.name}!')
print(args)

if os.path.exists(args.path):
    print("Этот файл существует.\n")
else:
    if args.crFile:
        name = input("Введите что-нибудь\n")
        with open(args.path, "w+") as f:
            f.write(name)
    else:
        createfile()

if os.path.exists(args.path):
    if args.noQ:
        os.remove(args.path)
        exit(0)
    else:
        removefile()
else:
    print("\n Извините, но этого файла не существует, проверьте команду.")
