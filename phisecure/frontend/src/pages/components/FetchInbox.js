import { useEffect, useState } from 'react';

const Inbox = ({ studentId }) => {
  const [emails, setEmails] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchInbox = async () => {
      try {
        // Make the fetch request to the correct endpoint, using the student_id in the URL path
        const response = await fetch(`messaging/inbox/4`);
        
        // Check if the response is OK (status 200)
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON data
        const data = await response.json();

        // If the inbox data is returned correctly, set it into state
        setEmails(data.inbox);
      } catch (error) {
        console.error("Error fetching data:", error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    // Call the function to fetch inbox data
    fetchInbox();
  }, [studentId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Inbox</h1>
      <ul>
        {emails.map(email => (
          <li key={email.id}>
            <strong>{email.subject}</strong> from {email.sender}
            <p>{email.body}</p>
            <small>{new Date(email.sent_at).toLocaleString()}</small>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Inbox;
