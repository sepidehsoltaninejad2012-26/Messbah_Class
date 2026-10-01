# while sum_unit <= 17 get unit, if sum_unit> 17  print(name :10, by ostad :20 (unit)
lesson_list = []
sum_unit = 0

lesson1 = {
    "title": "title",
    "teacher": "ali alipour",
    "duration": 60,
    "unit": 5
    }
sum_unit = sum_unit+7
lesson_list. append(lesson1)


lesson2 = {
    "lesson": "java",
    "teacher": "reza rezaei",
    "duration": 50,
    "unit":7
}
sum_unit = sum_unit+7
lesson_list.append(lesson2)

print(lesson_list)

for lesson in lesson_list:
    print(f'{lesson["title"]:10} by {lesson["teacher"]:10} ({lesson["unit"]})')
    #print(lesson)


