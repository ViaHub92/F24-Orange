import React, { useEffect, useState } from 'react';
import axios from 'axios';
import EmailView from './EmailView';

function Inbox({ studentId }) {
    const [emails, setEmails] = useState([]);
    const [selectedEmail, setSelectedEmail] = useState(null);

    useEffect(() => {
        // Fetch inbox emails for the specific student
        axios.get(`/messaging/inbox/${studentId}`)
            .then(response => {
                setEmails(response.data.inbox);
            })
            .catch(error => console.error('Error fetching inbox:', error));
    }, [studentId]);

    const handleEmailClick = (emailId) => {
        // Fetch the email details when clicked
        axios.get(`/messaging/view/${emailId}?student_id=${studentId}`)
            .then(response => {
                setSelectedEmail(response.data);
            })
            .catch(error => console.error('Error viewing email:', error));
    };

    const handleReplySubmit = (emailId, replyBody) => {
        // Send a reply to the selected email
        axios.post(`/messaging/reply/${emailId}?student_id=${studentId}`, { reply_body: replyBody })
            .then(() => {
                alert('Reply sent successfully!');
                // Optionally, re-fetch or update the interaction status
            })
            .catch(error => console.error('Error sending reply:', error));
    };

    return (
        <div className="inbox">
            <h2>Inbox</h2>
            <ul className="email-list">
                {emails.map(email => (
                    <li 
                        key={email.id} 
                        className="email-item" 
                        onClick={() => handleEmailClick(email.id)}
                    >
                        <div className="email-header">
                            <strong>{email.subject}</strong>
                            <span className="email-sender">{email.sender}</span>
                        </div>
                        <span className="email-timestamp">
                            {new Date(email.sent_at).toLocaleString()}
                        </span>
                    </li>
                ))}
            </ul>
            {selectedEmail && (
                <EmailView email={selectedEmail} onReply={handleReplySubmit} />
            )}
        </div>
    );
}

export default Inbox;