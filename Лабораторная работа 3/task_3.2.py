def find_common_participants(group_1, group_2, divided_by=","):
    divided_1 = group_1.split(divided_by)
    divided_2 = group_2.split(divided_by)

    common_participants = list(set(divided_1).intersection(divided_2))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, divided_by="|"))
