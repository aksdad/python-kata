def generateDSAFile(algoName, signature, folder):
    params = ",".join(signature["params"])
    print(algoName)
    print(signature)
    print(folder)
    template = '''class Solution:
        def {methodName} (self, {params}):
            '''.format(methodName=signature["method_name"], params=params)
    with open(folder + '/' + algoName + '.py', 'x') as f:
        f.write(template)
    
