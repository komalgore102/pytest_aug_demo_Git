from selenium import webdriver



class Test_001:
    def test_Credence_001(self):
        driver=webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == 'Credence':
            driver.save_screenshot("D:\\Python seleinium\\Pytest_aug_demo\\Screenshots\\Credence.PNG")
            assert  True

        else:
            print("You are at wrong place")
            driver.close()
            assert False

    def test_sum_002(self):
        a=30
        b=50
        sum=a+b
        print("this is sum of a and b" +str(sum))
        if sum==80:
            assert True
        else:
            assert False