# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой

names = ['John', 'George', 'Virginia', 'Jane']
salary = [25000, 40000, 15000, 75000]
bonus = ['10.25%', '15.00%', '18.50%', '12.05%']


def salary_gen(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in bonus))}.items()


print(*(salary_gen(names, salary, bonus)))