class InvalidURLException(Exception):
    def __init__(self,message:str ="Url is not found"):
        self.message =message
        
        super().__init__(self.message)
        