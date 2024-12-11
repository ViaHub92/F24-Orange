import React, { useState } from 'react';
import axios from 'axios';
import { EditorState } from 'draft-js'; 
import 'draft-js/dist/Draft.css'; // Make sure to include the CSS
import { Editor } from 'react-draft-wysiwyg';
import 'react-draft-wysiwyg/dist/react-draft-wysiwyg.css';

const PeerPhishing = () => {
    const [courseId, setCourseId] = useState('');
    const [targets, setTargets] = useState([]);
    const [selectedTargetId, setSelectedTargetId] = useState(null);
    const [editorState, setEditorState] = useState(EditorState.createEmpty()); 
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [category, setCategory] = useState('')
    const [difficulty, setDifficulty] = useState('')
    const [senderTemplate, setSenderTemplate] = useState('');   
    const [subjectTemplate, setSubjectTemplate] = useState('')
    const [badLink, setBadLink] = useState('')
    const [redFlag, setRedFlag] = useState('')
    const [createdBy, setCreatedBy] = useState('')


    const handleEditorChange = (state) => {
        setEditorState(state);
    };

    // Fetch the target list for a given course ID
    const fetchTargets = async () => {
        if (!courseId) return;

        try {
            const response = await axios.get(`peer_phishing/target-list/course/${courseId}`);
            if (response.data.error) {
                setError(response.data.error);
                setTargets([]);
            } else {
                setTargets(response.data);
                setError('');
            }
        } catch (error) {
            setError(error.response ? error.response.data.error : 'An error occurred while fetching targets');
            setTargets([]);
        }
    };

    // Handle course ID input change
    const handleInputChange = (event) => {
        setCourseId(event.target.value);
    };

    // Handle selecting a target from the list
    const handleSelectTarget = (targetId) => {
        setSelectedTargetId(targetId);
        setMessage('');
        setError('');
    };

    // Handle creating and sending phishing email for selected target
    const handleCreateAndSend = async () => {
        if (!selectedTargetId) {
            setError('Please select a target.');
            return;
        }
    
        // Validate the template fields
        if (!name || !description || !category) {
            setError('Please fill out all template details.');
            return;
        }
    
        // Ensure the email body is not empty
        const emailBody = editorState.getCurrentContent().getPlainText();
        if (!emailBody.trim()) {
            setError('Email body cannot be empty.');
            return;
        }
    
        try {
            const response = await axios.post('peer_phishing/create-and-send', {
                target_id: selectedTargetId,
                body_template: emailBody,
                sender: senderTemplate,
                subject: subjectTemplate,
                badLink,
                redFlag,
                createdBy,
            });
    
            setMessage(response.data.message);  // Assuming success message is returned
            setError('');
        } catch (error) {
            setError(error.response ? error.response.data.error : 'An error occurred while sending the phishing email.');
            setMessage('');
        }
    };
    
    return (
            <div>
                <h2>Fill Target List</h2>

                {/* Input for courseId */}
                <div>
                    <label htmlFor="courseId">Course ID:</label>
                    <input
                        type="number"
                        id="courseId"
                        value={courseId}
                        onChange={handleInputChange}
                        placeholder="Enter Course ID"
                    />
                    <button onClick={fetchTargets}>Fetch Targets</button>
                </div>

                {/* Display targets for the selected course */}
                {targets.length > 0 && (
                    <div>
                        <h3>Select a Target</h3>
                        <ul>
                            {targets.map((target) => (
                                <li key={target.target_list_id}>
                                    <button onClick={() => handleSelectTarget(target.target_list_id)}>
                                        {target.student_name} (ID: {target.student_id})
                                    </button>
                                </li>
                            ))}
                        </ul>
                    </div>
                )}

                {/* Input fields for template details */}
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

                {/* Radio buttons for difficulty level */}
                <div>
                    <label>Difficulty Level:</label>
                    <div>
                        <input
                            type="radio"
                            id="beginner"
                            name="difficulty"
                            value="beginner"
                            checked={difficulty === 'beginner'}
                            onChange={(e) => setDifficulty(e.target.value)}
                        />
                        <label htmlFor="beginner">beginner</label>
                    </div>
                    <div>
                        <input
                            type="radio"
                            id="intermediate"
                            name="difficulty"
                            value="intermediate"
                            checked={difficulty === 'intermediate'}
                            onChange={(e) => setDifficulty(e.target.value)}
                        />
                        <label htmlFor="intermediate">intermediate</label>
                    </div>
                    <div>
                        <input
                            type="radio"
                            id="advanced"
                            name="difficulty_level"
                            value="advanced"
                            checked={difficulty === 'advanced'}
                            onChange={(e) => setDifficulty(e.target.value)}
                        />
                        <label htmlFor="advanced">advanced</label>
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
                    <label htmlFor="createdBy">Created By:</label>
                    <input
                        type="text"
                        id="createdBy"
                        value={createdBy}
                        onChange={(e) => setCreatedBy(e.target.value)}
                        placeholder="Enter the creator's name"
                    />
                </div>

                <div>
                    <h2>Email Body</h2>
                    <Editor editorState={editorState} onEditorStateChange={handleEditorChange} />
                </div>

                {/* Submit button */}
                <div>
                    <button onClick={handleCreateAndSend}>Create and Send</button>
                </div>

                {/* Error or success messages */}
                {error && <div style={{ color: 'red' }}>{error}</div>}
                {message && <div style={{ color: 'green' }}>{message}</div>}
            </div>
    );
};

export default PeerPhishing;
