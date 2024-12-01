import React, { useState, useEffect } from "react";
import { Mosaic } from "react-loading-indicators";
import { FaEnvelope, FaEnvelopeOpen } from 'react-icons/fa';

function FetchPerformanceDetailed() {
  const [data, setData] = useState([]);
  const [openRowIndex, setOpenRowIndex] = useState(null); // Track which row is open
  const [openBody, setBodyIndex] = useState(null);

  useEffect(() => {
    const studentId = localStorage.getItem('student_id');
    
    fetch(`/performance/detailed/${studentId}`)
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);  // Log data to ensure it has the right format
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

  // Toggle the open/close state of the email body or feedback
  const toggleRow = (index) => {
    setOpenRowIndex(prevIndex => (prevIndex === index ? null : index));
  };

  const toggleBody = (index) => {
    setBodyIndex(prevIndex => (prevIndex === index ? null : index));
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
          <React.Fragment key={index}>
            {/* Main row with interaction data */}
            <tr>
              <td style={{ backgroundColor: getInteractionColor(item.opened, item.link_clicked, item.replied) }}>
                <p><strong>Opened:</strong> {item.opened ? "Yes" : "No"}</p>
                <p><strong>Link Clicked:</strong> {item.link_clicked ? "Yes" : "No"}</p>
                <p><strong>Replied:</strong> {item.replied ? "Yes" : "No"}</p>
              </td>

              {/* Email Subject Column */}
              <td onClick={() => toggleBody(index)} style={{ cursor: 'pointer', color: 'blue' }}>
                <div className="email-body-container-subject">
                  {item.email_subject || "No Email Subject"}
                  <span className="tooltip">
                    <strong>Click to View Email</strong>
                  </span>                                
                </div>
              </td>

              {/* Red Flags Column */}
              <td>
                <div className="email-body-container">
                  {item.red_flag ? item.red_flag : "No Red Flags"}
                </div>
              </td>

              {/* Instructor Feedback Column */}
              <td>
                <div className="email-body-container">
                  {item.instructor_feedback ? (
                    <>
                      <FaEnvelope
                        style={{ color: 'green', marginRight: '8px', cursor: 'pointer' }}
                        onClick={() => toggleRow(index)} // Toggle visibility on icon click
                      /> 
                      {openRowIndex === index && <p>{item.instructor_feedback}</p>} {/* Show feedback when row is open */}
                    </>
                  ) : (
                    <>
                      <FaEnvelopeOpen
                        style={{ color: 'gray', marginRight: '8px', cursor: 'pointer' }}
                        onClick={() => toggleRow(index)} // Toggle visibility on icon click
                      />
                      {openRowIndex === index}
                    </>
                  )}
                </div>
              </td>
            </tr>

            {/* Row to display feedback beneath the current row for feedback and email body */}
            {openRowIndex === index && (
              <tr className="feedback-row">
                <td colSpan="5" style={{ backgroundColor: '#f9f9f9' }}>
                  {item.instructor_feedback || "No Feedback"}
                </td>
              </tr>
            )}
            {openBody === index && (
              <tr className="body-row">
                <td colSpan="5" style={{ backgroundColor: '#f9f9f9' }}>
                  {item.email_body || "Error fetching email body"}
                </td>
              </tr>
            ) }
          </React.Fragment>

        ))
      )}
    </>
  );
}

export default FetchPerformanceDetailed;
