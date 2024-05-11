print(['love', 'python'][bool('cutshort')])

'''
bool('cutshort') = True and for empty string it's False
['love', 'python'][True] ==> ['love', 'python'][1] ==> python
['love', 'python'][False] ==> ['love', 'python'][0] ==> love
'''
