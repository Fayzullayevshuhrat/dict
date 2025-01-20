class Company:
    def init(self, cn, year, founder):
        self.cn = cn
        self.year = year
        self.founder = founder

    def to_dict(self):
        return {
            "company_name": self.cn,
            "year": self.year,
            "founder": self.founder,
        }


class Product:
    def init(self, pn, price, amount, company):
        self.pn = pn
        self.price = price
        self.amount = amount
        self.company = company

    def str(self):
        return f"Mahsulot: {self.pn}, Narxi: {self.price}, Miqdori: {self.amount}, Kompaniya: {self.company.cn}"

    def to_dict(self):
        return {
            "product_name": self.pn,
            "price": self.price,
            "amount": self.amount,
            "company": self.company.to_dict(),
        }


class Basket:
    def init(self):
        self.products = []

    def add(self, product):
        for i in self.products:
            if i.pn == product.pn:
                i.amount += product.amount
                return

        self.products.append(product)

    def remove(self, product_name):
        self.products = [p for p in self.products if p.pn != product_name]

    def view(self):
        for i in self.products:
            print(i)

    def total(self):
        summa = 0
        for product in self.products:
            summa += product.price * product.amount
        return summa

    def to_dict(self):
        return {
            "products": [product.to_dict() for product in self.products],
            "total_price": self.total(),
        }