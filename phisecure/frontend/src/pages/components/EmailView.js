import React, { useState } from 'react';
import { IoMdClose } from "react-icons/io";

function EmailView({ email, onReply, onClose }) {
    const [replyBody, setReplyBody] = useState('');

    const handleReplyChange = (e) => {
        setReplyBody(e.target.value);
    };

    const handleReplySubmit = (e) => {
        e.preventDefault();
        onReply(email.id, replyBody);
        setReplyBody(''); // Clear the reply box after sending
    };


    return (
        <div className="email-view">
            <button onClick={onClose} className="closeButton">
                <IoMdClose size={30} color="black" />
            </button>
            <h3>{email.subject}</h3>
            <p><strong>From:</strong> {email.sender}</p>
            <p><strong>To:</strong> {email.recipient}</p>
            <p><strong>Body:</strong> {email.body}</p>
            
            <form onSubmit={handleReplySubmit}>
                <textarea
                    value={replyBody}
                    onChange={handleReplyChange}
                    placeholder="Type your reply here"
                    required
                ></textarea>
                <button type="submit">Send Reply</button>
            </form>
        </div>
    );
}

export default EmailView;
