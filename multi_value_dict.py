class multi_value_dict:

    def __init__(self):
        self.dictionary = {}
    

    # Add a member to a collection for a given key. 
    # Displays an error if the value already existed in the collection.
    def add_members_to_key(self,given_key,given_val):
        try:
            if given_key in self.dictionary:  
                if given_val in self.dictionary.get(given_key):
                    raise Exception('ERROR, value already exists.')
                    # print('ERROR, value already exists.')
                else:
                    self.dictionary[given_key].append(given_val)
                    print('Added')
            else:
                self.dictionary[given_key] = [given_val]
                print('Added')
        except Exception as e:
            print(e)


    def list_all_keys(self):
        if not self.dictionary:
            print('empty set')
        else:
            for key,value in self.dictionary.items() :
                print (key)

    # Returns the collection of strings for the given key.Return order is not guaranteed. 
    # Returns an error if the key does not exists.
    def get_members_for_given_key(self, given_key):
        try:
            if given_key in self.dictionary: 
                for key,value in self.dictionary.items():
                    if key == given_key:
                        for x in range(len(value)):
                            print(value[x])
            else:
                raise KeyError('ERROR, key does not exist.')
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    # Removes a value from a key. If the last value is removed from the key, 
    # they key is removed from the dictionary. If the key or value does not exist, 
    # displays an error.
    def remove_value_for_given_key(self,given_key,given_value):
        try:
            if given_key in self.dictionary: 
                list_of_values = self.dictionary.get(given_key)
                print('Removed')
                if given_value in list_of_values:
                    list_of_values.remove(given_value)
                    if(len(list_of_values) == 0):
                        del self.dictionary[given_key]
                else:
                    raise Exception('ERROR, value does not exist')
            else:
                raise KeyError('ERROR, key does not exist')
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
    
    # Removes all value for a key and removes the key from the dictionary. 
    # Returns an error if the key does not exist.
    def remove_all_value_for_given_key(self,given_key):
        try:
            if given_key in self.dictionary: 
                del self.dictionary[given_key]
                print('Removed')
            else:
                raise KeyError('ERROR, key does not exist')
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    # Removes all keys and all values from the dictionary.
    def clear_all_keys(self):
        self.dictionary.clear()
        print('Cleared')

    # Returns whether a key exists or not.
    def key_exists(self,given_key):
        try:
            if not given_key in self.dictionary:
                print('false')
                return False
            else:
                print('true')
            return True
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    # Returns whether a value exists within a key. Returns false if the key does not exist.
    def value_exists(self,given_key,given_value):
        try:
            if given_key in self.dictionary:
                values_for_given_key = self.dictionary.get(given_key)
                if given_value in values_for_given_key:
                    print('true')
                else:
                    print('false')
            else:
                raise KeyError('ERROR, key does not exist')
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    # Returns all the values in the dictionary. Returns nothing if there are none. 
    # Order is not guaranteed.
    def get_all_values(self):
        for key,value in self.dictionary.items():
            for x in range(len(value)):
                print(value[x])

    # Returns all keys in the dictionary and all of their values. Returns nothing if there are none. 
    # Order is not guaranteed.
    def get_all_keys_with_values(self):
        for key,value in self.dictionary.items():
            for x in range(len(value)):
                print(f"{key}: {value[x]}")
            

    # For each command validate is user entered necessary input params.
    def validate_input_params(self,input_list,command):
        if command == 'ADD' and len(input_list) == 3:
            return True
        elif command == 'KEYS' and len(input_list) == 1:
            return True
        elif command == 'MEMBERS' and len(input_list) == 2:
            return True
        elif command == 'REMOVE' and len(input_list) == 3:
            return True
        elif command == 'REMOVEALL' and len(input_list) == 2:
            return True
        elif command == 'CLEAR' and len(input_list) == 1:
            return True
        elif command == 'KEYEXISTS' and len(input_list) == 2:
            return True
        elif command == 'VALUEEXISTS' and len(input_list) == 3:
            return True
        elif command == 'ALLMEMBERS' and len(input_list) == 1:
            return True
        elif command == 'ITEMS' and len(input_list) == 1:
            return True
        return False

active = True
valid_commands = ['ADD', 'MEMBERS','REMOVE','KEYS','REMOVEALL','CLEAR','KEYEXISTS','VALUEEXISTS','ALLMEMBERS','ITEMS']

mvd = multi_value_dict()
while(active):
    print('Enter the command to execute or Exit:')
    user_input = input()
    try:
        if not len(user_input) == 0:
            if user_input.upper() == 'EXIT':
                active = False
            else:
                input_list = user_input.split( )
                command = input_list[0].upper()

                if (command in valid_commands):
                    if command == "ADD" and mvd.validate_input_params(input_list, command):
                        mvd.add_members_to_key(input_list[1],input_list[2])
                    elif command == "KEYS" and mvd.validate_input_params(input_list, command):
                        mvd.list_all_keys()
                    elif command == "MEMBERS" and mvd.validate_input_params(input_list, command):
                        mvd.get_members_for_given_key(input_list[1])
                    elif command == "REMOVE" and mvd.validate_input_params(input_list, command):
                        mvd.remove_value_for_given_key(input_list[1],input_list[2])
                    elif command == "REMOVEALL" and mvd.validate_input_params(input_list, command):
                        mvd.remove_all_value_for_given_key(input_list[1])
                    elif command == "CLEAR" and mvd.validate_input_params(input_list, command):
                        mvd.clear_all_keys()
                    elif command == "KEYEXISTS" and mvd.validate_input_params(input_list, command):
                        mvd.key_exists(input_list[1])
                    elif command == "VALUEEXISTS" and mvd.validate_input_params(input_list, command):
                        mvd.value_exists(input_list[1],input_list[2])
                    elif command == "ALLMEMBERS" and mvd.validate_input_params(input_list, command):
                        mvd.get_all_values()
                    elif command == "ITEMS" and mvd.validate_input_params(input_list, command):
                        mvd.get_all_keys_with_values()
                    else:
                        raise Exception('Invalid numbers of input params.')
                        # print('Invalid numbers of input params.')
                else:
                    raise Exception('Please enter a valid command.')
                    # print('Please enter a valid command.')
        else:
            raise ValueError('Please enter a valid input.')
    except ValueError as ve:
        print(ve)
    except Exception as e:
            print(e)
