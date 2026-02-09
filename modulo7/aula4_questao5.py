livros = [
    ("O Caçador de Pipas", "Khaled Hosseini", 2003, 368),
    ("Torto Arado", "Itamar Vieira Junior", 2019, 264),
    ("1984", "George Orwell", 1949, 328),
    ("Dom Casmurro", "Machado de Assis", 1899, 256),
    ("O Hobbit", "J.R.R. Tolkien", 1937, 310),
    ("A Revolução dos Bichos", "George Orwell", 1945, 152),
    ("O Alquimista", "Paulo Coelho", 1988, 208),
    ("Capitães da Areia", "Jorge Amado", 1937, 288),
    ("Memórias Póstumas", "Machado de Assis", 1881, 240),
    ("Duna", "Frank Herbert", 1965, 412)
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        f.write(f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n")
