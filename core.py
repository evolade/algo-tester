from datetime import datetime
def testit(func, rep):
    tests = []
    for i in range(rep):
        startTime = datetime.now()
        func()
        tests.append(str(datetime.now() - startTime)
                [-8:-1] + str(datetime.now() - startTime)[-1])
    res = 0.0
    for i in tests:
        res += float(i)
    res /= len(tests)
    return res
