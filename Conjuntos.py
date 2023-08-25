### Formas de criar set.

teste_0 = {1, 2, 2, 3}
print(teste_0)

teste_1 = set(["Teste", "teste", "teste"])
print(teste_1)

### percorrendo set com enumerate

teste_3 = {"carro", "moto", "carroça", "avião", "carro" }

for teste, test in enumerate(teste_3):
    print(f"{teste}: {test}")

### {}.union junta valores 

conjunto_a = {1, 2}
conjunto_b = {3,4}

conjunto = conjunto_a.union(conjunto_b)
print(conjunto)

### {}.intersection mostra os valores repitidos 

conjunto_c = {1, 2, 3}
conjunto_d = {1, 2}

conjunto_1 = conjunto_c.intersection(conjunto_d)
print(conjunto_1)

### {}.diference mostra a diferença entre os conjuntos 

conjunto_e = {1, 2, 3, 5}
conjunto_f = {1, 2, 3}

conjunto_2 = conjunto_e.difference(conjunto_f)
print(conjunto_2)

### {}.simetric_difference mostra os valores diferentes em cada conjunto

conjunto_g = {1, 2, 3, 4}
conjunto_h = {1, 2, 3, 5}

conjunto_3 = conjunto_g.symmetric_difference(conjunto_h)
print(conjunto_3)

### {}.issubset valida se um conjunto esta dentro do outro

conjunto_i = {1, 2, 3}
conjunto_j = {1, 2, 3, 4}

conjunto_4 = conjunto_i.issubset(conjunto_j)
conjunto_5 = conjunto_j.issubset(conjunto_i)

print(conjunto_4)
print(conjunto_5)

### {}.issuperset valida se o conjunto de valores estão no set

conjunto_k = {9, 10, 11}
conjunto_l = {11, 10, 9, 8}

conjunto_6 = conjunto_l.issuperset(conjunto_k)
conjunto_7 = conjunto_k.issuperset(conjunto_l)

print(conjunto_6)
print(conjunto_7)

### {}.isdisjoint valida se um valor esta no outro

conjunto_m = {1, 2, 3}
conjunto_n = {4, 5, 6, 7}
conjunto_o = {1,7}

conjunto_8 = conjunto_m.isdisjoint(conjunto_n)
conjunto_9 = conjunto_n.isdisjoint(conjunto_o)

print(conjunto_8)
print(conjunto_9)

### {}.add assim posso adicionar valores 

conjunto_p = {1, 10}
conjunto_p.add(11)

print(conjunto_p)


### {}.copy assim posso copiar valores

conjunto_q = {9, 8}
conjunto_q.copy()

print(conjunto_q)


### {}.clear assim posso apagar valores

conjunto_r = {9, 8}
conjunto_r.clear()

print(conjunto_r)

### {}.discard descarta valores especificos 

conjunto_s = {1, 2, 3}
conjunto_s.discard(1)

print(conjunto_s) 

### {}.pop retira o primeiro valor da lista 

conjunto_t = {1, 2, 3}
conjunto_t.pop()
conjunto_t.pop()

print(conjunto_t)

### {}.remove remove valor especifico

conjunto_u = {1, 2, 3}
conjunto_u.remove(1)
print(conjunto_u)

### {}.len retorna tamanho do conjunto

conjunto_v = {1, 2, 3, 4}
print(len(conjunto_v))

### in valida se valor esta dentro do conjunto

conjunto_w = {1, 2, 3, 4, 5}
print(1 in conjunto_w) 
print(6 in conjunto_w) 











