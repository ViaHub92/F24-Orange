import React, { useState, useEffect } from 'react';

const EmailDetailsByIndex = ({ studentId, emailIndex }) => {
  const [emailDetails, setEmailDetails] = useState({ sender: null, subject: null, body: null });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchEmails = async () => {
      try {
        // Fetch the list of emails for the student
        const response = await fetch(`messaging/inbox/4`);
        
        if (!response.ok) {
          throw new Error('Failed to fetch emails');
        }

        const data = await response.json();
        
        // Check if the requested index is valid
        if (data.inbox && data.inbox.length > emailIndex) {
          const email = data.inbox[emailIndex];  // Get the email at the specified index
          
          // Extract sender, subject, and body
          setEmailDetails({
            sender: email.sender,
            subject: email.subject,
            body: email.body
          });
        } else {
          throw new Error(`No email found at index ${emailIndex}`);
        }

        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchEmails();
  }, [studentId, emailIndex]);  // Dependency array includes emailIndex for dynamic fetching

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <p><strong>From:</strong> {emailDetails.sender}</p>
      <p><strong>Subject:</strong> {emailDetails.subject}</p>
      <p><strong>Body:</strong> {emailDetails.body}</p>
    </div>
  );
};

export default EmailDetailsByIndex;
