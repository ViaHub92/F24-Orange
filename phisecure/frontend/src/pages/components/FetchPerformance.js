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
        <div>        
            <p>StudentTest: {data.student_id}</p>
            <p>Username: {data.student_name}</p>
            <p>Total Interaction: {data.total_interactions}</p>
            <p>Total Open: {data.total_opened}</p>
            <p>Total Replied: {data.total_replied}</p>
            <p>Total Links: {data.total_links_clicked}</p>
        </div> 
        )}    
    </div>
  )
};

export default FetchPerformance;
