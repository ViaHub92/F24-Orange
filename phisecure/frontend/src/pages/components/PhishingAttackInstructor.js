import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PhishingAttackInstructor = () => {
    const [courses, setCourses] = useState([]);
    const [students, setStudents] = useState([]);
    const [selectedCourse, setSelectedCourse] = useState(null);
    const [selectedStudent, setSelectedStudent] = useState(null);
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const instructorId = localStorage.getItem('instructor_id');

    // Fetch the list of courses
    useEffect(() => {
        axios.get(`/course/list_courses/${instructorId}`)
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
        
            })
            .catch(error => console.log(error))
            .finally(() => setLoading(false));
    };

    const handleStudentChange = (studentId) => {
        setSelectedStudent(studentId);
    };

    const handleSendEmail = () => {
        if (!selectedStudent) {
            setError("Please select a student.");
            return;
        }

        // Send phishing email
        axios.post(`messaging/compose_phishing_email/${selectedStudent}`)
            .then(response => {
                alert("Phishing email sent successfully!");
                setError(""); // Reset error
            })
            .catch(err => {
                setError("Error sending phishing email.");
            });
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

            {/* Send Button */}
            <div>
                <button onClick={handleSendEmail}>Send Phishing Email</button>
            </div>

            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
};

export default PhishingAttackInstructor;
