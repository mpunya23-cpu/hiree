import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("https://hire-backend-akj8.onrender.com/jobs")
      .then((res) => res.json())
      .then((data) => setJobs(data))
      .catch((err) => console.log(err));
  }, []);

  const filteredJobs = jobs.filter((job) => {
    const text = search.toLowerCase();

    return (
      job.company.toLowerCase().includes(text) ||
      job.categories.join(" ").toLowerCase().includes(text)
    );
  });

  return (
    <div className="app">
      <h1 className="title">DirectHire Local</h1>

      <p className="subtitle">
        Find jobs directly from official company career pages.
      </p>

      <div className="search-box">
        <input
          type="text"
          placeholder="Search AI, Finance, Cloud..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="search-input"
        />
      </div>

      <div className="jobs-grid">
        {filteredJobs.map((job, index) => (
          <div className="job-card" key={index}>
            <h2 className="company-name">{job.company}</h2>

            <p className="location">📍 {job.location}</p>

            <div className="categories">
              {job.categories.map((cat, i) => (
                <span className="category" key={i}>
                  {cat}
                </span>
              ))}
            </div>

            <a
              href={job.base_url}
              target="_blank"
              rel="noreferrer"
              className="career-btn"
            >
              Visit Careers Page
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;