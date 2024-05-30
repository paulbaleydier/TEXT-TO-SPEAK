class Utils:
    
    
    @staticmethod
    def getKeyAPI() -> str:
        with open('.env', 'r') as file:
            for line in file:
                split = line.split("=")
                if len(split) == 2 and split[1].strip():
                    return split[1].strip()
        return ""
    
    @staticmethod
    def getText() -> str:
        strReturn = str()
        with open('text.txt', 'r', encoding='utf8') as file:
            for line in file:
                strReturn += line
        return strReturn