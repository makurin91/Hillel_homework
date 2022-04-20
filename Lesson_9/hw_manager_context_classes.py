
"""
Задача-1
У вас есть список(list) IP адрессов. Вам необходимо создать
класс который будет иметь методы:
1) Получить список IP адресов в развернутом виде
(пример 10.11.12.13 -> 13.12.11.10)
2) Получить список IP адресов без первых октетов
(пример 0.11.12.13 -> 11.12.13)
3) Получить список последних октетов IP адресов
(пример 10.11.12.13 -> 13)
Пример инициализации класса
ip_adresses = ["10.11.12.13", "10.11.12.14", "10.11.12.15"]
ip_proccessing = IpProccessing(ip_adresses)
"""


class IpProccessing:
    def __init__(self, ips):
        self.__ip_data = ips

    def get_ips(self):
        return self.__ip_data

    def get_deployed_ips(self):
        return ['.'.join(octet for octet in ip_address.split('.')[::-1]) for ip_address in self.__ip_data]

    def get_ips_without_first_octet(self):
        return ['.'.join(octet for octet in ip_address.split('.')[1:]) for ip_address in self.__ip_data]

    def get_ips_last_octets(self):
        return [ip_address.split('.')[-1] for ip_address in self.__ip_data]


"""
Задача-2
Вам необходимо написать
класс который будет описывать работу с файлами, а
именно:
1) Запись данных в файл
2) Чтение данных из файла
3) Удаление данных из файла
Пример
files_processing = FilesProccessing(file_path, mode)
"""


class FileProccessing:

    def read_data(self, file_name):
        with open(file_name, 'r') as f:
            print(f.read())

    def write_data(self, file_name, text):
        with open(file_name, 'w') as f:
            f.write(text)

    def clear_data(self, file_name):
        with open(file_name, 'w') as f:
            f.close()


class Test:
    ip_adresses = ["10.11.12.13", "10.11.12.14", "10.11.12.15"]
    ip_proc = IpProccessing(ip_adresses)
    print(ip_proc.get_ips())
    print(ip_proc.get_deployed_ips())
    print(ip_proc.get_ips_without_first_octet())
    print(ip_proc.get_ips_last_octets())

    my_new_file = "home_work_file.txt"
    fp = FileProccessing()
    fp.write_data(my_new_file, 'write write write')
    fp.read_data(my_new_file)
    fp.clear_data(my_new_file)
