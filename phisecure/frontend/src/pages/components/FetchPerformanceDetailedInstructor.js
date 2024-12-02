import React, { useState, useEffect } from "react";
import { Mosaic } from "react-loading-indicators";
import { FaEnvelope, FaEnvelopeOpen, FaCheck, FaTimes } from 'react-icons/fa';

function FetchPerformanceDetailedInstructor({ studentId }) {
  const [data, setData] = useState([]);
  const [openRowIndex, setOpenRowIndex] = useState(null); 
  const [openBody, setBodyIndex] = useState(null);
  const [clickedStatus, setClickedStatus] = useState([]);

  useEffect(() => {
    if (!studentId) {
      console.error("No student ID provided");
      return;
    }
    
    fetch(`/performance/detailed/${studentId}`)
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);  // Log data to ensure it has the right format        
      })
      .catch(error => console.error("Error fetching data: ", error));
  }, [studentId]);  // This effect depends on the studentId prop

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
    setClickedStatus(prevStatus => {
      const updatedStatus = [...prevStatus];
      if (!updatedStatus[index]) {
        updatedStatus[index] = true; // Mark it as clicked
      }
      return updatedStatus;
    });
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
            <tr style={{ backgroundColor: getInteractionColor(item.opened, item.link_clicked, item.replied) }}>              
              {/* Email Subject Column */}
              <td onClick={() => toggleBody(index)} style={{ cursor: 'pointer', color: 'black' }}>
                <div className="email-body-container-subject">
                  {item.email_subject || "No Email Subject"}
                  <span className="tooltip">
                    <strong>Click to View Email</strong>
                  </span>
                </div>
              </td>

              {/* Checked by Instructor or not */}
              <td>
                <div className="email-body-container">
                  {clickedStatus[index] ? (
                    <div className="check-container">
                      <FaCheck style={{ color: 'green', fontSize: '20px' }} />
                    </div>
                  ) : (
                    <FaTimes
                      style={{ color: 'red', cursor: 'pointer', fontSize: '20px' }}
                      onClick={() => setClickedStatus(index)} // Toggle when clicked
                    />
                  )}
                </div>
              </td>

              {/* Instructor Feedback Column */}
              <td className="feedback-column">
                <div className="email-body-container">
                  {item.instructor_feedback ? (
                    <>
                      <FaEnvelope
                        style={{ color: 'green', marginRight: '8px', cursor: 'pointer' }}
                        onClick={() => toggleRow(index)} // Toggle visibility on icon click
                      />
                      {openRowIndex === index && <p>{item.instructor_feedback}</p>}
                    </>
                  ) : (
                    <>
                      <FaEnvelopeOpen
                        style={{ color: 'gray', marginRight: '8px', cursor: 'pointer' }}
                        onClick={() => toggleRow(index)}
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
                  <div
                    dangerouslySetInnerHTML={{
                      __html: item.email_body || "Error fetching email body"
                    }}
                  />
                  <div>
                    <p><strong>Opened:</strong> {item.opened ? "Yes" : "No"}</p>
                    <p><strong>Link Clicked:</strong> {item.link_clicked ? "Yes" : "No"}</p>
                    <p><strong>Replied:</strong> {item.replied ? "Yes" : "No"}</p>
                  </div>
                  <div className="email-body-container">
                    <strong>Red Flags:</strong> {item.red_flag ? item.red_flag : "No Red Flags"}
                  </div>
                </td>
              </tr>
            )}
          </React.Fragment>
        ))
      )}
    </>
  );
}

export default FetchPerformanceDetailedInstructor;
