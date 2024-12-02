import React, { useState, useEffect } from 'react';
import axios from 'axios';
import FetchPerformanceDetailed from './FetchPerformanceDetailed';

const LeaveFeedback = () => {
    const [courses, setCourses] = useState([]);
    const [selectedCourse, setSelectedCourse] = useState(null);
    const [students, setStudents] = useState([]);
    const [selectedStudent, setSelectedStudent] = useState(null);
    const [performanceData, setPerformanceData] = useState([]);
    const [selectedEmailId, setSelectedEmailId] = useState(null);
    const [feedback, setFeedback] = useState('');
    const [loading, setLoading] = useState(false); 

    // Fetch the list of courses
    useEffect(() => {
        axios.get('course/list_courses')
            .then(response => setCourses(response.data))
            .catch(error => console.log(error));
    }, []);

    // Fetch the students of the selected course
    const handleCourseChange = (courseName) => {
        setLoading(true);
        axios.get(`/course/get_course/${courseName}`)
            .then(response => {
                setStudents(response.data.students);
                setSelectedCourse(response.data);
                setSelectedStudent(null);
                setPerformanceData([]);
                setSelectedEmailId(null);
            })
            .catch(error => console.log(error))
            .finally(() => setLoading(false));
    };

    // Fetch the detailed performance report for the selected student
    const handleStudentChange = (studentId) => {
        setLoading(true);
        axios.get(`/performance/detailed/${studentId}`)
            .then(response => {
                setPerformanceData(response.data);
                setSelectedStudent(studentId);
                setSelectedEmailId(null);
            })
            .catch(error => console.log(error))
            .finally(() => setLoading(false));
    };

    // Submit feedback for the selected phishing email
    const handleFeedbackSubmit = () => {
        if (!selectedEmailId) {
            alert('Please select an email to leave feedback for.');
            return;
        }

        if (!feedback.trim()) {
            alert('Please provide feedback.');
            return;
        }

        setLoading(true);
        axios.patch(`/instructor_dashboard/phishing_email/${selectedEmailId}/feedback`, {
            instructor_feedback: feedback
        })
            .then(() => {
                alert('Feedback submitted successfully!');
                setFeedback('');
                setSelectedEmailId(null);
            })
            .catch(error => {
                alert('Failed to submit feedback');
                console.error(error);
            })
            .finally(() => setLoading(false));
    };

    return (
        <div>
            <h2>Leave Feedback for Student Performance</h2>

            {/* Select Course */}
            <select onChange={e => handleCourseChange(e.target.value)} value={selectedCourse?.course_name || ''}>
                <option value="">Select Course</option>
                {courses.map(course => (
                    <option key={course.id} value={course.course_name}>
                        {course.course_name}
                    </option>
                ))}
            </select>

            {/* Select Student */}
            {selectedCourse && (
                <select onChange={e => handleStudentChange(e.target.value)} value={selectedStudent || ''}>
                    <option value="">Select Student</option>
                    {students.map(student => (
                        <option key={student.id} value={student.id}>
                            {student.first_name} {student.last_name}
                        </option>
                    ))}
                </select>
            )}

            {/* Show Performance Data */}
            {performanceData.length > 0 && selectedStudent && (
                <div>
                    <FetchPerformanceDetailed data={performanceData} />

                    {/* Select Email */}
                    <h3>Select Email to Provide Feedback</h3>
                    <select onChange={e => setSelectedEmailId(e.target.value)} value={selectedEmailId || ''}>
                        <option value="">Select Email</option>
                        {performanceData.map((detail, index) => (
                            <option key={index} value={detail.email_id}> {/* This is the problem*/}
                                {detail.email_subject} - {detail.email_body.substring(0, 30)}...
                            </option>
                        ))}
                    </select>

                    {/* Feedback Form */}
                    {selectedEmailId && (
                        <div>
                            <textarea
                                value={feedback}
                                onChange={e => setFeedback(e.target.value)}
                                placeholder="Leave your feedback here"
                            />
                            <button onClick={handleFeedbackSubmit} disabled={loading}>
                                {loading ? 'Submitting...' : 'Submit Feedback'}
                            </button>
                        </div>
                    )}
                </div>
            )}

            {/* Loading Indicator */}
            {loading && <div>Loading...</div>}
        </div>
    );
};

export default LeaveFeedback;
