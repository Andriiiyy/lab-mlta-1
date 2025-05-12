import utils.adj_matrix_test
import  utils.adj_list_test
import utils.inc_matrix_test
import  utils.inc_list_test
import os

def main():
    os.system("cls")
    print('Виберіть спосіб задання графа для роботи')
    print('1. Матриця суміжності \n'
          '2. Список суміжності\n'
          '3. Матриця інцидентності\n'
          '4. Список ребер\n')
    method: int = int(input("введіть число: "))
    os.system("cls")

    print('Виберіть тип матриці')
    print('1. Направлена \n'
          '2. Не направлена\n')

    mtype: int = int(input("введіть число: "))
    os.system("cls")

    glist = ['adj_matrix', 'adj_list', 'inc_matrix', 'inc_list']
    dlist = ['directed', 'undirected']

    exec_string = f'utils.{glist[method - 1]}_test.{dlist[mtype - 1]}()'
    exec(exec_string)
    input("Натисніть будь-яку клавішу, щоб продовжити...")
    main()

if __name__ == '__main__':
    main()
