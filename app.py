from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

jobs = [
    {
        "company": "EY (GDS)",
        "categories": ["Audit", "Finance", "Consulting", "Tax"],
        "location": "Bangalore",
        "base_url": "https://careers.ey.com/search/?q="
    },

    {
        "company": "Deloitte (USI)",
        "categories": ["Finance", "Audit", "Consulting", "Operations"],
        "location": "Hyderabad",
        "base_url": "https://jobsindia.deloitte.com/search-jobs/results?keywords="
    },

    {
        "company": "PwC (AC)",
        "categories": ["Audit", "Finance", "Consulting", "Tax"],
        "location": "Bangalore",
        "base_url": "https://www.pwc.com/gx/en/careers/job-search.html?query="
    },

    {
        "company": "KPMG (GCC)",
        "categories": ["Audit", "Finance", "Tax", "Consulting"],
        "location": "Mumbai",
        "base_url": "https://kpmg.com/xx/en/home/careers/search-jobs.html?keywords="
    },

    {
        "company": "Accenture Operations",
        "categories": ["Finance", "Operations", "BPO", "Consulting"],
        "location": "Bangalore",
        "base_url": "https://www.accenture.com/in-en/careers/jobsearch?jk="
    },

    {
        "company": "IBM (Finance & Admin)",
        "categories": ["Finance", "Administration", "Cloud", "Operations"],
        "location": "Bangalore",
        "base_url": "https://www.ibm.com/careers/search?field_keyword_18="
    },

    {
        "company": "Genpact",
        "categories": ["Finance", "BPO", "Operations", "Analytics"],
        "location": "Hyderabad",
        "base_url": "https://careers.genpact.com/search-jobs?keywords="
    },

    {
        "company": "Capgemini (BPO)",
        "categories": ["Finance", "BPO", "Operations", "IT Services"],
        "location": "Pune",
        "base_url": "https://www.capgemini.com/careers/job-search/?keyword="
    },

    {
        "company": "Wipro (BPS)",
        "categories": ["BPO", "Finance", "Operations", "Customer Support"],
        "location": "Bangalore",
        "base_url": "https://careers.wipro.com/search/?q="
    },

    {
        "company": "Infosys BPM",
        "categories": ["BPM", "Finance", "Operations", "Consulting"],
        "location": "Bangalore",
        "base_url": "https://career.infosys.com/joblist?searchText="
    },

    {
        "company": "TCS (F&A)",
        "categories": ["Finance", "Accounting", "BPO", "Operations"],
        "location": "Mumbai",
        "base_url": "https://ibegin.tcs.com/iBegin/jobs/search?keyword="
    },

    {
        "company": "HCL (BPO)",
        "categories": ["BPO", "Finance", "Operations", "IT Services"],
        "location": "Noida",
        "base_url": "https://www.hcltech.com/careers/search-jobs?keywords="
    },

    {
        "company": "Cognizant (BPO)",
        "categories": ["BPO", "Finance", "Operations", "IT Services"],
        "location": "Chennai",
        "base_url": "https://careers.cognizant.com/global/en/search-results?keywords="
    },

    {
        "company": "WNS Global",
        "categories": ["BPO", "Finance", "Analytics", "Operations"],
        "location": "Mumbai",
        "base_url": "https://careers.wns.com/search/?q="
    },

    {
        "company": "Mphasis (Finance BPO)",
        "categories": ["Finance", "BPO", "Cloud", "Operations"],
        "location": "Bangalore",
        "base_url": "https://careers.mphasis.com/search/?q="
    },

    {
        "company": "Hexaware (BFSI BPO)",
        "categories": ["Finance", "BFSI", "BPO", "Operations"],
        "location": "Chennai",
        "base_url": "https://hexaware.com/careers/job-openings/?search="
    },

    {
        "company": "Sutherland Global",
        "categories": ["BPO", "Finance", "Customer Support", "Operations"],
        "location": "Chennai",
        "base_url": "https://www.sutherlandglobal.com/careers/job-search?keywords="
    },

    {
        "company": "EXL Service",
        "categories": ["Analytics", "Finance", "BPO", "Operations"],
        "location": "Noida",
        "base_url": "https://exlservice.com/careers/search-jobs?keywords="
    },

    {
        "company": "Firstsource",
        "categories": ["BPO", "Finance", "Operations", "Customer Support"],
        "location": "Bangalore",
        "base_url": "https://www.firstsource.com/careers/job-search?keywords="
    },

    {
        "company": "Concentrix (Finance)",
        "categories": ["Finance", "BPO", "Operations", "Support"],
        "location": "Bangalore",
        "base_url": "https://jobs.concentrix.com/global/en/search-results?keywords="
    },

    {
        "company": "Teleperformance (Finance)",
        "categories": ["Finance", "BPO", "Operations", "Support"],
        "location": "Mumbai",
        "base_url": "https://www.teleperformance.com/en-us/careers/job-opportunities/?keyword="
    },

    {
        "company": "Conduent",
        "categories": ["Finance", "BPO", "Operations", "Business Services"],
        "location": "Bangalore",
        "base_url": "https://jobs.conduent.com/search-jobs?keywords="
    },

    {
        "company": "Aon (GDC India)",
        "categories": ["Finance", "Risk", "Consulting", "Analytics"],
        "location": "Bangalore",
        "base_url": "https://jobs.aon.com/search-jobs?keywords="
    },

    {
        "company": "Societe Generale (GSC)",
        "categories": ["Banking", "Finance", "Risk", "Operations"],
        "location": "Bangalore",
        "base_url": "https://careers.societegenerale.com/en/job-offers/?keywords="
    },

    {
        "company": "Deutsche Bank (GCC)",
        "categories": ["Banking", "Finance", "Risk", "Operations"],
        "location": "Bangalore",
        "base_url": "https://careers.db.com/search-results?keywords="
    },

    {
        "company": "HSBC (GDC)",
        "categories": ["Banking", "Finance", "Operations", "Risk"],
        "location": "Hyderabad",
        "base_url": "https://mycareer.hsbc.com/search-jobs?keywords="
    },

    {
        "company": "Barclays (GCC India)",
        "categories": ["Banking", "Finance", "Risk", "Operations"],
        "location": "Pune",
        "base_url": "https://search.jobs.barclays/job-search-results/?keywords="
    },

    {
        "company": "Standard Chartered (GBS)",
        "categories": ["Banking", "Finance", "Operations", "Risk"],
        "location": "Chennai",
        "base_url": "https://scb.taleo.net/careersection/ex/jobsearch.ftl?keyword="
    },

    {
        "company": "JP Morgan (India Ops)",
        "categories": ["Banking", "Finance", "Operations", "Risk"],
        "location": "Mumbai",
        "base_url": "https://careers.jpmorgan.com/global/en/search?keywords="
    },

    {
        "company": "Goldman Sachs (India)",
        "categories": ["Investment Banking", "Finance", "Risk", "Operations"],
        "location": "Bangalore",
        "base_url": "https://higher.gs.com/search-jobs?q="
    },

    {
        "company": "Citi (India GCC)",
        "categories": ["Banking", "Finance", "Operations", "Risk"],
        "location": "Chennai",
        "base_url": "https://jobs.citi.com/search-jobs?keywords="
    },

    {
        "company": "American Express (India)",
        "categories": ["Finance", "Payments", "Operations", "Risk"],
        "location": "Gurgaon",
        "base_url": "https://aexp.eightfold.ai/careers?query="
    },

    {
        "company": "BNY Mellon (India GDC)",
        "categories": ["Banking", "Finance", "Operations", "Asset Management"],
        "location": "Pune",
        "base_url": "https://bnymellon.eightfold.ai/careers?query="
    },

    {
        "company": "State Street (India GCC)",
        "categories": ["Finance", "Banking", "Asset Management", "Operations"],
        "location": "Bangalore",
        "base_url": "https://statestreet.wd1.myworkdayjobs.com/Global?keywords="
    },

    {
        "company": "McKinsey (GDC)",
        "categories": ["Consulting", "Finance", "Analytics", "Strategy"],
        "location": "Gurgaon",
        "base_url": "https://www.mckinsey.com/careers/search-jobs?query="
    },

    {
        "company": "BCG (India KDC)",
        "categories": ["Consulting", "Strategy", "Finance", "Analytics"],
        "location": "New Delhi",
        "base_url": "https://careers.bcg.com/global/en/search-results?keywords="
    },

    {
        "company": "Bain & Company (India)",
        "categories": ["Consulting", "Finance", "Strategy", "Operations"],
        "location": "Bangalore",
        "base_url": "https://www.bain.com/careers/find-a-role/?keywords="
    },

    {
        "company": "Mercer (India GDC)",
        "categories": ["HR", "Finance", "Consulting", "Analytics"],
        "location": "Gurgaon",
        "base_url": "https://careers.mercer.com/global/en/search-results?keywords="
    },

    {
        "company": "Fidelity (India Ops)",
        "categories": ["Finance", "Asset Management", "Operations", "Analytics"],
        "location": "Bangalore",
        "base_url": "https://jobs.fidelity.com/search-jobs?keywords="
    },

    {
        "company": "Maersk (GCC India)",
        "categories": ["Logistics", "Finance", "Operations", "Supply Chain"],
        "location": "Chennai",
        "base_url": "https://jobsearch.maersk.com/search/?q="
    },

    {
        "company": "BP (GBS India)",
        "categories": ["Energy", "Finance", "Operations", "Procurement"],
        "location": "Pune",
        "base_url": "https://careers.bp.com/search-jobs?keywords="
    },

    {
        "company": "Shell (IGSC India)",
        "categories": ["Energy", "Finance", "Operations", "Analytics"],
        "location": "Bangalore",
        "base_url": "https://jobs.shell.com/search-jobs?keywords="
    },

    {
        "company": "Google India",
        "categories": ["AI", "Cloud", "Finance", "Backend", "Frontend"],
        "location": "Bangalore",
        "base_url": "https://careers.google.com/jobs/results/?q="
    },

    {
        "company": "Microsoft India",
        "categories": ["Cloud", "Finance", "Backend", "AI", "Operations"],
        "location": "Hyderabad",
        "base_url": "https://jobs.careers.microsoft.com/global/en/search?q="
    },

    {
        "company": "Amazon India",
        "categories": ["Finance", "Operations", "SDE", "Frontend", "Cloud"],
        "location": "Chennai",
        "base_url": "https://www.amazon.jobs/en/search?base_query="
    },

    {
        "company": "Oracle India GBS",
        "categories": ["ERP", "Finance", "Backend", "Cloud", "Operations"],
        "location": "Bangalore",
        "base_url": "https://careers.oracle.com/jobs/#en/sites/jobsearch/requisitions?keyword="
    },

    {
        "company": "SAP India",
        "categories": ["ERP", "Cloud", "Finance", "Procurement", "Backend"],
        "location": "Bangalore",
        "base_url": "https://jobs.sap.com/search/?q="
    },

    {
        "company": "Salesforce India",
        "categories": ["CRM", "Cloud", "Frontend", "Finance", "Operations"],
        "location": "Hyderabad",
        "base_url": "https://careers.salesforce.com/en/jobs/?search="
    },

    {
        "company": "Razorpay",
        "categories": ["Fintech", "Finance", "Payments", "Backend", "Operations"],
        "location": "Bangalore",
        "base_url": "https://razorpay.com/jobs/jobs-all/?search="
    },

    {
        "company": "PhonePe",
        "categories": ["Fintech", "Finance", "Payments", "Operations", "Backend"],
        "location": "Bangalore",
        "base_url": "https://www.phonepe.com/careers/jobs/?search="
    },

    {
        "company": "Flipkart",
        "categories": ["E-Commerce", "Frontend", "Backend", "Operations"],
        "location": "Bangalore",
        "base_url": "https://www.flipkartcareers.com/#!/joblist?q="
    },

    {
        "company": "Adobe India",
        "categories": ["Design", "Frontend", "AI", "Cloud", "Software"],
        "location": "Noida",
        "base_url": "https://careers.adobe.com/us/en/search-results?keywords="
    },

    {
        "company": "Intuit India",
        "categories": ["Fintech", "AI", "Backend", "Cloud", "Finance"],
        "location": "Bangalore",
        "base_url": "https://jobs.intuit.com/search-jobs?keywords="
    },

    {
        "company": "Workday India",
        "categories": ["HR Tech", "Cloud", "Backend", "Finance"],
        "location": "Pune",
        "base_url": "https://workday.wd5.myworkdayjobs.com/Workday?keywords="
    },

    {
        "company": "Swiggy",
        "categories": ["Logistics", "Backend", "Frontend", "Operations"],
        "location": "Bangalore",
        "base_url": "https://careers.swiggy.com/#/jobs?search="
    },

    {
        "company": "Zomato",
        "categories": ["FoodTech", "Operations", "Frontend", "Backend"],
        "location": "Gurgaon",
        "base_url": "https://www.zomato.com/careers?search="
    }
]

@app.route("/jobs")
def get_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)