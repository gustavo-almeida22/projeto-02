# criar funções para as notas

nome = str(input('Digite seu nome: '))
alunoOuProf = str(input('Você é aluno ou professor? '))
if alunoOuProf=='Aluno' or 'aluno':
    print('''Olá, eu sou o programa feito para você aluno,
descobrir suas médias por área de conhecimento.''')
    print('Agora digite suas notas por período em cada matéria:')
elif alunoOuProf=='professor' or 'Professor' or 'professora' or 'Professora':
    print('''Olá, eu sou o programa feito para você professor(a),
descobrir as médias por área de conhecimento de seus alunos.''')
    print('Agora digite as notas por período em cada matéria:')

# Matérias
print('1º BIMESTRE:')
mt1 = float(input('Matemática: '))
lp1 = float(input('Língua Portuguesa: '))
li1 = float(input('Língua Inglesa: '))
le1 = float(input('Língua Espanhola: '))
arte1 = float(input('Arte: '))
edFis1 = float(input('Educação Física: '))
geo1 = float(input('Geografia: '))
his1 = float(input('História: '))
fil1 = float(input('Filosofia: '))
soc1 = float(input('Sociologia: '))
fis1 = float(input('Física: '))
qui1 = float(input('Química: '))
bio1 = float(input('Biologia: '))

print('2º BIMESTRE:')
mt2 = float(input('Matemática: '))
lp2 = float(input('Língua Portuguesa: '))
li2 = float(input('Língua Inglesa: '))
le2 = float(input('Língua Espanhola: '))
arte2 = float(input('Arte: '))
edFis2 = float(input('Educação Física: '))
geo2 = float(input('Geografia: '))
his2 = float(input('História: '))
fil2 = float(input('Filosofia: '))
soc2 = float(input('Sociologia: '))
fis2 = float(input('Física: '))
qui2 = float(input('Química: '))
bio2 = float(input('Biologia: '))

print('3º BIMESTRE:')
mt3 = float(input('Matemática: '))
lp3 = float(input('Língua Portuguesa: '))
li3 = float(input('Língua Inglesa: '))
le3 = float(input('Língua Espanhola: '))
arte3 = float(input('Arte: '))
edFis3 = float(input('Educação Física: '))
geo3 = float(input('Geografia: '))
his3 = float(input('História: '))
fil3 = float(input('Filosofia: '))
soc3 = float(input('Sociologia: '))
fis3 = float(input('Física: '))
qui3 = float(input('Química: '))
bio3 = float(input('Biologia: '))

print('4º BIMESTRE:')
mt4 = float(input('Matemática: '))
lp4 = float(input('Língua Portuguesa: '))
li4 = float(input('Língua Inglesa: '))
le4 = float(input('Língua Espanhola: '))
arte4 = float(input('Arte: '))
edFis4 = float(input('Educação Física: '))
geo4 = float(input('Geografia: '))
his4 = float(input('História: '))
fil4 = float(input('Filosofia: '))
soc4 = float(input('Sociologia: '))
fis4 = float(input('Física: '))
qui4 = float(input('Química: '))
bio4 = float(input('Biologia: '))

# Cálculos

mediaMatematica = (mt1 + mt2 + mt3 + mt4)/4
mediaPortugues = (lp1 + lp2 + lp3 + lp4)/4
mediaIngles = (li1 + li2 + li3 + li4)/4
mediaEspanhol = (le1 + le2 + le3 + le4)/4
mediaArte = (arte1 + arte2 + arte3 + arte4)/4
mediaEdFisica = (edFis1 + edFis2 + edFis3 + edFis4)/4
mediaGeografia = (geo1 + geo2 + geo3 + geo4)/4
mediaHistoria = (his1 + his2 + his3 + his4)/4
mediaFilosofia = (fil1 + fil2 + fil3 + fil4)/4
mediaSociologia = (soc1 + soc2 + soc3 + soc4)/4
mediaFisica = (fis1 + fis2 + fis3 + fis4)/4
mediaQuimica = (qui1 + qui2 + qui3 + qui4)/4
mediaBiologia = (bio1 + bio2 + bio3 + bio4)/4


# Média por área

mediaNatureza = (mediaBiologia + mediaFisica + mediaQuimica)/3
mediaHumanas = (mediaFilosofia + mediaSociologia + mediaGeografia + mediaHistoria)/4
mediaLinguagens = (mediaArte + mediaEspanhol + mediaIngles + mediaPortugues + mediaEdFisica)/5
mediaCompleta = (mediaBiologia + mediaFisica + mediaQuimica + mediaFilosofia + mediaSociologia + mediaGeografia + mediaHistoria + mediaArte + mediaEspanhol + mediaIngles + mediaPortugues + mediaEdFisica + mediaMatematica)/13





