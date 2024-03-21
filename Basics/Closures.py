def OuterFunction(text):
    def InnerFunction():
        print(text)
    InnerFunction()
    
OuterFunction("Hello")

