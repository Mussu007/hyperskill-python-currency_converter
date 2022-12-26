currency = {"RUB" : 2.98, "ARS" : 0.82, "HNL" : 0.17, "AUD" : 1.9622, "MAD" : 0.208}

user_input = float(input())

for values, keys in currency.items():
    converted_currency = round((keys * user_input), 2)
    print(f"I will get {converted_currency} {values} from the sale of {user_input} conicoins.")