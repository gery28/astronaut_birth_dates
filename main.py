def get_dict_top_3(dict1):
    return sorted(dict1.items(), key=lambda item: item[1], reverse=True)[:3]


def print_top_3_percent(dict1, top_3):
    total = 0
    for i in dict1.items():
        total += i[1]
    for i in top_3:
        print(f"{i[0]}: {round(i[1] / total * 100, 1)}%")


def main():
    with open("astronauts.csv", "r", encoding="utf-8") as data:
        data.readline()
        data_list = []
        birth_dict = {}
        for i in data.readlines():
            i = i.strip("\n")
            data_list.append(i.split(","))
        for i in data_list:
            month = str(i[-1].split("/")[-3])
            if month in birth_dict.keys():
                birth_dict[month] += 1
            else:
                birth_dict[month] = 1
        print("top 3 birth month:")
        print_top_3_percent(birth_dict, get_dict_top_3(birth_dict))


main()
