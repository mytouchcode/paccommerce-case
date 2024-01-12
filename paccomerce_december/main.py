from math import sqrt
from tabulate import tabulate


class Membership:

    # inisialisasi data
    data = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }

    # inisialisai attribute
    def __init__(self, username):
        self.username = username

    # method untuk menampilkan benefit membership
    def show_benefit(self):
        headers = ["Membership", "Benefit", "Another Benefit"]
        tables = [
            ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojek Online "],
            ["Silver", "8%", "Voucher Makanan"]
        ]

        print("Paccommerce Membership Benefit")
        print("")
        print(tabulate(tabular_data=tables, headers=headers, tablefmt="grid"))

    # method untuk menampilkan requirements membership
    def show_requirement(self):
        headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
        tables = [
            ["Platinum", "8", "15"],
            ["Gold", "6", "10"],
            ["Silver", "5", "7"]
        ]

        print("Paccommerce Membership Requirement")
        print("")
        print(tabulate(tabular_data=tables, headers=headers, tablefmt="grid"))

    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance
    def predict_membership(self, username, monthly_expense, monthly_income):

        res = []

        membership_parameter = [[8, 15], [6, 10], [5, 7]]

        for idx, _ in enumerate(membership_parameter):
            euclidean_distance = round(sqrt((monthly_expense - membership_parameter[idx][0]) ** 2 + \
                                            (monthly_income - membership_parameter[idx][1]) ** 2), 2)

            res.append(euclidean_distance)

        res_dict = {
            "Platinum": res[0],
            "Gold": res[1],
            "Silver": res[2]
        }
        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {res_dict}")

        for member, distance in res_dict.items():
            if distance == min(res):
                self.data[username] = member
                return member

    # method untuk menampilkan membership yang dimiliki
    # dari database yang dimiliki
    def get_membership(self, username):
        if username in self.data:
            get_member = self.data.get(username)

            return get_member

    # method untuk menghitung final price berdasarkan membership
    def calculate_price(self, username, list_harga_barang):
        try:
            if username in self.data:
                membership = self.data.get(username)

                if membership == "Platinum":
                    calculate_discount = (sum(list_harga_barang) * 0.15)
                    final_price = sum(list_harga_barang) - calculate_discount

                elif membership == "Gold":
                    calculate_discount = (sum(list_harga_barang) * 0.10)
                    final_price = sum(list_harga_barang) - calculate_discount

                elif membership == "Silver":
                    calculate_discount = (sum(list_harga_barang) * 0.08)
                    final_price = sum(list_harga_barang) - calculate_discount

                else:
                    raise Exception("Membership Tidak Valid")

            else:
                raise Exception("Username Tidak Ada")

        except:
            raise Exception("Program Tidak Valid")

        return final_price


# Create Instance
user_1 = Membership(username="Bambang")

print(f"username: {user_1.username}")

# Predict Membership
Membership = user_1.predict_membership(username=user_1.username,
                                        monthly_expense=3,
                                        monthly_income=4)
print(Membership)

# Calculate Final Price
final_price = user_1.calculate_price(username=user_1.username,
                                     list_harga_barang=[300_000, 150_000, 1_250_000, 15_000])
print(final_price)
