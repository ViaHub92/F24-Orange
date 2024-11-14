import React, { useState, useEffect } from 'react';

const Inbox = ({ studentId }) => {
  const [email, setEmail] = useState(null); // We'll store just the first email here
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Function to fetch inbox emails using fetch
    const fetchInboxEmails = async () => {
      try {
        const response = await fetch(`messaging/inbox/4`);
        
        if (!response.ok) {
          throw new Error('Failed to fetch inbox emails');
        }

        const data = await response.json();
        
        // Get the first email from the inbox
        const firstEmail = data.inbox[0];
        
        if (firstEmail) {
          setEmail(firstEmail); // Store the first email in the state
        } else {
          setError('No emails found');
        }

        setLoading(false);
      } catch (err) {
        console.error("Error fetching inbox:", err);
        setError('Failed to load emails');
        setLoading(false);
      }
    };

    fetchInboxEmails();
  }, [studentId]); // Re-fetch if studentId changes

  if (loading) {
    return <div>Loading email...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (!email) {
    return <div>No email found.</div>;
  }

  return (
    <div>
      <div>
        <strong>Sender:</strong> {email.sender}
      </div>
      <div>
        <strong>Body:</strong> {email.body}
      </div>
      <div>
        <strong>Sent at:</strong> {new Date(email.sent_at).toLocaleString()}
      </div>
    </div>
  );
};

export default Inbox;
