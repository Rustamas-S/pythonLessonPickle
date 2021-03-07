import re  # Regex biblioteka
import pickle


class DataParser:
    def __init__(self, path, parsed_fields):  # Nes tik vienas txt failo variantas, kur "path" kreipiasi tiesiai į klasę
        self.path = path
        self.instruction_list = parsed_fields.items()  # padaro tuplų listą (2 tuple su email ir telephone)
        print(self.instruction_list)

    def parse_file(self):
        file_content = self.read_file()
        result = []
        for line in file_content:
            line_data = dict()
            for field, regex in self.instruction_list:
                match = re.search(regex, line) and re.search(regex, line)[0] or ""
                line_data[field] = match
            result.append(line_data)

        return result

    def read_file(self):
        file_content_list = []
        with open(self.path) as file_data:
            for line in file_data:
                file_content_list.append(line)


return file_content_list


class Employee:
    def __init__(self, data_):
        self.email = self.validate_email(data_.get("email", "") or "")
        self.telephone = data_.get("telephone", "") or ""

    def __repr__(self):
        return f"Darbuotojo emailas: {self.email}, telefonas: {self.telephone}"

    @staticmethod
    def validate_email(email):
        if email:
            return email

else:
error1 = f"Email {email} is invalid !!! All employees must have valid email.\n"
error2 = f"Kita bet kokia klaida"
error = error1 + error2
raise ValueError(error)


class ObjectSerialiser:
    def __init__(self, file_name, file_read_format, file_write_format):
        self.file_name = file_name
        self.r_format = file_read_format  # read bites
        self.w_format = file_write_format  # write files

    def put_into_pickle(self, employees):
        with open(self.file_name, self.w_format) as f:
            pickle.dump(employees, f)
            print(f"Saved {self.file_name} into pickle.")

    def get_from_pickle(self):
        result = False
        with open(self.file_name, self.r_format) as f:
            result = pickle.load(f)

        return result


if __name__ == "__main__":
    object_serializer = ObjectSerialiser(
        'save1',
        "rb",  # "rb" ir ne kitaip
        "wb"  # "wb" ir ne kitaip
    )
    # reikia uzkomentuoti printa leidziant pirma karta,
    #  leidziant antra karta uzkomentuoti viska po printu.
    # print(object_serializer.get_from_pickle())
    parser = DataParser(
        "/home/wooden/workspace/sdacademy/multithread_train/data.txt",
        {
            "email": r'[\w\.-]+@[\w\.-]+',
            "telephone": r'[\d|\-]{2,23}'
        }
    )
    parsed_employee_data = parser.parse_file()
    employee_list = []
    for employee_data in parsed_employee_data:
        try:
            employee = Employee(employee_data)
        except ValueError as error:
            print(error)
            continue

employee_list.append(employee)

object_serializer.put_into_pickle(employee_list)

print(employee_list)
print(object_serializer.get_from_pickle())
