class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeWarehouse:
    printer_company_ls = []
    scanner_company_ls = []
    copier_company_ls = []
    printer_number_ls = []
    scanner_number_ls = []
    copier_number_ls = []
    printer_prise_ls = []
    scanner_prise_ls = []
    copier_prise_ls = []
    printers = {}
    scanners = {}
    copiers = {}

    def add_to_printers(self, office_equipment):
        try:
            if isinstance(office_equipment.__dict__.get('number'), int) and isinstance(
                    office_equipment.__dict__.get('prise'), (int, float)) is True:
                self.printer_company_ls.append(office_equipment.__dict__.get('company'))
                self.printer_number_ls.append(office_equipment.__dict__.get('number'))
                self.printer_prise_ls.append(office_equipment.__dict__.get('prise'))
                self.printers['companies'] = set(self.printer_company_ls)
                self.printers['total number'] = sum(self.printer_number_ls)
                self.printers['max prise'] = max(self.printer_prise_ls)
                self.printers['min prise'] = min(self.printer_prise_ls)
                return self.printers
            else:
                raise MyError(f'Error. This printer {office_equipment.__dict__.get("company")} cannot be added. '
                              f'Check if number and price values are correct.')
        except MyError as err:
            print(err)

    def add_to_scanners(self, office_equipment):
        try:
            if isinstance(office_equipment.__dict__.get('number'), int) and isinstance(
                    office_equipment.__dict__.get('prise'), (int, float)):
                self.scanner_company_ls.append(office_equipment.__dict__.get('company'))
                self.scanner_number_ls.append(office_equipment.__dict__.get('number'))
                self.scanner_prise_ls.append(office_equipment.__dict__.get('prise'))
                self.scanners['companies'] = set(self.scanner_company_ls)
                self.scanners['total number'] = sum(self.scanner_number_ls)
                self.scanners['max prise'] = max(self.scanner_prise_ls)
                self.scanners['min prise'] = min(self.scanner_prise_ls)
                return self.scanners
            else:
                raise MyError(f'Error. This scanner {office_equipment.__dict__.get("company")} be added. '
                              f'Check if number and price values are correct.')
        except MyError as err:
            print(err)

    def add_to_copiers(self, office_equipment):
        try:
            if isinstance(office_equipment.__dict__.get('number'), int) and isinstance(
                    office_equipment.__dict__.get('prise'), (int, float)):
                self.copier_company_ls.append(office_equipment.__dict__.get('company'))
                self.copier_number_ls.append(office_equipment.__dict__.get('number'))
                self.copier_prise_ls.append(office_equipment.__dict__.get('prise'))
                self.copiers['companies'] = set(self.copier_company_ls)
                self.copiers['total number'] = sum(self.copier_number_ls)
                self.copiers['max prise'] = max(self.copier_prise_ls)
                self.copiers['min prise'] = min(self.copier_prise_ls)
                return self.copiers
            else:
                raise MyError(f'Error. This copier {office_equipment.__dict__.get("company")} '
                              f'cannot be added. Check if number and price values are correct.')
        except MyError as err:
            print(err)

    @property
    def get_info(self):
        return f'Printers info:\n{self.printers}\n' \
               f'Scanners info:\n{self.scanners}\n' \
               f'Copiers info:\n{self.copiers}'


class OfficeEquipment:
    def __init__(self, company, number, prise):
        self.company = company
        self.number = number
        self.prise = prise

    def check(self):
        if isinstance(self.number, int) and isinstance(self.prise, (int, float)):
            print(f'This office equipment {self.company} can be added to the warehouse')
        else:
            print('Confirm number and price values!')

    def __str__(self):
        return self.company


class Printer(OfficeEquipment):
    def __init__(self, company, number, prise, color_printer=False, two_sided=False):
        super().__init__(company, number, prise)
        self.color_printer = color_printer
        self.two_sided_printing = two_sided


class Scanner(OfficeEquipment):
    def __init__(self, company, number, prise, ultrasonic=True):
        super().__init__(company, number, prise)
        self.ultrasonic = ultrasonic


class Copier(OfficeEquipment):
    def __init__(self, company, number, prise, color_copier=False):
        super().__init__(company, number, prise)
        self.color_copier = color_copier


my_warehouse = OfficeWarehouse()
p1 = Printer('Samsumg', '44', 120)
# p1.check()
p2 = Printer('Canon', 12, 159)
p3 = Printer('hp', 25, 99.9)
s1 = Scanner('Canon', 88, 1445)
s2 = Scanner('Toshiba', 12, 1040, ultrasonic=False)
c1 = Copier('Konica', 21, 23456, color_copier=True)
c2 = Copier('Xerox', 22, 12499)
my_warehouse.add_to_printers(p1)
my_warehouse.add_to_printers(p2)
my_warehouse.add_to_printers(p3)
my_warehouse.add_to_scanners(s1)
my_warehouse.add_to_scanners(s2)
my_warehouse.add_to_copiers(c1)
my_warehouse.add_to_copiers(c2)
print()
print(my_warehouse.get_info)
