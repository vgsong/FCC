import re
import operator


def arithmetic_arranger(lista, show_result=False):
    def find_greater(x, y):
        # return the largest len count between x and y
        if len(x) > len(y):
            return len(x) + 2
        else:
            return len(y) + 2

    def sign_pos(mstr, pattern):
        return re.search(pattern, mstr).start()

    if len(lista) > 5:
        return 'Error: Too many problems.'

    elif any(re.search(r'[\*\/]', x) for x in lista):
        return "Error: Operator must be '+' or '-'."

    elif any(re.search(r'\d{5}', x) for x in lista):
        return 'Error: Numbers cannot be more than four digits.'

    elif any(re.search(r'[A-za-z]', x) for x in lista):
        return 'Error: Numbers must only contain digits.'

    ops = {"+": operator.add, "-": operator.sub}

    top_lista = []
    sign_lista = []
    bot_lista = []

    bar_lista = []
    result_lista = []
    format_top = []
    format_bot = []

    arranged_problems = []

    # obtain data
    for x in range(len(lista)):
        tempos = sign_pos(lista[x], "[\+\-]")
        top_lista.append(lista[x][:tempos - 1])
        sign_lista.append(lista[x][tempos])
        bot_lista.append(lista[x][tempos + 2:])

        # change to final formatting
        main_len = find_greater(top_lista[x], bot_lista[x])
        format_top.append(top_lista[x].rjust(main_len))
        format_bot.append(sign_lista[x] + bot_lista[x].rjust(main_len - 1))
        bar_lista.append(''.rjust(len(format_bot[x]), '-'))
        result_lista.append(str(ops[sign_lista[x]](int(top_lista[x]), int(bot_lista[x]))).rjust(main_len))

    arranged_problems = '    '.join(format_top)
    arranged_problems = arranged_problems + ''.join('\n')
    arranged_problems = arranged_problems + '    '.join(format_bot)
    arranged_problems = arranged_problems + ''.join('\n')
    arranged_problems = arranged_problems + '    '.join(bar_lista)

    if show_result == True:
        arranged_problems = arranged_problems + ''.join('\n')
        arranged_problems = arranged_problems + '    '.join(result_lista)

    return arranged_problems
