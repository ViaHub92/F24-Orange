import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const PeerCourse = () => {
    const [courseId, setCourseId] = useState('');
    const [targets, setTargets] = useState([]);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const verifyStudent = async () => {
            try {
                const studentId = localStorage.getItem('student_id'); // Assuming the student ID is stored in localStorage
                if (!studentId) {
                    navigate('/login');
                    return;
                }

                const response = await axios.get(`/account/get_student/${studentId}`);
                if (response.status !== 200) {
                    navigate('/login');
                }
            } catch (error) {
                // Redirect to login if the API fails or the student isn't found
                navigate('/login');
            }
        };

        verifyStudent();
    }, [navigate]);

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
            setError(error.response ? error.response.data.error : 'An error occurred while fetching targets.');
            setTargets([]);
        }
    };

    const handleInputChange = (event) => {
        setCourseId(event.target.value);
    };

    const handleSelectTarget = (targetId) => {
        navigate(`/${targetId}`);
    };

    return (
        <div>
            <h2>Select a Course</h2>
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

            {error && <div style={{ color: 'red' }}>{error}</div>}
        </div>
    );
};

export default PeerCourse;
