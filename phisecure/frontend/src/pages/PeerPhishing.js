import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { EditorState } from 'draft-js';
import 'draft-js/dist/Draft.css';
import { Editor } from 'react-draft-wysiwyg';
import 'react-draft-wysiwyg/dist/react-draft-wysiwyg.css';
import axios from 'axios';

const PeerPhishingTemplate = () => {
    const { targetId } = useParams();
    const [editorState, setEditorState] = useState(EditorState.createEmpty());
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [category, setCategory] = useState('');
    const [difficulty, setDifficulty] = useState('');
    const [senderTemplate, setSenderTemplate] = useState('');
    const [subjectTemplate, setSubjectTemplate] = useState('');
    const [badLink, setBadLink] = useState('');
    const [redFlag, setRedFlag] = useState('');
    const [createdBy, setCreatedBy] = useState('');
    const [error, setError] = useState('');
    const [message, setMessage] = useState('');

    useEffect(() => {
        const loggedInStudentId = localStorage.getItem('student_id'); // Example: get from localStorage
        setCreatedBy(loggedInStudentId);
    }, []);
    
    const handleEditorChange = (state) => {
        setEditorState(state);
    };

    const handleCreateAndSend = async () => {
        if (!name || !description || !category) {
            setError('Please fill out all template details.');
            return;
        }

        const emailBody = editorState.getCurrentContent().getPlainText();
        if (!emailBody.trim()) {
            setError('Email body cannot be empty.');
            return;
        }

        console.log({
            name: name,
            description: description,
            category: category,
            target_id: targetId,
            difficulty_level: difficulty,
            body_template: emailBody,
            sender_template: senderTemplate,
            subject_template: subjectTemplate,
            link: badLink,
            template_redflag: redFlag,
            created_by: createdBy,
        });

        try {
            const response = await axios.post('peer_phishing/create-and-send', {
                name: name,
                description: description,
                category: category,
                target_id: targetId,
                difficulty_level: difficulty,
                body_template: emailBody,
                sender_template: senderTemplate,
                subject_template: subjectTemplate,
                link: badLink,
                template_redflag: redFlag,
                created_by: createdBy,
            });

            setMessage(response.data.message);
            setError('');
        } catch (error) {
            setError(error.response ? error.response.data.error : 'An error occurred while sending the phishing email.');
            setMessage('');
        }
    };

    return (
        <div>
            <h2>Peer Phishing Template</h2>
            <div>
                <label htmlFor="name">Template Name:</label>
                <input
                    type="text"
                    id="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Enter template name"
                />
            </div>

            <div>
                <label htmlFor="description">Template Description:</label>
                <input
                    type="text"
                    id="description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Enter template description"
                />
            </div>

            <div>
                <label htmlFor="category">Template Category:</label>
                <input
                    type="text"
                    id="category"
                    value={category}
                    onChange={(e) => setCategory(e.target.value)}
                    placeholder="Enter template category"
                />
            </div>

            <div>
                <label>Difficulty Level:</label>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <input
                            type="radio"
                            id="beginner"
                            name="difficulty"
                            value="beginner"
                            checked={difficulty === 'beginner'}
                            onChange={(e) => setDifficulty(e.target.value)}
                        />
                        <label htmlFor="beginner">Beginner</label>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <input
                            type="radio"
                            id="intermediate"
                            name="difficulty"
                            value="intermediate"
                            checked={difficulty === 'intermediate'}
                            onChange={(e) => setDifficulty(e.target.value)}
                        />
                        <label htmlFor="intermediate">Intermediate</label>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <input
                            type="radio"
                            id="advanced"
                            name="difficulty"
                            value="advanced"
                            checked={difficulty === 'advanced'}
                            onChange={(e) => setDifficulty(e.target.value)}
                        />
                        <label htmlFor="advanced">Advanced</label>
                    </div>
                </div>
            </div>



            <div>
                <label htmlFor="senderTemplate">Sender:</label>
                <input
                    type="text"
                    id="senderTemplate"
                    value={senderTemplate}
                    onChange={(e) => setSenderTemplate(e.target.value)}
                    placeholder="Enter sender's email"
                />
            </div>

            <div>
                <label htmlFor="subjectTemplate">Subject:</label>
                <input
                    type="text"
                    id="subjectTemplate"
                    value={subjectTemplate}
                    onChange={(e) => setSubjectTemplate(e.target.value)}
                    placeholder="Enter subject template"
                />
            </div>

            <div>
                <label htmlFor="badLink">Bad Link:</label>
                <input
                    type="text"
                    id="badLink"
                    value={badLink}
                    onChange={(e) => setBadLink(e.target.value)}
                    placeholder="Enter a bad link"
                />
            </div>

            <div>
                <label htmlFor="redFlag">Red Flag:</label>
                <input
                    type="text"
                    id="redFlag"
                    value={redFlag}
                    onChange={(e) => setRedFlag(e.target.value)}
                    placeholder="Enter a red flag"
                />
            </div>

            <div>
                <h3>Email Body</h3>
                <Editor editorState={editorState} onEditorStateChange={handleEditorChange} />
            </div>

            <div>
                <button onClick={handleCreateAndSend}>Create and Send</button>
            </div>

            {error && <div style={{ color: 'red' }}>{error}</div>}
            {message && <div style={{ color: 'green' }}>{message}</div>}
        </div>
    );
};

export default PeerPhishingTemplate;
