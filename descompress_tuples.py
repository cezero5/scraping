tuple=('Loki', 'Duke', 'Princesa', 'Lisa', 'Burns', 'Latin')

var = {}

for element in tuple:
    var[element] = element
    
for key, value in var.items():
    print(f"Elemento: {key} -> Valor: {value}")

#primer_elemento, segundo_elemento, *_, ultimo_elemento = ('Loki', 'Duke', 'Princesa', 'Lisa', 'Burns', 'Latin')
