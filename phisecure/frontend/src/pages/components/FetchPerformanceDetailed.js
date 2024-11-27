import React, { useState, useEffect } from "react";
import { Mosaic } from "react-loading-indicators";

function FetchPerformanceDetailed() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const studentId = localStorage.getItem('student_id');
    
    fetch(`/performance/detailed/${studentId}`)
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      })
      .catch(error => console.error("Error fetching data: ", error));
  }, []);

  // Determine the background color based on user interaction
  const getInteractionColor = (opened, linkClicked, replied) => {
    if (!opened) return "white"; // No action
    if (opened && !linkClicked && !replied) return "#d4edda"; // Only opened (green)
    if (opened && linkClicked && !replied) return "#fff3cd"; // Opened and clicked (yellow)
    if (opened && replied) return "#f8d7da"; // Replied (red)
  };

  return (
    <>
      {data.length === 0 ? (
        <tr>
          <p style={{ textAlign: "center" }}>
            <Mosaic color="#231D6C" size="small" text="" textColor="" />
          </p>
        </tr>
      ) : (
        data.map((item, index) => (
          <tr key={index}>
            {/* Interactions Column - Apply color to this td only */}
            <td style={{ backgroundColor: getInteractionColor(item.opened, item.link_clicked, item.replied) }}>
              <p><strong>Opened:</strong> {item.opened ? "Yes" : "No"}</p>
              <p><strong>Link Clicked:</strong> {item.link_clicked ? "Yes" : "No"}</p>
              <p><strong>Replied:</strong> {item.replied ? "Yes" : "No"}</p>
            </td>
            
            {/* Email Body Column */}
            <td>
              <div className="email-body-container" dangerouslySetInnerHTML={{ __html: item.email_body }}></div>
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
