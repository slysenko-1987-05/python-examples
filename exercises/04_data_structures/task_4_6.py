# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
d_keys = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
ospf = dict.fromkeys(d_keys)
list = ospf_route.split()
list[1] = list[1].replace('[','')
list[1] = list[1].replace(']','')
list[3] = list[3].replace(',','')                                                                                                                                      
list[4] = list[4].replace(',','')
ospf['Prefix'] = list[0] 
ospf['AD/Metric'] = list[1]
ospf['Next-Hop'] = list[3]
ospf['Last update'] = list[4]
ospf['Outbound Interface'] = list[5]
print(template.format(ospf['Prefix'], ospf['AD/Metric'], ospf['Next-Hop'], ospf['Last update'], ospf['Outbound Interface'])) 

