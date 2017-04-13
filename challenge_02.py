# http://epublications.regis.edu/cgi/viewcontent.cgi?article=1511&context=theses
# 1. pulled out all the middle pieces
# 2. realized the cube likely has to be solved?
# 3. https://rubiks-cube-solver.com
# 4.

reds = {('2', '2'): 'N'}
blue = {('2', '2'): 'n'}
yell = {('2', '2'): 'W'}
gree = {('2', '2'): 'w'}
whit = {('2', '2'): 'E'}
oran = {('2', '2'): 'e'}

def main():
    text = """brbgboorrooyoobgwrorwrgbwrwoworogoorwrrorwbobgorrooobrowyborobworyrrbwogoor313223323223123212231213321113222222113232223232322332212232213132312322223231131233222131132332313332322323331331231231123322231233223233113332323333"""
    clr = text[0:75]
    row = text[75:150]
    col = text[150:]

    print(len(text), len(text)/3)
    print(clr)
    print(row)
    print(col)

    for item in zip(clr, row, col):
        colour, id = item[0], (item[1], item[2])

        if 'r' in colour:
            print(reds.get(id, '*'), end='')
        elif 'y' in colour:
            print(yell.get(id, '*'), end='')
        elif 'o' in colour:
            print(oran.get(id, '*'), end='')
        elif 'w' in colour:
            print(whit.get(id, '*'), end='')
        elif 'b' in colour:
            print(blue.get(id, '*'), end='')
        elif 'g' in colour:
            print(gree.get(id, '*'), end='')

if __name__ == '__main__':
    main()
