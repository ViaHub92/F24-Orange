import React, { useState, useEffect } from 'react';
import axios from 'axios';
import FetchPerformanceDetailedInstructor from './FetchPerformanceDetailedInstructor';

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
            .then(response => {
                console.log("Fetched Courses:", response.data); // Log courses data
                setCourses(response.data);
            })
            .catch(error => console.log(error));
    }, []);

    const handleCourseChange = (courseName) => {
        setLoading(true);
        axios.get(`/course/get_course/${courseName}`)
            .then(response => {
                console.log("Fetched Course Details:", response.data); // Log course details
                setStudents(response.data.students);
                setSelectedCourse(response.data);
                setSelectedStudent(null);
                setPerformanceData([]);
                setSelectedEmailId(null);
            })
            .catch(error => console.log(error))
            .finally(() => setLoading(false));
    };

    const handleStudentChange = (studentId) => {
        setSelectedStudent(studentId);
    };
    
    // Watch for selectedStudent change and fetch performance data
    useEffect(() => {
        if (selectedStudent) {
            setLoading(true);
            axios.get(`/performance/detailed/${selectedStudent}`)
                .then(response => {
                    console.log("Fetched Performance Data for Student:", response.data);
                    setPerformanceData(response.data);
                    setSelectedEmailId(null);
                })
                .catch(error => console.log(error))
                .finally(() => setLoading(false));
        }
    }, [selectedStudent]);
            
    const handleFeedbackSubmit = () => {
        if (!selectedEmailId) {
            alert('Please select an email to leave feedback for.');
            return;
        }
    
        if (!feedback.trim()) {
            alert('Please provide feedback.');
            return;
        }
    
        console.log("Submitting Feedback:", { selectedEmailId, feedback }); // Log feedback submission details
    
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
                <select onChange={e => {
                    const studentId = e.target.value;
                    console.log("Selected Student ID:", studentId); // Debug log to check the selected student ID
                    handleStudentChange(studentId);
                }} value={selectedStudent || ''}>
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
                    <FetchPerformanceDetailedInstructor studentId={selectedStudent} />

                    {/* Select Email */}
                    <h3>Select Email to Provide Feedback</h3>
                    <select onChange={e => setSelectedEmailId(e.target.value)} value={selectedEmailId || ''}>
                        <option value="">Select Email</option>
                        {performanceData.map((detail, index) => {
                            console.log("Email Detail:", detail); 
                            return (
                            <option key={index} value={detail.email_id}> {/* This is the problem*/}
                                {detail.email_subject} - {detail.email_body.substring(0, 30)}...
                            </option>
                            );
                        })}
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
