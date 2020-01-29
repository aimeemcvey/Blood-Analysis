def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline low"
    else:
        return "Low"


def LDL_analysis(LDL_level):
    if LDL_level >= 190:
        return "Very high"
    elif 160 <= LDL_level < 189:
        return "High"
    elif 130 <= LDL_level < 159:
        return "Borderline high"
    else:  # LDL_level <130
        return "Normal"


def cholesterol_analysis():
    print("Cholesterol Analysis")
    data_input = input("Enter test results: ")
    # print(data_input)
    test_info = data_input.split("=")
    # print(test_info)
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))
    elif test_info[0] == "LDL":
        answer = LDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))


def new_feature():
    pass


def name_function():
    first_name = input("First name: ")
    last_name = input("Last name: ")


def interface():
    while True:
        print("Cholesterol Calculator")
        print("Options:")
        print("  1 - Cholesterol Analysis")
        print("  9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return
        elif choice == '1':
            cholesterol_analysis()


if __name__ == "__main__":
    interface()
