Требуется написать программу, которая определит тип предложения. 
Если в предложении есть вопросительный знак, то оно вопросительное. 
Если есть восклицательный, то предложение восклицательное. 
Если есть и то и другое, то оно вопросительно-восклицательное. 
Если ни того ни другого в предложении нет, то оно повествовательное. 
Если ко всему прочему в предложении есть хотя бы одна запятая, то оно еще и сложное.

_ans = input()
_newStr= ""
if "," in _ans:
    _newStr = "сложное"+" "
    
if "!" in _ans and "?" in _ans:
    _newStr +="вопросительно-восклицательное"
elif "?" in _ans:
    _newStr += "вопросительное"
elif "!" in _ans:
    _newStr += "восклицательное"
else:
    _newStr +="повествовательное"
print(_newStr)
