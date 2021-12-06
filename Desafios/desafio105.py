def notas(*n, sit=False):
    notasa = dict()
    notasa['total'] = len(n)
    notasa['maior'] = max(n)
    notasa['menor'] = min(n)
    notasa['média'] = sum(n) / len(n)
    if sit:
        if notasa['média'] < 5:
            notasa['situação'] = 'RUIM'
        elif 5 < notasa['média'] <= 7:
            notasa['situação'] = 'RAZOÁVEL'
        elif notasa['média'] > 7:
            notasa['situação'] = 'BOA'
    return notasa


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)