'''
this file contains general functions for the application.
'''

def get_snow_day_policy():
    '''
    this function reads the snow day policy text file
    '''
    policy = ''
    with open('snow_day_policy.txt', 'r', encoding='utf-8') as file:
        policy = file.read()
        
    return policy
