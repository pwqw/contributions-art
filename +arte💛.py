from datetime import datetime, timezone, timedelta

from .utils import valida_coherencia, do_the_commits, do_the_push

# La gama de colores es 0-gris hacia 4-verde oscuro
corazon = '000144100144440144144144144044144100441441004414400044440000440'
valida_coherencia(corazon)
letra_e = '110011144111444414144441414444444444444444'
valida_coherencia(letra_e)
letra_t = '0000111000014411111444444444444444400001441000044'
valida_coherencia(letra_t)
letra_r = '410111144114444444444114414444444444444444'
valida_coherencia(letra_r)
letra_a = '1111100444441044444410144044114414444444404444400'
valida_coherencia(letra_a)
simbolo_mas = '001100000140001114110144444000140000014000'
valida_coherencia(simbolo_mas)

start = datetime.now(tz=timezone.utc)
start.hour = 6
start.minute = 33
start.second = 33
start.microsecond = 0
weekday = start.weekday()
if weekday != 5:
    # si no es sábado, arranco desde el próximo sábado.
    start = start - timedelta(days=weekday + 2)
dibujo = corazon + letra_e + letra_t + letra_r + letra_a + simbolo_mas
dibujo.reverse()
valida_coherencia(dibujo)
start = start - timedelta(days=len(dibujo) - 1)
mes_del_commit = start.month
for conts in dibujo:
    if mes_del_commit != start.month:
        print('Haciendo el push del mes {}'.format(mes_del_commit))
        do_the_push()
        input('Presione una tecla para continuar..')
        mes_del_commit = start.month
    do_the_commits(conts, start)
    start = start + timedelta(days=1)
