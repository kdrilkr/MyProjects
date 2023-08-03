import logging

class Person:
    contact= {
        "name": [],
        "surname": [],
        "country_code": [],
        "number": []
    }

    def __init__(self, name, surname, country_code, number):
        self.name = name
        self.surname = surname
        self.country_code = country_code
        self.number = number

    def add(self):
        Person.contact["name"].append(self.name)
        Person.contact["surname"].append(self.surname)
        Person.contact["country_code"].append(self.country_code)
        Person.contact["number"].append(self.number)

    def delete(self, name, surname, country_code, number):
        remove_index = None
        for i in range(len(Person.contact["name"])):
            if (Person.contact["name"][i] == name and
                Person.contact["surname"][i] == surname and
                Person.contact["country_code"][i] == country_code and
                Person.contact["number"][i] == number):
                remove_index = i
                break
        if remove_index is not None:
            Person.contact["name"].pop(remove_index)
            Person.contact["surname"].pop(remove_index)
            Person.contact["country_code"].pop(remove_index)
            Person.contact["number"].pop(remove_index)
        else:
            logging.warning("Contact not found. Deletion failed.\n Kisi bulunamadi, silme islemi basarisiz.")

    def edit(self, old_name, old_surname, old_country_code, old_number, new_name, new_surname, new_country_code, new_number):
        edit_index = None
        for i in range(len(Person.contact["name"])):
            if (Person.contact["name"][i] == old_name and
                Person.contact["surname"][i] == old_surname and
                Person.contact["country_code"][i] == old_country_code and
                Person.contact["number"][i] == old_number):
                edit_index = i
                break
        if edit_index is not None:
            Person.contact["name"][edit_index] = new_name
            Person.contact["surname"][edit_index] = new_surname
            Person.contact["country_code"][edit_index] = new_country_code
            Person.contact["number"][edit_index] = new_number
        else:
            logging.warning("Contact not found. Editing failed.\n Kisi bulunamadi, duzenleme islemi basarisiz.")


person = Person("", "", "", "")  # Create one instance of Person

print("Welcome to the Contact Book.\nTelefon Rehberine Hosgeldin.\n########################################")
print("Choose the operation you want.\nKullanmak istediginiz opsiyonu seciniz.\n########################################")
print("1-->Add Person(Kisi Ekle)\n2-->Delete Person(Kisi Sil)\n3-->Edit Person(Kisi Duzenle)\n4-->See the contact(Kisileri goruntule)\n########################################")

while True:
    try:
        opt = int(input(":"))

        if opt == 1:
            name = input("Enter the name(Ismi giriniz): ")
            surname = input("Enter the surname(Soyismi giriniz): ")
            country_code = int(input("Enter the country code(Ulke kodunuz giriniz): "))
            number = int(input("Enter the number(Numarayi giriniz): "))
            person = Person(name, surname, country_code, number)
            person.add()
        
        elif opt == 2:
            name = input("Enter the name(Ismi giriniz): ")
            surname = input("Enter the surname(Soyismi giriniz): ")
            country_code = int(input("Enter the country code(Ulke kodunuz giriniz): "))
            number = int(input("Enter the number(Numarayi giriniz): "))
            person.delete(name, surname, country_code, number)
        
        elif opt == 3:
            oldname = input("Enter the  old name(Eski ismi giriniz): ")
            oldsurname = input("Enter the old surname(Eski soyismi giriniz): ")
            oldcode = int(input("Enter the old country code(Eski ulke kodunuz giriniz): "))
            oldnumber = int(input("Enter the old number(Eski numarayi giriniz): "))
            newname = input("Enter the new name(Yeni ismi giriniz): ")
            newsurname = input("Enter the new surname(Yeni soyismi giriniz): ")
            newcode = int(input("Enter the new country code(Yeni ulke kodunuz giriniz): "))
            newnumber = int(input("Enter the new number(Yeni numarayi giriniz): "))
            person.edit(oldname, oldsurname, oldcode, oldnumber, newname, newsurname, newcode, newnumber)
        
        elif opt == 4:
            print("Contact List(Rehberiniz):\n")
            for i in range(len(person.contact["name"])):
                print(
                    f"{person.contact['name'][i]} {person.contact['surname'][i]}\n "
                    f"{person.contact['country_code'][i]} {person.contact['number'][i]} "
                )
        else:
            print("Invalid option. Please choose a valid operation (1, 2, 3, or 4).")
    except ValueError:
        logging.warning("Invalid input. Please enter a valid integer for the operation.")
