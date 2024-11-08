import React, { useState, useEffect } from "react";

function FetchPerformance() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("performance/summary/4")
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
        data.map((student, i) => (
          <div key={i}>
            <p>StudentTest: {student.id}</p>
            <p>Username: {student.username}</p>
            <p>Total Opened: {total_opened}</p>
            <p>Total Replied: {total_replied}</p>
            <p>Total clicked: {total_links_clicked}</p>

          </div>
        ))
      )
      }
    </div>
)
};

export default FetchPerformance;
