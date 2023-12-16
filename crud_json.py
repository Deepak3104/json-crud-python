'''
Created on 
   16th Feb 2022
Course work: 
@author: Elakia 
Source:
    https://datagy.io/python-delete-dictionary-key/

    https://datatofish.com/measure-time-to-run-python-script/

    https://faker.readthedocs.io/en/master/index.html
'''

# Import necessary modules
import json
from pprint import pprint
import time
from faker import Faker

fake = Faker()
 
FILEPATH = 'city.json'

def get_json_data():

    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    return data

def store_json_data(data):

    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)

# CRUD: CREATE
def add_city(city, state):

    current_data = {
        "name"  : city,
        "state" : state
    }

    data = get_json_data() 
        
    # print(data)

    data[city] = current_data
    store_json_data(data)

# CRUD: CREATE data with population
def add_city(city, state, population):
    data = get_json_data() 

    # index = len(data) + 1 

    current_data = {
        "name"  : city,
        "state" : state,
        "population" : population
    }
        
    # print(data)

    data[city] = current_data
    store_json_data(data)


# CRUD: READ All
def get_all_cities():

    data = get_json_data() 

    # print(data)
    return data


# CRUD: READ Single
def get_single_city(city_name):

    data = get_json_data() 

    if(city_name in data):
        return data[city_name]

    # print(data)
    return None


def update_single_city_with_population(city_name, city_state, city_population):

    data = get_json_data() 

    if(city_name in data):
        city_data = {
            'name' : city_name,
            'state' : city_state,
            'population' : city_population
        }
        data[city_name] = city_data

        store_json_data(data)

def update_single_city(city_name, city_state):

    data = get_json_data() 

    if(city_name in data):
        city_data = {
            'name' : city_name,
            'state' : city_state,
        }
        data[city_name] = city_data

        store_json_data(data)

def delete_single_city(city_name):

    data = get_json_data() 

    if(city_name in data):
        data.pop(city_name)

        store_json_data(data)

def delete_population_single_city(city_name):

    data = get_json_data() 

    if city_name in data:
        del data[city_name]["population"]

        store_json_data(data)

def delete_all_cities():

    # get all keys and pop each
    data = get_json_data() 

    city_list = list(data.keys())

    for current_city in city_list:
        print(current_city)

        data.pop(current_city)

    store_json_data(data)   

def delete_all_cities_efficient():

    current_dict = {}

    store_json_data(current_dict)

def add_multiple_cities_test():

    Faker.seed(0)
    for c_index in range(10):
        current_city = fake.city()
        current_state = fake.state()

        # print(current_city, current_state)

        add_city(current_city, current_state)

        print(f'{c_index} Added: ', current_city, current_state)

def startpy():
    
    # print("CRUD started!")

    #CRUD: Add City

    # city    = "Namakkal"
    # state   = "Tamilnadu"
    # add_city(city, state)
    # print('city data added successfully')



    # CRUD: Add City with population

    # city    = "chennai"
    # state   = "Tamilnadu"
    # population = "11,776,147"
    # add_city(city, state, population)
    # print('city data with population added successfully')


    # # CRUD: READ all
    # cities = get_all_cities()
    # pprint(cities)

    # CRUD: READ single
    # city_name = 'Namakkal'
    # single_city = get_single_city(city_name)
    # print(single_city)

    # CRUD: UPDATE
    # city_name = 'Changchester'
    # city_state = 'Arizona'
    # update_single_city(city_name, city_state)
    # print('city data updated successfully')
    
    # CRUD: UPDATE_with_population

    # city_name = 'Changchester'
    # city_state = 'Arizona'
    # city_population = '1,834,270'
    # update_single_city_with_population(city_name, city_state, city_population)
    # print('city data updated successfully')

    # CRUD: DELETE Single
    # city_name = 'Montreal'
    # delete_single_city(city_name)
    # print('city data deleted successfully')

    # CRUD: DELETE population for specified city
    city_name = 'Namakkal'
    delete_population_single_city(city_name)
    print('population for city name deleted successfully')

    # CRUD: DELETE All
    # start_time = time.time()
    # delete_all_cities()
    # executionTime = (time.time() - start_time)
    # print('[delete_all_cities]Execution time in seconds: ' + str(executionTime))

    # # # CRUD: DELETE All Efficient
    # start_time = time.time()
    # delete_all_cities_efficient()
    # executionTime = (time.time() - start_time)
    # print('[delete_all_cities_efficient]Execution time in seconds: ' + str(executionTime))

    # # CRUD: Add multiple cities
    # add_multiple_cities_test()

    # print('\nCRUD Done!')

if __name__ == '__main__':
    startpy()