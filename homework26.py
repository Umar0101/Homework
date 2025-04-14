'==================== Umar ===================='
# 1. Агрегация
# Создай класс Team и класс Player. Команда может состоять из игроков, но игроки
# могут существовать и без команды.
# Добавь игрока в команду и выведи всех игроков в команде.
# Ожидаемый вывод:
# Players in team:
# Alice
# Bob

class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self):
        self.player = []
    
    def add_player(self, name):
        self.player.append(name)

    def print_player(self):
        print('Players in team:')
        for p in self.player:
            print(p.name)

    
player_Alice = Player('Alice')
player_Bob = Player('Bob')

obj_team = Team()
obj_team.add_player(player_Alice)
obj_team.add_player(player_Bob)

obj_team.print_player()


# 2. Агрегация с несколькими связями
# Создай классы Company и Employee. Один сотрудник может работать в нескольких
# компаниях. Добавь одного сотрудника в две компании и выведи список
# сотрудников в каждой компании.
# Ожидаемый вывод:
# Employees in Company A:
# John
# Employees in Company B:
# John

class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

    def print_employee(self):
        print(f'Employees in Company {self.name}\n{self.employee.name}')    

employee_John = Employee('John')
company_a = Company('A', employee_John)
company_b = Company('B', employee_John)

company_a.print_employee()
company_b.print_employee()


# 3. Композиция
# Создай класс House и класс Room. Комнаты создаются внутри дома и не могут
# существовать без него.
# Создай дом с двумя комнатами и выведи количество комнат в доме.
# Ожидаемый вывод:
# Number of rooms: 2

class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.room = [Room('Kitchen'), Room('Badroom')]
    
    def print_room(self):
        print(f'Number of rooms: {len(self.room)}')

house = House()
house.print_room()


# 4. Композиция с вложенными объектами
# Создай класс Book и класс Page. Страницы создаются при создании книги и не
# используются отдельно. Выведи количество страниц в книге.
# Ожидаемый вывод:
# Pages in book: 3

class Page:
    def __init__(self, page):
        self.page = page

class Book:
    def __init__(self, name):
        self.name = name
        self.pages = []
    
    def add_page(self,pages):
        for p in range(1, pages + 1):
            self.pages.append(Page(p))

    def print_pages(self):
        print(f'Pages in book: {len(self.pages)}')

book = Book('Маугли')
book.add_page(20)
book.print_pages()        
        

# 5. Композиция в цепочке

# Создай класс Computer, который при инициализации создаёт объекты классов CPU
# и RAM. Выведи информацию о составе компьютера.
# Ожидаемый вывод:
# Computer has:
# CPU: Intel i7
# RAM: 16GB

class CPU:
    def __init__(self, name):
        self.name = name

class Ram():
    def __init__(self, gb):
        self.gb = gb

class Computer:
    def __init__(self, name):
        self.name_company = name
        self.cpu_name = CPU('Intel core i7')
        self.ram_size = Ram('16GB')
    
    def print_computer(self):
        print(f'Computer has:\nCPU: {self.cpu_name.name}\nRAM: {self.ram_size.gb}')

computer = Computer('Mi')
computer.print_computer()


# 6. Агрегация и удаление объектов
# Создай класс Playlist и класс Song. Песни добавляются в плейлист, но при
# удалении плейлиста сами песни не исчезают. Проверь, что песня существует
# после удаления плейлиста.
# Ожидаемый вывод:
# Song still exists: True

class Song:
    def __init__(self, name):
        self.name = name

class Playlist:
    def __init__(self, plist_name):
        self.plist_name = plist_name
        self.song_name = []

    def add_song(self,song):
        self.song_name.append(song)


plist = Playlist('Ислам Идигов')
song1 = Song('Ангелом быть')
plist.add_song(song1)
del plist

print(f'Song still exists: {song1.name is not None}')


# 7. Композиция и удаление объектов
# Создай класс Document и класс Paragraph. При удалении документа все
# параграфы должны быть уничтожены. Проверь, что параграфов больше не
# существует.
# Ожидаемый вывод:
# Paragraphs after document deletion: 0

class Paragraph:
    def __init__(self, para):
        self.para = para

class Document:
    def __init__(self, name):
        self.name = name
        self.para_count = [Paragraph(1), Paragraph(2)]
    def __del__(self):
        self.para_count.clear()
        print(f'Paragraphs after document deletion: {len(self.para_count)}')

doc_obj = Document('Заявление')

del doc_obj

