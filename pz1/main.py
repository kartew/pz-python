def say():
    first_name = input('Введите Ваше имя: ')
    last_name = input('Введите Вашу фамилию: ')
    otchestvo = input('Введите Ваше отчество: ')
    return first_name, last_name, otchestvo


def work():
    positions = []
    for i in range(3):
        position = input(f'Введите должность #{i + 1}: ')
        if position in ('0', 'return'):
            break
        else:
            positions.append(position)
    return positions


def experience_skill():
    exp_dict = {}
    i = 1
    while True:
        experience = input(f'Введите Ваш опыт #{i}: ')
        if experience in ('0', 'return'):
            break
        else:
            exp_dict[f'Exp{i}'] = experience
        i += 1

    skill_dict = {}
    i = 1
    while True:
        skill = input(f'Введите Вашу способность #{i}: ')
        if skill in ('0', 'return'):
            break
        else:
            skill_dict[f'Skill_{i}'] = skill
        i += 1
    return exp_dict, skill_dict


def cv():
    year = input('Введите Ваш год рождения: ')
    education = input('Введите Ваше образование: ')
    hobby = input('Введите Ваше хобби: ')
    salary = input('Введите Вашу заработную плату: ')
    global city

    first_name, last_name, otchestvo = say()
    positions = work()
    exp_dict, skill_dict = experience_skill()

    cv = "Ваше резюме:\n"
    cv += f'Ваше ФИО: {first_name} {last_name} {otchestvo}\n'
    cv += 'Ваши должности:\n'
    j = 1
    for i in positions:
        cv += f'{j}. {i}\n'
        j += 1
    j = 1
    cv += 'Ваш опыт:\n'
    for key, value in exp_dict.items():
        cv += f'{j}. {key} : {value}\n'
        j += 1
    j = 1
    cv += 'Ваши способности:\n'
    for key, value in skill_dict.items():
        cv += f'{j}. {key} : {value}\n'
        j += 1
    cv += 'Общая информация:\n'
    cv += f'1. Год рождения: {year}\n'
    cv += f'2. Образование: {education}\n'
    cv += f'3. Хобби: {hobby}\n'
    cv += f'4. Заработная плата: {salary}\n'
    cv += f'5. Город: {city}\n'

    return cv


def slice_cv():
    first_name, last_name, otchestvo = say()
    year = input('Введите Ваш год рождения: ')
    city = input('Введит Ваш город проживания: ')

    return f'{last_name} {first_name[0]}.{otchestvo[0]}. {year}, {city}.'


def formula(n):
    def fac(num):
        if num == 0:
            return 1
        return fac(num - 1) * num

    x = n
    y = n + 2
    st1 = (1 + x) ** y
    st2 = (y * x) / fac(1)
    st3 = (y * (y - 1) * x * x) / fac(2)
    st4 = ((1 + 4 * (x / y)) / (20 * y)) ** 0.5

    return st1 + st2 + st3 + st4


city = 'Харьков'


def _main():
    # first_name, last_name, otchestvo = say()
    # print(f'Ваше ФИО: {first_name} {last_name} {otchestvo}')

    # positions = work()
    # print('Ваши должности: ', end='')
    # print(*positions, sep=', ')

    # exp_dict, skill_dict = experience_skill()
    # print('Ваш опыт:')
    # for key, value in exp_dict.items():
    #     print(key, ' : ', value)
    # print('Ваши способности:')
    # for key, value in skill_dict.items():
    #     print(key, ' : ', value)

    # my_cv = cv()
    # print(my_cv)

    # my_slice = slice_cv()
    # print(my_slice)

    my_result = formula(2)
    print(my_result)


if __name__ == '__main__':
    _main()
