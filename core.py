import webbrowser


def openLogin(semester):
    url = 'https://www3.reg.cmu.ac.th/regist' \
          + semester + \
          '/student/index.php'
    webbrowser.open(url)


def addCourse(allCourse,semester):
    for course in allCourse:
        url = 'https://www3.reg.cmu.ac.th/regist' \
              + semester + \
              '/student/main.php?act=add&cid=' \
              + course['id'] + \
              '&seclec=' \
              + course['lec'] + \
              '&seclab=' \
              + course['lab']
        webbrowser.open(url)
