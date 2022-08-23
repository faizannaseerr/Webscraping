from bs4 import BeautifulSoup
import requests
import time

print('Enter in a skill you are unfamiliar with')
unfamiliar_skill = input('> ')
print('Filtering out', unfamiliar_skill, '...')

def FindJobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            key_skills = job.find('span', class_='srp-skills').text.replace(' ', '').replace(',', ', ').strip()
            if unfamiliar_skill not in key_skills:
                company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                more_info = job.header.h2.a['href']
                print(published_date)
                print('Company: ', company_name)
                print('Key Skill Required: ', key_skills)
                print('More Information: ', more_info)
                print('')


            ''' if unfamiliar_skill not in key_skills:
                company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                more_info = job.header.h2.a['href']

                f = open(f'Job Posts/{index}.text', 'w')
                f.write(f'{published_date}\n')
                f.write(f'Company: {company_name}\n')
                f.write(f'Key Skill Required: {key_skills}\n')
                f.write(f'More Information: {more_info}\n')
                print('File Saved: ', index)
                '''

# Un-quote depending on whether you want to print or write details to text files.


if __name__ == '__main__':
    while True:
        FindJobs()
        waiting_time = 10
        print('Waiting 10 minutes...')
        time.sleep(waiting_time * 60)

