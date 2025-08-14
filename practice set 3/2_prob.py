# write a python program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected !
<|Date|>'''
print(letter.replace("<|Name|>","ABHIJIT").replace("<|Date|>","24/5/2005"))