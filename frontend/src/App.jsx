import { useEffect, useState } from "react";

function App() {
  const [jobs, setJobs] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/jobs")
      .then((res) => res.json())
      .then((data) => setJobs(data))
      .catch((err) => console.log(err));
  }, []);

  const filteredJobs = jobs.filter((job) => {
    const searchText = search.toLowerCase();

    return (
      job.company.toLowerCase().includes(searchText) ||
      job.categories.join(" ").toLowerCase().includes(searchText)
    );
  });

  return (
    <div
      style={{
        minHeight: "100vh",
        padding: "20px",
        fontFamily: "Arial",
        backgroundColor: "#f5f5f5",
      }}
    >
      <h1
        style={{
          textAlign: "center",
          fontSize: "40px",
          marginBottom: "10px",
        }}
      >
        DirectHire Local
      </h1>

      <p
        style={{
          textAlign: "center",
          color: "#555",
          marginBottom: "30px",
          fontSize: "18px",
        }}
      >
        Find jobs directly from official company career pages.
      </p>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "10px",
          alignItems: "center",
          marginBottom: "40px",
        }}
      >
        <input
          type="text"
          placeholder="Search AI, Finance, Cloud, Backend..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          style={{
            padding: "12px",
            width: "100%",
            maxWidth: "400px",
            borderRadius: "10px",
            border: "1px solid #ccc",
            fontSize: "16px",
          }}
        />
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
          gap: "20px",
        }}
      >
        {filteredJobs.map((job, index) => (
          <div
            key={index}
            style={{
              backgroundColor: "white",
              padding: "20px",
              borderRadius: "15px",
              boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
            }}
          >
            <h2
              style={{
                marginBottom: "10px",
                fontSize: "24px",
              }}
            >
              {job.company}
            </h2>

            <p>
              <strong>Location:</strong> {job.location}
            </p>

            <p>
              <strong>Categories:</strong>{" "}
              {job.categories.join(", ")}
            </p>

            <a
              href={job.base_url}
              target="_blank"
              rel="noreferrer"
              style={{
                display: "inline-block",
                marginTop: "15px",
                padding: "10px 15px",
                backgroundColor: "#2563eb",
                color: "white",
                borderRadius: "8px",
                textDecoration: "none",
                fontWeight: "bold",
              }}
            >
              View Careers
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;