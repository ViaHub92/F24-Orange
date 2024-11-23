import React, { useState, useEffect } from 'react';
import { IoMdClose } from "react-icons/io";

const convertMarkdownToHtml = (text) => {
    const urlRegex = /\[([^\]]+)\]\((https?:\/\/[^\s]+)\)/g;
    return text.replace(urlRegex, (match, label, url) => {
        return `<a href="${url}" class="email-link" data-email-id="${label}" data-url="${url}" target="_blank">${label}</a>`;
    });
};

function EmailView({ email, onReply, onClose, onLinkClick }) {
    const [replyBody, setReplyBody] = useState('');
    const [emailBodyHtml, setEmailBodyHtml] = useState('');

    useEffect(() => {
        if (email && email.body) {
            setEmailBodyHtml(convertMarkdownToHtml(email.body));
        }
    }, [email]);

    const handleReplyChange = (e) => {
        setReplyBody(e.target.value);
    };

    const handleReplySubmit = (e) => {
        e.preventDefault();
        onReply(email.id, replyBody);
        setReplyBody('');
    };

    const handleLinkClick = (e) => {

        e.preventDefault();
        onLinkClick(email.id);
    };

    return (
        <div className="email-view">
            <button onClick={onClose} className="closeButton">
                <IoMdClose size={30} color="black" />
            </button>
            <h3>{email.subject}</h3>
            <p><strong>From:</strong> {email.sender}</p>
            <p><strong>To:</strong> {email.recipient}</p>

            <div
                dangerouslySetInnerHTML={{ __html: emailBodyHtml }}
                onClick={handleLinkClick}
            />
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
