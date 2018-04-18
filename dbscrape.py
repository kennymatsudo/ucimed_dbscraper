from bs4 import BeautifulSoup
import urllib2
import re
import json

###################### bugs #########################

# location - no comma between address and city - FIXED
# medschool - no comma between school and study - FIXED
# \t gets returned sometimes - FIXED

#####################################################
physician_database = {}

def openUrl(website):
    page = urllib2.urlopen(website)
    soup = BeautifulSoup(page,'html.parser')
    return soup


def getDocName(soup):
    getName = soup.find(id='main_1_contentpanel_0_pnlInfo')
    name = getName.find('h1').text.strip().replace("."," ")
    return name

def getSpecialties(soup):
    getSpecialties = soup.find(id='main_1_contentpanel_0_ctl03_pnlInfoSpecialties')
    specialties = getSpecialties.find('p').string.strip()
    return specialties

def getInterests(soup):
    try:
        getInterests = soup.find(id='main_1_contentpanel_0_ctl03_pnlInfoClinicalInterests')
        interests = getInterests.find('p').string.strip()
        return interests
    except:
        pass
    
def getServices(soup):
    try:
        serviceArray = []
        services = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabServices')
        medServiceTitle = services.find('div',{'class':'module-pd-tab-label'}).string.strip()
        medicalServices = services.find_all('a')
        for services in medicalServices:
            serviceArray.append(services.string)
        return serviceArray
    except:
        pass
    
def getCert(soup):
    try:
        certArray = []
        getCert = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabCertifications')
        certTitle = getCert.find('div',{'class':'module-pd-tab-label'}).string.strip()
        certList = getCert.find_all('li')
        for certs in certList:
            certArray.append(certs.string)
        return certArray
    except:
        pass

def getLang(soup):
    try:
        langArray = []
        getLang = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabLanguages')
        languageTitle = getLang.find('div',{'class':'module-pd-tab-label'}).string.strip()
        languageList = getLang.find_all('li')
        for lang in languageList:
            langArray.append(lang.string)
        return langArray
    except:
        pass

def getGender(soup):
    try:
        getGender = soup.find(id='main_1_contentpanel_0_ctl05_pnlGender')
        genderTitle = getGender.find('div',{'class':'module-pd-tab-label'}).string.strip()
        return getGender.find('div',{'class':'module-pd-tab-label'}).next_sibling.strip()
    except:
        pass


def getMedSchool(soup):
    try:
        medSchoolArray = []
        getMedSchool = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabEducation')
        medSchoolTitle = getMedSchool.find('div',{'class':'module-pd-tab-label'}).string.strip()
        medSchoolList = getMedSchool.find_all('div',{'class':'module-pd-attribute'})
        for mschool in medSchoolList:
            school = (mschool.find('span').previous_sibling.strip())
            study = (mschool.find('span').text.strip())
            medSchoolArray.append(school + " " + study)
        return medSchoolArray
    except:
        pass
'''
            school = (mschool.find('span').previous_sibling.strip())
            study = (mschool.find('span').text.strip())
            medSchoolArray.append(school + " " + study)
'''

def getIntern(soup):
    try:
        internArray = []
        getIntern = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabInternship')
        internTitle = getIntern.find('div',{'class':'module-pd-tab-label'}).string.strip()
        internList = getIntern.find_all('div',{'class':'module-pd-attribute'})
        for ischool in internList:
            school = (ischool.find('span').previous_sibling.strip())
            study = (ischool.find('span').text.strip())
            internArray.append(school+ " " + study)
            if(ischool.find('br')):
                allInterns = ischool.find_all('br')
                for interns in allInterns:
                    otherSchool = (interns.next_sibling.strip())
                    otherStudy = (interns.next_sibling.next_sibling.text.strip())
                    internArray.append(school+ " "+study)
                
#            else:
#                print('false')
        return internArray
    except:
        pass

def getResidency(soup):
    try:
        resArray = []
        getResidency = soup.find(id="main_1_contentpanel_0_ctl05_pnlTabResidency")
        residencyTitle = getResidency.find('div',{'class':'module-pd-tab-label'}).string.strip()
        residencyList = getResidency.find('div',{'class':'module-pd-attribute'})
        for rschool in residencyList:
            resArray.append(rschool.string.strip())
        return resArray
    except:
        pass

def getFellowship(soup):
    try:
        fellowArray = []
        getFellowship = soup.find(id="main_1_contentpanel_0_ctl05_pnlTabFellowship")
        fellowshipTitle = getFellowship.find('div',{'class':'module-pd-tab-label'}).string.strip()
        fellowshipList = getFellowship.find_all('div',{'class':'module-pd-attribute'})

        for i in fellowshipList:           
            school = i.find('span').previous_sibling.strip()
            study = i.find('span').text.strip()
            fellowArray.append(school+ " - " + study)
            if(i.find('br')):
                allFellowships = i.find_all('br')
                for fellows in allFellowships:
                    otherFellowSchool = fellows.next_sibling.strip()
                    otherFellowStudy = fellows.next_sibling.next_sibling.text.strip()
                    fellowArray.append(otherFellowSchool + " - " + otherFellowStudy)
        
            
        
#        temp = fellowshipList.get_text().strip().replace("\b","").replace("\n","").replace(u'\u2014','-')
#        regex = re.compile('[^a-zA-Z0-9\n]')
#        temp = regex.sub(' ', temp)
#        for i in temp.split("  "):
#            if(len(i) > 4):
#                fellowArray.append(i)
#            else:
#                pass
        return fellowArray
    except:
        pass
            
def getProfPos(soup):
    try:
        profPosArray = []
        getPositions = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabPublications')
        positionTitle = getPositions.find('div',{'class':'module-pd-tab-label'}).string.strip()
        positionList = getPositions.find_all('li')
        for positions in positionList:
            profPosArray.append(positions.text.replace(u"\u2014",""))
        return profPosArray
    except:
        pass

def getAwards(soup):
    try:
        awardArray = []
        getAwards = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabAwards')
        awardsTitle = getAwards.find('div',{'class':'module-pd-tab-label'}).string.strip()
        awardList = getAwards.find_all('li')
        for awards in awardList:
            awardArray.append(awards.text.replace(u"\u2014","").replace(u"\xae"," -"))
        return awardArray
    except:
        pass

def getMoreInfo(soup):
    try:
        infoArray = []
        getInfo = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabCommunity')
        infoTitle = getInfo.find('div',{'class':'module-pd-tab-label'}).string.strip()
        infoList = getInfo.find_all('li')
        for info in infoList:
            infoArray.append(info.string)
        return infoArray
    except:
        pass


def getFirstLoc(soup):
    try:
        getFirstLoc = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlOfficeName_0')
        firstLocTitle = getFirstLoc.find('h5').text.strip()
        firstLocAddr = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlAddress_0')
        addr = (firstLocAddr.find('br').previous_sibling).strip()
        city = (firstLocAddr.find('br').next_sibling).strip()
        #print(addr + ", " + city)
        firstLocNum = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlPhone_0').text.strip().split(" ")
        for number in firstLocNum:
            if(len(number) > 5):
                firstLocNum = number
        return firstLocTitle, (addr + ", " + city), firstLocNum
    except:
        pass

def getSecLoc(soup):
    try:
        getSecLoc = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlOfficeName_1')
        secLocTitle = getFirstLoc.find('h5').text.strip()
        secLocAddr = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlAddress_1').text.strip()
        secLocNum = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlPhone_1').text.strip().split(" ")
        for number in secLocNum:
            if(len(number) > 5):
                firstLocNum = number
        return secLocTitle, secLocAddr, secLocNum
    except:
        pass
    
def toJSON(name,spec,interest,serv,certif,lang,gen,meds,interns,res,fell,prof,awards,info,loc1,loc2):
    physician_database[name] = {
        'name':(name),
        'specialties':(spec),
        'interests':(interest),
        'services': (serv),
        'certifications':(certif),
        'languages':(lang),
        'gender':(gen),
        'med_school':(meds),
        'internships':(interns),
        'residency':(res),
        'fellowship':(fell),
        'professional_position': (prof),
        'awards_recognition':(awards),
        'more_info':(info),
        'first_location':(loc1),
        'second_location':(loc2)
        }
    return physician_database


    
if __name__ == "__main__":

    testfile = open("physician_links.txt")
    for line in testfile:
        soup = openUrl(line)
        
        name = getDocName(soup)
        #print("Name: " + str(name) + "\n")

        specialties = getSpecialties(soup)
        #print("Specialties: " + str(specialties) + "\n")

        interests = getInterests(soup)
        #print("Interests: " + str(interests) + "\n")

        services = getServices(soup)
        #print("Services: " + str(services) + "\n")

        certification = getCert(soup)
        #print("Certifications: " + str(certification) + "\n")

        languages = getLang(soup)
        #print("Languages: " + str(languages) + "\n")

        gender = getGender(soup)
        #print("Gender: " + str(gender) + "\n")

        medical_schools = getMedSchool(soup)
        #print("MedSchool: " + str(medical_schools) + "\n")

        internships = getIntern(soup)
        #print("Intern: " + str(internships) + "\n")

        residency = getResidency(soup)
        #print("Residency: " + str(residency) + "\n")

        fellowship = getFellowship(soup)
        #print("Fellowship: " + str(fellowship) + "\n")

        professional_pos = getProfPos(soup)
        #print("Professional Position: " + str(professional_pos) + "\n")

        awards = getAwards(soup)
        #print("Awards: " + str(awards) + "\n")

        more_info = getMoreInfo(soup)
        #print("More Info: " + str(more_info) + "\n")

        first_location = getFirstLoc(soup)
        #print("Location 1: " + str(first_location) + "\n")

        second_location = getSecLoc(soup)
        #print("Location 2: " + str(second_location) + "\n")
        
        #print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        
        toJSON(name,specialties,interests,services,certification,languages,gender,medical_schools,internships,residency,fellowship,professional_pos,awards,more_info,first_location,second_location)

        with open('outputTest.text','w') as outfile:
            json.dump(physician_database,outfile)
    #print(json.dumps(physician_database))
    '''
    soup = openUrl(test_doctor)
    print("Name: " + getDocName(soup) + "\n")
    print("Specialties: " + getSpecialties(soup) + "\n")
    print("Interests: " + getInterests(soup) + "\n")
    print("Services: " + str(getServices(soup)) + "\n")
    print("Certifications: " + str(getCert(soup)) + "\n")
    print("Languages: " + str(getLang(soup)) + "\n")
    print("Gender: " + str(getGender(soup)) + "\n")
    print("MedSchool: " + str(getMedSchool(soup)) + "\n")
    print("Intern: " + str(getIntern(soup)) + "\n")
    print("Residency: " + str(getResidency(soup)) + "\n")
    print("Fellowship: " + str(getFellowship(soup)) + "\n")
    print("Professional Position: " + str(getProfPos(soup)) + "\n")
    print("Awards: " + str(getAwards(soup)) + "\n")
    print("More Info: " + str(getMoreInfo(soup)) + "\n")
    print("Location 1: " + str(getFirstLoc(soup)) + "\n")
    print("Location 2: " + str(getSecLoc(soup)) + "\n")
    '''
    

   


    

    





    
