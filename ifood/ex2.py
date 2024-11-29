sacola = {item[0]: item[1] for item in bag}
    
    for item_id, quantidade in toAdd:
        if item_id in sacola: 
            sacola[item_id] += quantidade
        else:
            sacola[item_id] = quantidade
    
    sacola_atualizada = sorted([[item_id, qtd] for item_id, qtd in sacola.items()])
    
    return sacola_atualizada