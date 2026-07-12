# match-case statement(switch):
# an alternative to using many elif statements.
# execute some code if a value matches a case.(benefit: cleaner and syntax is more readable)

# def week(day):
#     if day == 1:
#         return "sunday"
#     elif day==2:
#         return "monday"
#     elif day ==3:
#         return "tuesday"
#     elif day==4:
#         return "wednesday"
#     else:
#         return "NOT VALID !"
# print(week(1))


# NOW BY USING MATCH-CASE STATEMENT

def week(day):
    match day:
        case 1:
            return "sunday"
        case 2:
            return "monday"
        case 3:
            return "tuesday"
        case 4:
            return "wednesday"
        case 5:
            return "thursday"
        case 6:
            return "friday"
        case 7:
            return "saturday"
        case _:
            return "it's noa a valid day "
print(week(5))


def week(day):
    match day:
        case "sunday" | "monday" | "tuesday"|"thursday":
            return "FALSE"
        case "friday"|"saturday":
            return "TRUE"
        case _:
            return "not valid"
print(week("saturday"))
