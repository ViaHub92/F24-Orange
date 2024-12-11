import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DeleteStudent = () => {
  const [students, setStudents] = useState([]);
  const [selectedStudentId, setSelectedStudentId] = useState(null);

  // Fetch list of students
  useEffect(() => {
    const fetchStudents = async () => {
      try {
        const response = await axios.get('/account/list_students');
        setStudents(response.data);
      } catch (error) {
        console.error('Error fetching students:', error);
      }
    };
    fetchStudents();
  }, []);

  // Handle student selection for deletion
  const handleStudentSelect = (event) => {
    setSelectedStudentId(event.target.value);
  };

  // Delete selected student
  const handleDeleteStudent = async () => {
    if (!selectedStudentId) {
      alert('Please select a student to delete');
      return;
    }

    try {
      await axios.delete(`/account/delete_student/${selectedStudentId}`);
      alert('Student deleted successfully!');
      setStudents(students.filter((student) => student.student_id !== selectedStudentId));
      setSelectedStudentId(null);
    } catch (error) {
      console.error('Error deleting student:', error);
      alert('Error deleting student');
    }
  };

  return (
    <div>
      <h5>Delete Student</h5>
      
      <div>
        <select onChange={handleStudentSelect} value={selectedStudentId || ''}>
          <option value="">Select a student to delete</option>
          {students.map((student) => (
            <option key={student.student_id} value={student.student_id}>
              {student.first_name} {student.last_name} ({student.username})
            </option>
          ))}
        </select>
      </div>

      <div>
        <button onClick={handleDeleteStudent} disabled={!selectedStudentId}>
          Delete Student
        </button>
      </div>
    </div>
  );
};

export default DeleteStudent;
