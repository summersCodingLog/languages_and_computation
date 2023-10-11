import re

def fixURL(url):
    pattern = re.compile(r'https?://([\w.-]+)/([\w.-]+/)*([\w.-]+)/?')
    match = pattern.search(url)
    if match:
        domain = match.group(1)
        subdirs = match.group(2)
        last_subdir = match.group(3)
        if subdirs.count('/') > 1:
            subdirs = subdirs[:-len(last_subdir)]
            new_url = f'https://{domain}/{subdirs}{last_subdir}'
            return new_url
    return url

import re

def fixURL(url):
    pattern = re.compile(
        r"(?P<protocol>https?:\/\/)"  # match http:// or https://
        r"(?P<subdomain>[\w.]+\/)*"  # match subdomains if present
        r"(?P<domain>seattleu\.edu\.)"
        r"(?P<subdirectories>([\w-]+\/)+)"  # match subdirectories (must be 2 or more)
        r"(?P<lastdir>[\w-]+\/?)"  # match the last directory (with or without a trailing /)
    )
    match = pattern.match(url)
    if match:
        subdirectories = match.group("subdirectories")
        if subdirectories.count("/") >= 2:  # check if there are 2 or more subdirectories
            subdirs_list = subdirectories.strip("/").split("/")  # strip off leading/trailing slashes
            subdirs_list[-1], subdirs_list[-2] = subdirs_list[-2], subdirs_list[-1]  # swap last two subdirectories
            new_subdirectories = "/".join(subdirs_list) + "/"
            return pattern.sub(fr"\g<protocol>\g<subdomain>\g<domain>{new_subdirectories}\g<lastdir>", url)
    return url


url1 = 'https://www.seattleu.edu/scieng/computer-science/bacs/undergraduate/'
url2 = 'https://seattleu.instructure.com/courses/1606917'
url3 = 'https://www.seattleu.edu'
url4 = 'https://www.seattleu.edu/scieng/computer-science/bacs/undergraduate'
url5 = 'https://www.seattleu.edu/scieng/computer-science/bacs/undergraduate//'

print(fixURL(url1)) # https://www.seattleu.edu/scieng/computer-science/undergraduate/bacs/
print(fixURL(url2)) # https://seattleu.instructure.com/courses/1606917
print(fixURL(url3)) # https://www.seattleu.edu
print(fixURL(url4)) # https://www.seattleu.edu/scieng/computer-science/bacs/undergraduate
print(fixURL(url5)) # https://www.seattleu.edu/scieng/computer-science/undergraduate/bacs/


validC_0 = "https://www.seattleu.edu/scieng/computer-science/bacs/undergraduate/"
validC_1 = "https://www.seattleu.edu/scieng/cs/bacs/undergrad_"
validC_2 = "https://seattleu.edu/scieng/cs/bacs_/undergrad"
validC_3 = ""

invalidC_0 = "https://seattleu.instructure.com/courses/1606917"
invalidC_1 = ""
invalidC_2 = ""
invalidC_3 = ""