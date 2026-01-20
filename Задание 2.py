# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator = ","):
    paricipant_1 = participants_first_group.split(separator)
    paricipant_2 = participants_second_group.split(separator)
    set_1 = set(paricipant_1)
    set_2 = set(paricipant_2)
    common_paricipants = list(set(paricipant_1).intersection(paricipant_2))
    common_paricipants.sort()
    return common_paricipants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator = ","))
