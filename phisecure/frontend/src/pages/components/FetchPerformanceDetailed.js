import React, { useState, useEffect } from "react";

function FetchPerformanceDetailed() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/performance/detailed/8")  // Add full URL if needed, like `http://localhost:5000/performance/detailed/4`
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      })
      .catch(error => console.error("Error fetching data: ", error));
  }, []);

  return (
    <>
      {data.length === 0 ? (
        <tr>
          <td colSpan="3">Waiting...</td>
        </tr>
      ) : (
        data.map((item, index) => (
          <tr key={index}>
            {/* Interactions Column */}
            <td>
              <p><strong>Opened:</strong> {item.opened ? "Yes" : "No"}</p>
              <p><strong>Link Clicked:</strong> {item.link_clicked ? "Yes" : "No"}</p>
              <p><strong>Replied:</strong> {item.replied ? "Yes" : "No"}</p>
            </td>
            
            {/* Email Body Column */}
            <td>
              
            <div className="email-body-container">
            {item.email_body}
            </div>

            </td>



            {/* Red Flags Column */}
            <td>
            <div className="email-body-container">
              {item.red_flag ? item.red_flag : "No Red Flags"}
            </div>
            </td>
          </tr>
        ))
      )}
    </>
  );
}

export default FetchPerformanceDetailed;