def testSomething():
    something = makeSomething()
    assert something.name is not None
    # ...

# create an equivalent test case instance as follows,
# with optional set-up and tear-down methods:
testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=makeSomethingDB,
                                     tearDown=deleteSomethingDB)

# this approach is not recommended