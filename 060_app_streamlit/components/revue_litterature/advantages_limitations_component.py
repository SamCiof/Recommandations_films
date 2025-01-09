from components.base_component import BaseComponent

class AdvantagesLimitationsComponent(BaseComponent):
    def __init__(self):
        super().__init__("Quels sont les avantages et les limitations des systèmes de recommandation basés sur le ML ?")

    def get_content(self):
        return (
            """
            **Avantages** : Les systèmes de recommandation basés sur le machine learning offrent de nombreux avantages. Tout d'abord, ils permettent une personnalisation des recommandations, ce qui signifie que chaque utilisateur reçoit des suggestions adaptées à ses préférences individuelles. En outre, ces systèmes aident les utilisateurs à découvrir de nouveaux contenus qu'ils pourraient ne pas avoir trouvés autrement, élargissant ainsi leurs horizons. En proposant des suggestions pertinentes, ils permettent également aux utilisateurs de gagner du temps en recherchant des contenus qui correspondent à leurs goûts. Enfin, en fournissant des recommandations attrayantes, ces systèmes peuvent contribuer à augmenter l'engagement des utilisateurs sur une plateforme, favorisant ainsi la fidélité et la satisfaction des utilisateurs.
            
            **Limitations** : Malgré leurs avantages, les systèmes de recommandation basés sur le machine learning présentent également certaines limitations importantes. Tout d'abord, ils peuvent être affectés par les biais présents dans les données d'entraînement, ce qui peut conduire à des recommandations discriminatoires ou injustes. Par exemple, l'affaire de l'algorithme de recrutement d'Amazon illustre bien ces risques, mettant en lumière la possibilité de perpétuation de stéréotypes ou de discriminations involontaires. Dans ce cas, l'outil discriminait les femmes candidates, car le modèle avait été entraîné sur des CV soumis à l'entreprise au cours des dix années précédentes, période où les hommes étaient majoritairement embauchés pour des postes techniques. En conséquence, le système avait appris à associer certaines caractéristiques des CV masculins à une performance élevée.
            
            De surcroît, le manque de transparence quant à la manière dont les systèmes de recommandation génèrent leurs suggestions peut susciter la méfiance des utilisateurs quant à leur fiabilité et à leur impartialité. Parfois, ces systèmes ont également tendance à recommander trop de contenu similaire, ce qui limite la diversité des choix offerts aux utilisateurs.
            """
        )