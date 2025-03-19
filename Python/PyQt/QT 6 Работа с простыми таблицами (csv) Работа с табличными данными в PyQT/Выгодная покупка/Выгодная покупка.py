import csv

money = 1000

with open("wares.csv", "r") as f:
    data = csv.reader(f, delimiter=";")
    data_dict = {}

    for row in data:
        data_dict[row[0]] = int(row[1])

    available_products = list(
        (filter(lambda el: el[1] <= money, data_dict.items()))
    )
    available_products = sorted(available_products, key=lambda item: item[1])

    if not available_products:
        with open('output.txt', 'w', encoding="utf-8") as file:
            file.write("error")

    else:
        usage = {}
        point = 0

        with open('output.txt', 'w', encoding="utf-8") as file:
            result = []

            while money:
                if point > len(available_products) - 1:
                    break

                product_name = available_products[point][0]
                product_price = available_products[point][1]

                if product_name not in usage:
                    money -= product_price
                    usage[product_name] = 1
                    if money >= 0:
                        result.append(product_name)

                else:
                    if usage[product_name] < 10:
                        usage[product_name] += 1
                        money -= product_price
                        if money >= 0:
                            result.append(product_name)

                    else:
                        point += 1
                        continue

            file.write(', '.join(result))
