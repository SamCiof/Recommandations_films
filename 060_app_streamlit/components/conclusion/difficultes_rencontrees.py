from components.base_component import BaseComponent

class DifficultesRencontresComponent(BaseComponent):
    def __init__(self):
        super().__init__("Difficultés rencontrées")

    def get_content(self):
        return """
        Les deux principales difficultés rencontrées ont été liées au matériel et à la coordination au sein de l'équipe. À maintes et maintes reprises, l'infrastructure matérielle s'est révélée insuffisante, en particulier en ce qui concerne la puissance de calcul, qui ne parvenait pas à supporter la charge des traitements requis. En conséquence, nous avons dû explorer des alternatives pour contourner ces limitations. C'est d'ailleurs cette contrainte qui nous a conduits à privilégier le modèle Annoy, lequel a su fonctionner de manière fluide malgré les ressources limitées du serveur.

        En ce qui concerne la coordination au sein de l'équipe, le fait que nous venions de divers horizons professionnels a représenté à la fois une force et une faiblesse. Cela a été une force dans la mesure où nos perspectives variées ont enrichi les solutions apportées aux livrables et au traitement des données. Cependant, cela a également constitué une faiblesse, car nous avons dû apprendre à collaborer efficacement et à adopter un langage commun. Néanmoins, malgré ces défis susdits, nous avons réussi à finaliser les livrables bien avant la date de la soutenance.

        """
