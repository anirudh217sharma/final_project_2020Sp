import random
from typing import Dict, List, Any, Union
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import math
import copy


def to_str(var):  # https://stackoverflow.com/questions/24914735/convert-numpy-list-or-float-to-string-in-python
    """
    :param var: input -decimal number
    :return:
     Converted integer
     >>> to_str(52.09566843846285)
    '52'
    >>> to_str(29.537659592948213)
    '29'
    """
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1].split('.')[0]


def distance(x1, y1, x2, y2):
    """
    :param x1: First person's x coordinate
    :param y1: First person's y coordinate
    :param x2: Second person's x coordinate
    :param y2: Second person's y coordinate
    :param d: Distance under which a person will become infected
    :return: A Boolean
    >>> distance(1,1,2,2)
    True
    >>> distance(1,1,8,9)
    False
    """
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return abs(distance) <= 6


final_dict = {}


def death_recovery_calculator(final_dict):
    """
    :param final_dict: Total infected population after two months

    return: simulation_death_record - a dictionary containing the death information for various age groups

    """
    final_dict['death_rate'] = []
    final_dict['age_group'] = []
    final_dict['count'] = []
    for num in final_dict['age']:
        if num <= 29:
            final_dict['death_rate'].append(0.2)
            final_dict['age_group'].append('less_then_29')
        elif 30 <= num <= 39:
            final_dict['death_rate'].append(0.4)
            final_dict['age_group'].append('between 30 and 39')
        elif 40 <= num <= 49:
            final_dict['death_rate'].append(0.6)
            final_dict['age_group'].append('between 40 and 49')
        elif 50 <= num <= 59:
            final_dict['death_rate'].append(1.4)
            final_dict['age_group'].append('between 50 and 59')
        elif 60 <= num <= 69:
            final_dict['death_rate'].append(3.6)
            final_dict['age_group'].append('between 60 and 69')
        elif 70 <= num <= 79:
            final_dict['death_rate'].append(8.0)
            final_dict['age_group'].append('between 70 and 79')
        else:
            final_dict['death_rate'].append(15.0)
            final_dict['age_group'].append('greater than 80')
    final_dict['count'] = [1] * len(final_dict['age'])
    infected_population = pd.DataFrame(final_dict)
    infected_population['death_number'] = infected_population['death_rate'] / 100
    simulation_death_record = dict(infected_population.groupby(['age_group']).sum()['death_number'])
    return simulation_death_record


def no_social_distancing(infected_percentage, final_dict, test_set):
    """
    :param infected_percentage: List to store precentage of infected people each day
    :param final_dict: Dictionary to store information about infected people
    :param test_set : Dictionary representing the population

    :return: infected_percentage,final_dict

    """

    a = 0
    b = 1
    c = 0
    delta = 0
    while a < 15:
        for m in range(4):
            counter = []
            for i, num in enumerate(test_set['condition']):
                if num == 'I':
                    for j, k in enumerate(test_set['xy']):
                        try:
                            if distance(k[0], k[1], test_set['xy'][i][0], test_set['xy'][i][1]) and i != j:
                                final_dict['age'].append(test_set['age'][j])
                                final_dict['condition'].append('I')
                                final_dict['xy'].append(k)
                                test_set['condition'][j] == 'I'
                                counter.append(j)
                            else:
                                continue
                        except:
                            continue
            test_set['x'] = [random.randint(1, 150) for i in range(len(test_set['condition']))]
            test_set['y'] = [random.randint(1, 150) for i in range(len(test_set['condition']))]
            test_set['xy'] = list(zip(test_set['x'], test_set['y']))
            del test_set['x']
            del test_set['y']
            b += 1
            infected_percentage['number'].append(((len(counter) + delta) / 1000) * 100)
            infected_percentage['day'].append(b)
            #         print(len(test_set['age']))
            delta += len(counter)
            #             print(delta)
            #         print(len(counter))
            try:
                for thi in counter:
                    test_set['age'].pop(thi)
                    test_set['condition'].pop(thi)
                    test_set['xy'].pop(thi)
                    test_set['delta'].pop(thi)
            except:
                continue
        #         print(len(test_set['age']))
        a += 1
    return infected_percentage, final_dict


def social_distancing(infected_percentage_social_distancing, final_dict_sd, test_set_sd):
    """
    :param infected_percentage: List to store precentage of infected people each day
    :param final_dict: Dictionary to store information about infected people
    :param test_set : Dictionary representing the population

    :return: infected_percentage_social_distancing,final_dict_sd

    """

    a = 0
    b = 1
    c = 0
    delta = 0
    while a < 15:
        for m in range(4):
            counter = []
            for i, num in enumerate(test_set_sd['condition']):
                if num == 'I':
                    for j, k in enumerate(test_set_sd['xy']):
                        try:
                            if distance(k[0], k[1], test_set_sd['xy'][i][0], test_set_sd['xy'][i][1]) and i != j:
                                final_dict_sd['age'].append(test_set_sd['age'][j])
                                final_dict_sd['condition'].append('I')
                                final_dict_sd['xy'].append(k)
                                test_set_sd['condition'][j] == 'I'
                                counter.append(j)
                            else:
                                continue
                        except:
                            continue
            b += 1
            infected_percentage_social_distancing['number'].append(((len(counter) + delta) / 1000) * 100)
            infected_percentage_social_distancing['day'].append(b)
            #         print(len(test_set_sd['age']))
            delta += len(counter)
            #         print(delta)
            try:
                for thi in counter:
                    test_set_sd['age'].pop(thi)
                    test_set_sd['condition'].pop(thi)
                    test_set_sd['xy'].pop(thi)
                    test_set_sd['delta'].pop(thi)
            except:
                continue

        #         print(len(test_set_sd['age']))
        test_set_sd['x'] = [random.randint(1, 150) for i in range(len(test_set_sd['condition']))]
        test_set_sd['y'] = [random.randint(1, 150) for i in range(len(test_set_sd['condition']))]
        test_set_sd['xy'] = list(zip(test_set_sd['x'], test_set_sd['y']))
        del test_set_sd['x']
        del test_set_sd['y']
        a += 1
    #     print(a)
    return infected_percentage_social_distancing, final_dict_sd


if __name__ == "__main__":
    import doctest

    doctest.testmod()
