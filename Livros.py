class Book:
    _id_counter = 1

    def __init__(self, name, author, year, is_read):
        self.code = Book._id_counter
        Book._id_counter += 1
        self.name = name
        self.author = author
        self.year = year
        self.is_read = is_read

    def __str__(self):
        read_status = "Lido" if self.is_read else "Não lido"
        return f"[Cód: {self.code}] {self.name} - {self.author} ({self.year}) - {read_status}"


def display_menu():
    print("\n=== Menu ===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Alterar status de leitura")
    print("4. Excluir livro")
    print("5. Sair")


def add_book():
    print("\n--- Adicionar Livro ---")
    name = input("Nome do livro: ")
    author = input("Autor: ")
    year = input("Ano: ")
    while True:
        is_read_input = input("O livro está lido? (s/n): ").lower()
        if is_read_input in ['s', 'n']:
            is_read = is_read_input == 's'
            break
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")
    
    book = Book(name, author, year, is_read)
    books.append(book)
    print("Livro adicionado com sucesso!")


def list_books():
    print("\n--- Lista de Livros ---")
    if not books:
        print("Nenhum livro cadastrado ainda.")
    else:
        for book in books:
            print(book)


def update_read_status():
    print("\n--- Alterar Status de Leitura ---")
    if not books:
        print("Nenhum livro cadastrado ainda.")
        return

    try:
        code = int(input("Digite o código do livro que deseja alterar: "))
        book = next((b for b in books if b.code == code), None)
        if book:
            book.is_read = not book.is_read
            status = "lido" if book.is_read else "não lido"
            print(f"O status de leitura do livro '{book.name}' foi alterado para: {status}.")
        else:
            print("Livro não encontrado.")
    except ValueError:
        print("Código inválido. Por favor, digite um número válido.")


def delete_book():
    print("\n--- Excluir Livro ---")
    if not books:
        print("Nenhum livro cadastrado ainda.")
        return

    try:
        code = int(input("Digite o código do livro que deseja excluir: "))
        book = next((b for b in books if b.code == code), None)
        if book:
            books.remove(book)
            print(f"O livro '{book.name}' foi excluído com sucesso.")
        else:
            print("Livro não encontrado.")
    except ValueError:
        print("Código inválido. Por favor, digite um número válido.")


# Lista para armazenar os livros
books = []

# Programa principal
while True:
    display_menu()
    choice = input("Escolha uma opção: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        list_books()
    elif choice == "3":
        update_read_status()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")


