from selenium import webdriver
import time

# SwitchCase use to get the appropriate driver

def getDriver(browesrTestRun):
    match browesrTestRun:
        case "chromeBrowser":
            driverinFunc = webdriver.Chrome()
            return driverinFunc
        case "firefoxBrowser":
            driverinFunc = webdriver.Firefox()
            return driverinFunc
        case default:
            print("No matched browser found")
            return "something"

def websiteOpenScroll(driverinFunction, link1):
    driverinFunction.get(link1)
    time.sleep(1)
    driverinFunction.execute_script("window.scrollBy(0, 2160);")
