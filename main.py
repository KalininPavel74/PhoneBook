# Модуль для запуска приложения.

# Телефонный справочник. Концепция MVC. SIDU. Console. Python. 

import control
import export_import
import view_console as view

taskName = '''Задание  №1. Создать телефонный справочник 
с возможностью импорта и экспорта данных в нескольких форматах.
           '''
view.print_text("-----------------------------------\n\r" + taskName)

# Экспортировать первичные данные.
control.choice_first_data_for_DB()
# Показать записи (для наглядности происходящего)
view.print_list(export_import.get_DB_as_list_of_text(20))

# Выполнение операций из главного зациклинного меню
control.looped_menu()