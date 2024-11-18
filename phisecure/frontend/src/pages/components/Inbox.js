import React, { useEffect, useState } from 'react';
import axios from 'axios';
import EmailView from './EmailView';

function Inbox() {
    const [emails, setEmails] = useState([]);
    const [selectedEmail, setSelectedEmail] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [studentId, setStudentId] = useState(null); // Added state for studentId

    useEffect(() => {
        const storedStudentId = localStorage.getItem('student_id');
        console.log(storedStudentId); 

        if (!storedStudentId) {
            setError("Student ID not found in localStorage.");
            setLoading(false);
            return;
        }

        setStudentId(storedStudentId); // Set the studentId in the state

        // Fetch inbox emails for the specific student
        axios.get(`/messaging/inbox/${storedStudentId}`)
            .then(response => {
                console.log('Fetched emails:', response.data.inbox);
                setEmails(response.data.inbox);
            })
            .catch(error => {
                console.error('Error fetching inbox:', error);
                setError(error.message);
            })
            .finally(() => setLoading(false)); // Stop loading after fetch
    }, []);

    const handleEmailClick = (emailId) => {
        console.log('email id', emailId); 
        console.log('student id', studentId);
        const email = emails.find(e => e.id === emailId);
        setSelectedEmail(email);
        if (!studentId) {
            setError("Student ID not found.");
            return;
        }

        // Fetch the email details when clicked
        axios.get(`/messaging/view/${emailId}?student_id=${studentId}`)
            .then(response => {
                console.log('Email details from API:', response.data);
                setSelectedEmail(response.data);
                console.log('email id', emailId);
            })
            .catch(error => console.error('Error viewing email:', error));
    };

    const handleReplySubmit = (emailId, replyBody) => {
        console.log('email id', emailId);

        if (!studentId) {
            setError("Student ID not found.");
            return;
        }

        axios.post(`/messaging/reply/${emailId}?student_id=${studentId}`, { reply_body: replyBody }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(() => {
            alert('Reply sent successfully!');
        })
        .catch(error => console.error('Error sending reply:', error));
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

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
                <EmailView email={selectedEmail} onReply={(replyBody) => handleReplySubmit(selectedEmail.email_id, replyBody)} />
            )}
        </div>
    );
}

export default Inbox;
