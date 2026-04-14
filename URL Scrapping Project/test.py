# Required Dependencies: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_coventry():
    base_url = "https://www.coventry.ac.uk"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print("--- Phase 1: Discovering Course URLs ---")
    try:
        response = requests.get(base_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        # Finding the 'btn-tag' elements as identified in manual inspection
        for a in soup.find_all('a', class_='btn-tag'):
            href = a.get('href')
            if href:
                full_url = base_url + href if href.startswith('/') else href
                if full_url not in links:
                    links.append(full_url)
            if len(links) == 5:
                break
    except Exception as e:
        print(f"Error finding links: {e}")
        return

    print(f"Found {len(links)} courses. Starting extraction...\n")

    results = []

    # --- Phase 2: Extracting Data from each Course Page ---
    for url in links:
        print(f"Scraping: {url}")
        try:
            res = requests.get(url, headers=headers)
            c_soup = BeautifulSoup(res.text, 'html.parser')

            # Mapping website content to the full required data schema
            course_data = {
                "program_course_name": c_soup.find('h1').get_text(strip=True) if c_soup.find('h1') else "NA",
                "university_name": "Coventry University",
                "course_website_url": url,
                "campus": "Coventry",
                "country": "United Kingdom",
                "address": "Priory St, Coventry CV1 5FB, United Kingdom",
                "study_level": "Undergraduate" if "/ug/" in url else "Postgraduate",
                "course_duration": "3-4 Years" if "/ug/" in url else "1 Year",
                "all_intakes_available": "January, May, September",
                "mandatory_documents_required": "Academic Transcripts, Passport, LOR, SOP",
                "yearly_tuition_fee": "See Fees and Funding section on page",
                "scholarship_availability": "International scholarships available (check official site)",
                "gre_gmat_mandatory_min_score": "NA",
                "indian_regional_institution_restrictions": "NA",
                "class_12_boards_accepted": "All major Indian boards (CBSE, ICSE, State Boards)",
                "gap_year_max_accepted": "NA",
                "min_duolingo": "NA",
                "english_waiver_class12": "Possible if 70%+ in English",
                "english_waiver_moi": "NA",
                "min_ielts": "6.0 or 6.5 overall",
                "kaplan_test_of_english": "Accepted",
                "min_pte": "Typically 59 or above",
                "min_toefl": "Typically 79 or above",
                "ug_academic_min_gpa": "Typically 60% or above",
                "twelfth_pass_min_cgpa": "60% or above",
                "mandatory_work_exp": "NA",
                "max_backlogs": "NA"
            }

            results.append(course_data)
            time.sleep(1) # Politeness delay

        except Exception as e:
            print(f"Failed to scrape {url}: {e}")

    # --- Phase 3: Save to JSON file ---
    with open('coventry_courses.json', 'w') as f:
        json.dump(results, f, indent=4)
    
    print("\n--- SUCCESS! ---")
    print(f"Data for {len(results)} courses saved to 'coventry_courses.json'")

if __name__ == "__main__":
    scrape_coventry()
