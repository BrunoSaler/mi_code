#entradas
puntos_partido_ganado=int(3)
puntos_partido_empatado=int(1)
puntos_partido_perdido=int(0)
partidos_ganados=int(input("¿Cuántos partidos ganó tu equipo?: "))
partidos_empatados=int(input("¿Cuántos partidos empató tu equipo?: "))
partidos_perdidos=int(input("¿Cuántos partidos perdió tu equipo?: "))
#operaciones
promedio=((partidos_ganados*puntos_partido_ganado)+(partidos_empatados*puntos_partido_empatado)+(partidos_perdidos*puntos_partido_perdido))/(partidos_ganados+partidos_empatados+partidos_perdidos)
#salida
print(f"El promedio es {promedio:.3f}.")#con el .3f le fuerzo que me ponga 3 decimales