from bs4 import BeautifulSoup
import urllib2

physicians = open("physician_links.txt",'r')

physicians_array = physicians.read().split()

#test_doctor = 'http://www.ucirvinehealth.org/find-a-doctor/b/nitin-bhatia'
#test_doctor= 'http://www.ucirvinehealth.org/find-a-doctor/a/rosa-m-andrade'
test_doctor = 'http://www.ucirvinehealth.org/find-a-doctor/a/pablo-abbona'
page = urllib2.urlopen(test_doctor)
soup = BeautifulSoup(page,'html.parser')

getName = soup.find(id='main_1_contentpanel_0_pnlInfo')
doctorName = getName.find('h1').string
print("Name: " + str(doctorName.strip()))


#doc specialties
try:
    getSpecialties = soup.find(id='main_1_contentpanel_0_ctl03_pnlInfoSpecialties')
    specialties = getSpecialties.find('p').string
    print("Specialties: " + specialties + '\n')
except:
    pass



#doc interests
try:
    getInterests = soup.find(id='main_1_contentpanel_0_ctl03_pnlInfoClinicalInterests')
    interests = getInterests.find('p').string
    print("Interests: " + interests)
except:
    pass



#general overview tab
try:
    overview = soup.find(id='pnlOverview')
    education = soup.find(id='pnlEducation')
    bio = soup.find(id="pnlBio")
    location = soup.find(id="pnlLocation")
except:
    pass

print("-------------------------------------------------")

''' --------------------OVERVIEW----------------------------------- '''

#medical services section
try:
    services = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabServices')
    medicalServicesTitle = (services.find('div',{'class':'module-pd-tab-label'}).string)
    medicalServices = (services.find_all('a'))
    print("\t\t\t" + medicalServicesTitle.strip() + "\n")
    print("TESTING")
    for services in medicalServices:
        print(services.string)
except:
    print("None")
    pass
print("-------------------------------------------------")


#certifications section
try:
    ceritifications = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabCertifications')
    certificationsTitle = (ceritifications.find('div',{'class':'module-pd-tab-label'}).string)
    certificaitonList = (ceritifications.find_all('li'))
    print("\t\t\t" + certificationsTitle.strip() + "\n")
    for certs in certificaitonList:
        print(certs.string)
except:
    print("None")
    pass
print("-------------------------------------------------")


#languages section
try:
    languages = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabLanguages')
    languageTitle = (languages.find('div',{'class':'module-pd-tab-label'}).string)
    languageList = (languages.find_all('li'))
    print("\t\t\t" + languageTitle.strip() + "\n")
    for lang in languageList:
        print(lang.string)
except:
    pass

print("-------------------------------------------------")

#gender section
try:
    gender = soup.find(id='main_1_contentpanel_0_ctl05_pnlGender')
    genderTitle = (gender.find('div',{'class':'module-pd-tab-label'}).string)
    print("\t\t\t" + genderTitle.strip() + "\n")
    print(gender.find('div',{'class':'module-pd-tab-label'}).next_sibling.strip())
except:
    pass

print("-------------------------------------------------")

                
''' ------------------------EDUCATION-------------------------------- '''


#medical school section
#try:
getMedSchool = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabEducation')
medSchoolTitle = getMedSchool.find('div',{'class':'module-pd-tab-label'})
medSchoolList = getMedSchool.find_all('div',{'class':'module-pd-attribute'})
print("\t\t\t" + medSchoolTitle.string.strip())
for mschool in medSchoolList:
    print(mschool.text.strip())
print('\n')
#except:
#    pass

#internship section
try:
    getIntern = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabInternship')
    internTitle = getIntern.find('div',{'class':'module-pd-tab-label'})
    internList = getIntern.find_all('div',{'class':'module-pd-attribute'})
    print("\t\t\t" + internTitle.text.strip())
    for ischool in internList:
        print(ischool.text.strip())
    print('\n')
except:
    print("None")
    pass

#residency section
try:
    getResidency = soup.find(id="main_1_contentpanel_0_ctl05_pnlTabResidency")
    residencyTitle = getResidency.find('div',{'class':'module-pd-tab-label'})
    residencyList = getResidency.find('div',{'class':'module-pd-attribute'})
    print("\t\t\t" + residencyTitle.string.strip())
    for rschool in residencyList:
        print(rschool.string.strip())
    print('\n')
except:
    print("None")
    pass

#fellowship section
try:
    getFellowship = soup.find(id="main_1_contentpanel_0_ctl05_pnlTabFellowship")
    fellowshipTitle = getFellowship.find('div',{'class':'module-pd-tab-label'})
    fellowshipList = getFellowship.find('div',{'class':'module-pd-attribute'})
    print("\t\t\t" + fellowshipTitle.string.strip())
    for fship in fellowshipList:
        print(fship.string.strip())
    print('\n')
except:
    pass


print("-------------------------------------------------")

''' ------------------------Bio-------------------------------- '''


#professional positions
try:
    getPositions = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabPublications')
    positionTitle = getPositions.find('div',{'class':'module-pd-tab-label'})
    positionList = getPositions.find_all('li')
    print(positionTitle.string)
    for positions in positionList:
        print(positions.string)
except:
    pass

#awards and recognition
try:
    getAwards = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabAwards')
    awardsTitle = getAwards.find('div',{'class':'module-pd-tab-label'})
    awardList = getAwards.find_all('li')
    print(awardsTitle.string)
    for awards in awardList:
        print(awards.string)
except:
    pass

#more info
try:
    getInfo = soup.find(id='main_1_contentpanel_0_ctl05_pnlTabCommunity')
    infoTitle = getInfo.find('div',{'class':'module-pd-tab-label'})
    infoList = getInfo.find_all('li')
    print(infoTitle.string)
    for info in infoList:
        print(info.string)
except:
    pass

print("-------------------------------------------------")


''' ------------------------Location-------------------------------- '''

### Fix getting phone number
try:
    getFirstLocation = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlOfficeName_0')
    firstLocationTitle = getFirstLocation.find('h5')
    print(firstLocationTitle.text.strip())
    firstLocationAddr = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlAddress_0')
    print("Address: " + firstLocationAddr.text.strip())
    firstLocationNum = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlPhone_0')
    print(firstLocationNum.text.strip() + "\n")
except:
    print("Address: " + "None")
    pass
    
print("-------------------------------------------------")


try:
    getSecondLocation = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlOfficeName_1')
    secondLocationTitle = getSecondLocation.find('h5')
    print(secondLocationTitle.text.strip())
    secondLocationAddr = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlAddress_1')
    print("Address: " + secondLocationAddr.text.strip())
    secondLocationNum = soup.find(id='main_1_contentpanel_0_ctl05_ctl00_rptOffices_pnlPhone_1')
    print(secondLocationNum.text.strip() + "\n")
except:
    print("Address: " + "None")
    pass
