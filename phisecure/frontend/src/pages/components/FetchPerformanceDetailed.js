import React, { useState, useEffect } from "react";

function FetchPerformanceDetailed() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/performance/detailed/4")  // Add full URL if needed, like `http://localhost:5000/performance/detailed/4`
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      })
      .catch(error => console.error("Error fetching data: ", error));
  }, []);

  return (
    <div>
      {data.length === 0 ? (
        <p>Waiting...</p>
      ) : (
        <div>
          {data.map((item, index) => (
            <div key={index} style={{ marginBottom: "20px", borderBottom: "1px solid #ddd", padding: "10px" }}>
              <tr>
              <p><strong>Email Subject:</strong> {item.email_subject}</p>
              <p><strong>Opened:</strong> {item.opened ? "Yes" : "No"}</p>
              <p><strong>Link Clicked:</strong> {item.link_clicked ? "Yes" : "No"}</p>
              <p><strong>Replied:</strong> {item.replied ? "Yes" : "No"}</p>
              </tr>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default FetchPerformanceDetailed;