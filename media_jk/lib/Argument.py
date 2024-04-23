class Argument:
    def __init__(self, args):
        self.commands = []
        self.options = []
        self.optionValues = {} #Dict/Set here... Unique Index/No Repeating Value
        self.args = args
        # print(self.args)

        for arg in self.args:
            if "-" in arg:
                if "=" in arg:
                    # this is option with value
                    pair = arg.split('=')
                    self.optionValues[pair[0]] = pair[1] #appending the key value pair
                    self.options.append(pair[0])
                else:
                    # this is just an option
                    self.options.append(arg)
            else:
                self.commands.append(arg)
        
        

    def hasOptions(self, options: list):
        useroptions = set(self.options)
        reqoptions = set(options)
        return len(list(reqoptions & useroptions)) == len(options)
    
    def hasOption(self, option):
        return option in self.hasOptions([option])

    def hasOptionValue(self, option):
        return option in self.optionValues
    
    def hasCommands(self, commands):
        usercommands = set(self.commands)
        reqcommands = set(commands)
        return list(usercommands & reqcommands)
    
    def hasCommand(self, command):
        return command in self.hasCommands([command])

    def getOptionValue(self, option, default=None):
        if option in self.optionValues:
            return self.optionValues[option]
        else:
            return default 

        
