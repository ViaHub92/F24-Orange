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

    const handleEditorChange = (state) => {
      setEditorState(state);
    };

    // Handle creating and sending phishing email for selected target
    const handleCreateAndSend = async () => {
        if (!selectedTargetId) {
            setError('Please select a target.');
            return;
        }

        // Get the email body from the editor
        const emailBody = editorState.getCurrentContent().getPlainText(); // Convert the editor content to plain text

        try {
            const response = await axios.post('peer_phishing/create-and-send', {
                target_id: selectedTargetId,
                body_template: emailBody, // Include the email body in the POST request
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

            {/* react-draft-wysiwyg Editor for the email body */}
            <div>
                <h3>Phishing Email:</h3>
                <Editor
                editorState={editorState}
                onEditorStateChange={handleEditorChange}  // Handle editor state changes
                toolbarClassName="demo-toolbar"
                wrapperClassName="demo-wrapper"
                editorClassName="demo-editor"
                placeholder="Write your phishing email content here..."
            />
            </div>

            {/* Button to create and send phishing email */}
            {selectedTargetId && (
                <div>
                    <button onClick={handleCreateAndSend}>Create and Send Phishing Email</button>
                </div>
            )}

            {/* Display success or error message */}
            {message && <div style={{ color: 'green', marginTop: '10px' }}>{message}</div>}
            {error && <div style={{ color: 'red', marginTop: '10px' }}>{error}</div>}
        </div>
    );
};

export default PeerPhishing;
