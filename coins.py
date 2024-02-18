#name : Pierre Andre El Boustany
#McGill ID : 26107411

import requests

def dict_to_query(my_dict):
    ''' dict -> str
    >>> dict_to_query({'email': 'jonathan.campbell@mcgill.ca', 'token': 'ABC'})
    'email=jonathan.campbell@mcgill.ca&token=ABC'
    
    >>> dict_to_query({'email': 'pierre.elboustany@mcgill.ca', 'token': 'BJfJsXQDjvVigBGF'})
    'email=pierre.elboustany@mcgill.ca&token=BJfJsXQDjvVigBGF'
    '''
    keys_list = list(my_dict.keys())
    full = ''
    for i in keys_list :
        information = str(i) + '=' + str(my_dict[i])
        if i != keys_list[-1]:
            information += '&'
        full += information
    return full


class Account:
    def __init__(self, email, token):
        '''
        >>> my_acct = Account("jonathan.campbell@mcgill.ca", "ABC")
        >>> my_acct.balance
        -1
        
        >>> my_acct = Account('pierre.elboustany@mcgill.ca', 'BJfJsXQDjvVigBGF')
        >>> my_acct.token
        BJfJsXQDjvVigBGF

        >>> my_acct = Account('pierre.elboustany@mcgill.ca', 'BJfJsXQDjvVigBGF')
        >>> my_acct.email
        pierre.elboustany@mcgill.ca
        '''
        if type(email) != str or type(token) != str or email[-9:] != 'mcgill.ca' :
            raise AssertionError ('the email or the token is incorrect')
        else:
            self.email = email
            self.token = token
            self.balance = -1
            self.request_log = []
            
    def __str__(self):
        '''
        >>> my_acct = Account("jonathan.campbell@mcgill.ca", "ABC")
        >>> print(my_acct)
        jonathan.campbell@mcgill.ca has balance -1
        
        >>> my_acct = Account('pierre.elboustany@mcgill.ca', 'BJfJsXQDjvVigBGF')
        >>> print(my_acct)
        pierre.elboustany@mcgill.ca has balance -1
        '''
        return str(self.email) + ' ' + 'has balance' + ' ' + str(self.balance)
            
    def call_api(self, endpoint, my_dict):
        '''
        >>> my_acct = Account("jonathan.campbell@mcgill.ca", "ABC")
        >>> my_acct.call_api("balance", {'email': my_acct.email})
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        
        my_acct = Account('pierre.elboustany@mail.mcgill.ca', 'BJfJsXQDjvVigBGF')
        >>> my_acct.call_api("balance", {'email': my_acct.email})
        {'message': 825, 'status': 'OK'}
        '''
        if type(endpoint) != str or type(my_dict) != dict or (endpoint != 'transfer' and endpoint != 'balance'):
            raise AssertionError ('one of the inputs is not correct')
        
        my_dict['token'] = self.token
        API_URL = 'https://coinsbot202.herokuapp.com/api/'
        request_url = API_URL + endpoint +'?' + dict_to_query(my_dict)
        result = requests.get(url=request_url).json()
        if result['status'] != 'OK':
            raise AssertionError (result["message"])
        return result
    
    def retrieve_balance(self):
        '''
        >>> my_acct = Account("jonathan.campbell@mcgill.ca", "ABC")
        >>> my_acct.retrieve_balance()
        1
        
        >>> my_acct = Account('pierre.elboustany@mcgill.ca', 'BJfJsXQDjvVigBGF')
        >>> my_acct.retrieve_balance()
        1600
        '''
        general = self.call_api('balance', {'email': self.email , 'token': self.token})
        self.balance = general['message']
        return(self.balance)
    
    def transfer (self, amount, receiver):
        '''
        >>> my_acct = Account("jonathan.campbell@mcgill.ca", "ABC")
        >>> my_acct.retrieve_balance()
        25
        >>> my_acct.transfer(25, "alexa.infelise@mail.mcgill.ca")
        'You have transferred 25 coins of your balance of 25 coins to alexa.infelise@mail.mcgill.ca. Your balance is now 0.'
        
        >>> my_acct = Account('pierre.elboustany@mcgill.ca', 'BJfJsXQDjvVigBGF')
        >>> my_acct.retrieve_balance()
        1600
        >>> my_acct.transfer(100, "marc.srour@mail.mcgill.ca")
        'You have transferred 100 coins of your balance of 1600 coins to marc.srour@mail.mcgill.ca. Your balance is now 1500.'
        '''
        if type(amount) != int or type(receiver) != str: 
            raise AssertionError ('the type of your inputs are not valid')
        
        elif receiver[-9:] != 'mcgill.ca' or receiver == self.email:
            raise AssertionError ("There is a mistake with the email you provided")
        
        elif amount < 0 or amount > self.balance or self.balance == -1 :
            raise AssertionError ("You don't have the facilities for that Big Man")
        
        general = self.call_api ('transfer', {'withdrawal_email': self.email, 'deposit_email': receiver, 'amount': amount})
        return general ['message']
        
    
    
        
