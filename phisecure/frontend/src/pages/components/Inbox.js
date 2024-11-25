import React, { useEffect, useState } from 'react';
import axios from 'axios';
import EmailView from './EmailView';

function Inbox() {
    const [emails, setEmails] = useState([]);
    const [selectedEmail, setSelectedEmail] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [studentId, setStudentId] = useState(null);

    useEffect(() => {
        const storedStudentId = localStorage.getItem('student_id');
        console.log(storedStudentId); 

        if (!storedStudentId) {
            setError("Student ID not found in localStorage.");
            setLoading(false);
            return;
        }

        setStudentId(storedStudentId);

        axios.get(`/messaging/inbox/${storedStudentId}`)
            .then(response => {
                console.log('Fetched emails:', response.data.inbox);
                setEmails(response.data.inbox);
            })
            .catch(error => {
                console.error('Error fetching inbox:', error);
                setError(error.message);
            })
            .finally(() => setLoading(false));
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

    const handleLinkClick = (emailId, url) => {
        
        console.log('Link clicked: ', emailId, studentId, url);
        console.log('Link clicked: ', emailId, studentId, url);

        fetch(`messaging/track/${emailId}?student_id=${studentId}`, {
            method: 'POST',
        })
            .then((response) => {
                if (response.ok) {
                    console.log('Link click tracked');
                } else {
                    console.error('Failed to track link click');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    };

    const handleCloseEmailView = () => {
        setSelectedEmail(null); 
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div className="emailList__list">
            <ul  className="email-list">
                {emails.map(email => (
                    <li 
                        key={email.id} 
                        className="emailRow" 
                        onClick={() => handleEmailClick(email.id)}
                    >
                        <div className="emailRow__options">
                            <input type="checkbox" name id />
                            <span className="material-icons"> star_border </span>
                            <span className="material-icons"> label_important </span>
                        </div>

                    
                        <h3 className="emailRow__title">{email.sender}</h3>
                            <div className="emailRow__message">
                                <h4>
                                {email.subject}
                                </h4>
                            </div>
                            <p className="emailRow__time">{new Date(email.sent_at).toLocaleString()}</p>                               

                    </li>
                ))}
            </ul>
            {selectedEmail && (
                <EmailView
                    email={selectedEmail}
                    onReply={(replyBody) => handleReplySubmit(selectedEmail.email_id, replyBody)}
                    onLinkClick={(url) => handleLinkClick(selectedEmail.email_id, url)}
                    onClose={handleCloseEmailView}
                />
            )}
        </div>
    );
}

export default Inbox;
