import React, { useState, useEffect } from "react";

function FetchPerformanceSummary() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("performance/summary/8")
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
            <p>Total Open: {data.total_opened}</p>
            <p>Total Replied: {data.total_replied}</p>
            <p>Total Links: {data.total_links_clicked}</p>
        </div> 
        )}    
    </div>
  )
};

export default FetchPerformanceSummary;
