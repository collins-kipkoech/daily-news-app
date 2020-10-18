
class News:
    '''
    news class to define news Objects
    '''

    def __init__(self,id,title,image,description):
        self.id =id
        self.title = title
        
        self.image = 'https://image.tmdb.org/t/p/w500/'+ image
        self.description = description