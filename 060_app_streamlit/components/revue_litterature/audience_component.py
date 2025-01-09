from components.base_component import BaseComponent

class AudienceComponent(BaseComponent):
    def __init__(self):
        super().__init__("Pour qui ?")

    def get_content(self):
        return (
            """
            Les systèmes de recommandation sont utilisés dans de nombreux secteurs et par diverses plateformes :
            
            **Streaming Vidéo et Musique** : Netflix, YouTube, Spotify
            
            **E-commerce** : Amazon, eBay
            
            **Réseaux Sociaux** : Facebook, LinkedIn
            
            **Bibliothèques Numériques** : Goodreads, Kindle
            
            **Applications de Rencontres** : Tinder, OkCupid
            """
        )