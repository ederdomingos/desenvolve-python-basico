import csv

musicas_por_ano = {}

with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor)

    for linha in leitor:
        try:
            track, artist, artist_count, year, *_ , streams = linha
            year = int(year)
            streams = int(streams)

            if 2012 <= year <= 2022 and artist_count == "1":
                if year not in musicas_por_ano or streams > musicas_por_ano[year][3]:
                    musicas_por_ano[year] = [track, artist, year, streams]
        except:
            continue

resultado = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano)]
print(resultado)
