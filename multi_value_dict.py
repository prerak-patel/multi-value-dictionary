valid_commands = ['ADD', 'MEMBERS','REMOVE','KEYS','REMOVEALL','CLEAR','KEYEXISTS','VALUEEXISTS','ALLMEMBERS','ITEMS']
dictionary = {}

# Custom Error/Exceptions
class ValueExistsError(Exception):
    def __init__(self,message):
        self.message = message

class NoKeyError(Exception):
    def __init__(self,message):
        self.message = message

class InvalidCommandError(Exception):
    def __init__(self,message):
        self.message = message

class InvalidInputParamsError(Exception):
    def __init__(self,message):
        self.message = message

# Add a member to a collection for a given key. 
# Displays an error if the value already existed in the collection.
def add_members_to_key(split_input):
    key = split_input[1]
    value = split_input[2]

    if key in dictionary:
        try:    
            if value in dictionary.get(key):
                raise ValueExistsError('ERROR, value already exists.')
            else:
                dictionary[key].append(value)
                print('Added')
        except ValueExistsError as vee:
            print(vee.message)
    else:
        dictionary[key] = [value]
        print('Added')
    
    return 'Added'

# Returns all the keys in the dictionary. Order is not guaranteed.
def list_all_keys():
    if not dictionary:
        print('empty set')
    else:
        print(dictionary.keys())
        for key,value in dictionary.items() :
            print (key)
    return get_all_keys()

# Returns the collection of strings for the given key.Return order is not guaranteed. 
# Returns an error if the key does not exists.
def get_members_for_given_key(split_input):
    given_key = split_input[1]
    try:
        if given_key in dictionary: 
            for key,value in dictionary.items():
                if key == given_key:
                    for x in range(len(value)):
                        print(value[x])
        else:
            raise NoKeyError('ERROR, key does not exist.')
    except NoKeyError as nke:
        print(nke.message)

 # Removes a value from a key. If the last value is removed from the key, 
 # they key is removed from the dictionary. If the key or value does not exist, 
 # displays an error.
def remove_value_for_given_key(split_input):
    
    try:
        given_key=split_input[1]
        given_value=split_input[2]
        if given_key in dictionary: 
            list_of_values = dictionary.get(given_key)
            print('Removed')
            if given_value in list_of_values:
                list_of_values.remove(given_value)
                if(len(list_of_values) == 0):
                    del dictionary[given_key]
            else:
                raise ValueExistsError('ERROR, value does not exist')
                # print('ERROR, value does not exist')
        else:
            raise NoKeyError('ERROR, key does not exist')
    except ValueExistsError as vee:
        print(vee.message)
    except NoKeyError as nke:
        print(nke.message)
    except Exception as e:
        print(e.message)

# Removes all value for a key and removes the key from the dictionary. 
# Returns an error if the key does not exist.
def remove_all_value_for_given_key(split_input):
    try:
        given_key=split_input[1]
        if given_key in dictionary: 
            del dictionary[given_key]
        else:
            raise NoKeyError('ERROR, key does not exist')
    except NoKeyError as nke:
        print(nke.message)
    except Exception as e:
        print(e.message)   

# Removes all keys and all values from the dictionary.
def clear_all_keys(split_input):
    dictionary.clear()
    print('Cleared')

# Returns whether a key exists or not.
def key_exists(split_input):
    given_key =split_input[1]
    if not given_key in dictionary:
        return False
    else:
        print('true')
    return True

# Returns whether a value exists within a key. Returns false if the key does not exist.
def value_exists(split_input):
    try:
        given_key=split_input[1]
        given_value=split_input[2]

        if key_exists(split_input):
            values_for_given_key = dictionary.get(given_key)
            if given_value in values_for_given_key:
                print('true')
                return True
            else:
                print('false')
        else:
            raise NoKeyError('ERROR, key does not exist')
        return False
    except NoKeyError as nke:
        print(nke.message)

# Returns all the values in the dictionary. Returns nothing if there are none. 
# Order is not guaranteed.
def get_all_values():
    all_values = []
    for key,value in dictionary.items():
        for x in range(len(value)):
            print(value[x])
            all_values.append(value[x])
    return all_values

# Returns all keys in the dictionary and all of their values. Returns nothing if there are none. 
# Order is not guaranteed.
def get_all_keys():
    all_keys = []
    for key,value in dictionary.items():
        print(key)
        all_keys.append(key)
    return all_keys

# For each command validate is user entered necessary input params.
def validate_input_params(split_input,command):
    if command == 'ADD' and len(split_input) == 3:
        return True
    elif command == 'KEYS' and len(split_input) == 1:
        return True
    elif command == 'MEMBERS' and len(split_input) == 2:
        return True
    elif command == 'REMOVE' and len(split_input) == 3:
        return True
    elif command == 'REMOVEALL' and len(split_input) == 2:
        return True
    elif command == 'CLEAR' and len(split_input) == 1:
        return True
    elif command == 'KEYEXISTS' and len(split_input) == 2:
        return True
    elif command == 'VALUEEXISTS' and len(split_input) == 3:
        return True
    elif command == 'ALLMEMBERS' and len(split_input) == 1:
        return True
    elif command == 'ITEMS' and len(split_input) == 1:
        return True
    return False
        
def main():
    active = True
    try:
        while(active):
            print('Enter the command to execute or Exit:')
            user_input = input()

            if not len(user_input) == 0:
                if user_input.upper() == 'EXIT':
                    active = False
                else:
                    split_input = user_input.split( )
                    command = split_input[0].upper()

                    if (command in valid_commands):
                        if command == "ADD" and validate_input_params(split_input, command):
                            add_members_to_key(split_input)
                        elif command == "KEYS" and validate_input_params(split_input, command):
                            list_all_keys()
                        elif command == "MEMBERS" and validate_input_params(split_input, command):
                            get_members_for_given_key(split_input)
                        elif command == "REMOVE" and validate_input_params(split_input, command):
                            remove_value_for_given_key(split_input)
                        elif command == "REMOVEALL" and validate_input_params(split_input, command):
                            remove_all_value_for_given_key(split_input)
                        elif command == "CLEAR" and validate_input_params(split_input, command):
                            clear_all_keys(split_input)
                        elif command == "KEYEXISTS" and validate_input_params(split_input, command):
                            key_exists(split_input)
                        elif command == "VALUEEXISTS" and validate_input_params(split_input, command):
                            value_exists(split_input)
                        elif command == "ALLMEMBERS" and validate_input_params(split_input, command):
                            get_all_values()
                        elif command == "ITEMS" and validate_input_params(split_input, command):
                            get_all_keys()
                        else:
                            raise InvalidInputParamsError('Invalid numbers of input params.')    
                    else:
                        raise InvalidCommandError('Please enter a valid command.')
            else:
                print('Please enter a command or enter Exit.')
    except InvalidInputParamsError as iipe:
        print(iipe.message)
    except InvalidCommandError as ice:
        print(ice.message)
    except Exception as e:
        print(e.message)


if __name__ == "__main__":
    main()
    



