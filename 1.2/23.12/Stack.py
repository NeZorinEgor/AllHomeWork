def checkio(expression):
    list_backets = []
    

    for i in expression:
        if character in "[](){}{}":
            list_backets.append(i)
    if len(list_backets) == 0: 
        return True

    elif all(brackets.count(opening) == brackets.count(closing)
             for opening, closing in zip("[({", "])}")):
        j = 0
        try:
            while j != len(brackets):
                if list_backets[j] == "(" and list_backets[j+1] == ")":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                elif list_backets[j] == "{" and list_backets[j+1] == "}":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                elif list_backets[j] == "[" and list_backets[j+1] == "]":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                else:
                    j += 1

        except:
            return (not list_brackets)
        return False
