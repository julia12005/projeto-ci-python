def calcular_media(notas: list[float])->float:
    """Retornaamédiadasnotasinformadas."""
    if not notas:
        raise ValueError("Alistadenotasnãopodeestarvazia.")
    return sum(notas)/ len(notas)

def situacao_aluno(media: float)-> str:
    """Classificaoalunoapartirdesuamédiafinal."""
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"

if __name__== "__main__":
    notas_exemplo =[8.0,7.0,9.0]
    media=calcular_media(notas_exemplo)
    print(f"Média:{media:.1f}")
    print(f"Situação:{situacao_aluno(media)}")