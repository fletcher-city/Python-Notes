import json
import os
from datetime import datetime

notes = []

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, separators=(',', ':'))

def load_notes():
    global notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)

def add_note():
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "body": body, "created_at": created_at, "updated_at": created_at}
    notes.append(note)
    save_notes()
    print("Заметка добавлена успешно!")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок заметки: ")
            note["body"] = input("Введите новый текст заметки: ")
            note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована!")
            return
    print("Заметка с таким ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена!")
            return
    print("Заметка с таким ID не найдена.")

def display_notes():
    for note in notes:
        print(f"ID: {note['id']}; Заголовок: {note['title']}; Текст: {note['body']}; Создано: {note['created_at']}; Обновлено: {note['updated_at']}")

def display_notes_by_date(date_type):
    date_format = "%Y-%m-%d %H:%M:%S"
    sorted_notes = sorted(notes, key=lambda x: datetime.strptime(x[date_type], date_format))
    for note in sorted_notes:
        print(f"ID: {note['id']}; Заголовок: {note['title']}; Текст: {note['body']}; Создано: {note['created_at']}; Обновлено: {note['updated_at']}")

load_notes()

while True:
    print("\nМеню:")
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Показать все заметки")
    print("5. Показать заметки по дате создания")
    print("6. Показать заметки по дате обновления")
    print("7. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        display_notes()
    elif choice == "5":
        display_notes_by_date("created_at")
    elif choice == "6":
        display_notes_by_date("updated_at")
    elif choice == "7":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")