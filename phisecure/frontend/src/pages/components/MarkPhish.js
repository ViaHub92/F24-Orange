import React, { useState, useEffect } from 'react';

const MarkPhish = () => {
  const [email, setEmail] = useState(null);

  // Fetch the email data from the Flask API
  useEffect(() => {
    const fetchEmail = async () => {
      
      
        // Fetch the email details
        const response = await fetch(`/messaging/view/4`);

        if (!response.ok) {
          throw new Error('Failed to fetch email');
        }

        const data = await response.json();
        setEmail(data);  // Store the email data in state


        const updateResponse = await fetch(`/messaging/view/4`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        });

        if (!updateResponse.ok) {
            throw new Error('Failed to update interaction');
        }
        

    fetchEmail();
  }})

  // Function to mark the email as phishing
  const markAsPhishing = async () => {
    try {
      const response = await fetch(`/messaging/mark_as_phishing/4`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',  // Telling the server the content is JSON
        },
      });

      const data = await response.json();

      if (response.ok) {
        alert('Email marked as phishing!');
        setEmail({ ...email, is_phishing: true });  // Update the state to reflect the change
      } else {
        throw new Error(data.error || 'Failed to mark email as phishing');
      }
    } catch (err) {
      alert('Error marking email as phishing');
    }
  };

  return (
    <div>
    <markAsPhishing />
    </div>
  );
};

export default MarkPhish;
