# module des expressions régulières
import re

# fonction identification des deux membres de l'équation
def format_equation(equation):
    # définition du format ax + b = cx + d
    expression_type=re.compile("(\\-*\d*x *[\\+\\-] *\d*) *= *(\\-*\d*x *[\\+\\-] *\d*)")
    # vérification du format de l'équation
    expression=expression_type.match(equation)
    while expression==None:
        equation=input("ce n'est pas de la forme ax+b=cx+d, veuillez ressaisir votre équation:")
        expression=expression_type.match(equation)
    # identification des deux membres
    membre1=expression.group(1)
    membre2=expression.group(2)

# fonction identification du terme en x et de la constante
def identification(membre):
    expression_type=re.compile("(\\-*\d*x) *[\\+\\-] *(\d*)")
    expression=expression_type.match(membre)
    terme_en_x=expression.group(1)
    constante=expression.group(2)

# saisie de l'équation à résoudre
equation=input("saisissez une équation au format ax+b = cx + d:")


