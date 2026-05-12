import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/jobs")
      .then((response) => response.json())
      .then((data) => {
        setJobs(data);
      });
  }, []);

  const filteredJobs = jobs.filter((job) => {
    const searchText = search.toLowerCase();

    return (
      job.company.toLowerCase().includes(searchText) ||
      job.categories.some((category) =>
        category.toLowerCase().includes(searchText)
      )
    );
  });

  return (
    <div className="app-container">
      <nav className="navbar">
        <h1>DirectHire Local</h1>
      </nav>

      <main className="main-content">
        <section className="hero">
          <h2 className="hero-title">Find Your Next Role</h2>
          <p className="hero-subtitle">
            Search top companies by skills, domains, or interests.
          </p>

          <div className="search-container">
            <input
              type="text"
              className="search-input"
              placeholder="Search AI, Frontend, Finance, Cloud..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </div>
        </section>

        <div className="jobs-grid">
          {filteredJobs.map((job, index) => (
            <div key={index} className="job-card">
              <h3 className="company-name">{job.company}</h3>
              
              <div className="job-location">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                {job.location}
              </div>

              <div className="categories-list">
                {job.categories.map((category, idx) => (
                  <span key={idx} className="category-chip">
                    {category}
                  </span>
                ))}
              </div>

              <a
                href={`${job.base_url}${search}`}
                target="_blank"
                rel="noopener noreferrer"
                style={{ textDecoration: 'none' }}
              >
                <button className="visit-btn">
                  Visit Careers Page
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                  </svg>
                </button>
              </a>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;