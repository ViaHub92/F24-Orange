import React, { useState, useEffect } from "react";
import { FaSnapchat, FaInstagram, FaTwitter } from "react-icons/fa";
import '../../styles/styles.css'; 




const ViewQuestionnaire = () => { 
    const [data, setData] = useState([]);
    const [selectedOption, setSelectedOption] = useState();
    const studentId = 9;

    useEffect(() => {
        fetch("/questionnaire/3")
          .then(res => res.json())
          .then(data => {
            setData(data);
            console.log(data);
          })
          .catch(error => console.error("Error fetching data: ", error));
      }, []);

      const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);  // Create FormData object from the form
    
        // Prepare the answers from the form data
        const answers = [];
        formData.forEach((value, key) => {
            const questionId = key.split('-')[1];
            answers.push({ question_id: questionId, answer_text: value });
        });

        
     // Log the data being sent
     console.log('Form Data:', formData);
     console.log('Answers:', answers);
     console.log('Student ID:', studentId);
    
        try {
            const response = await fetch(`/questionnaire/Submit/${studentId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    student_id: studentId,
                    questionnaire_id: data.id,
                    answers: answers,
                }),
            });
    
            if (!response.ok) {
                const errorText = await response.text();
                console.error('Error:', response.status, errorText);
                alert(`Error: ${response.status} - ${errorText}`);
            } else {
                const result = await response.json();
                console.log('Success:', result);
            }
        } catch (error) {
            console.error('Fetch error:', error);
            alert(`Fetch error: ${error.message}`);
        }
    };
  
    return (
      <div className="container">
        <h1 className="title">{data.name}</h1>
        <p className="description">{data.description}</p>
        <form onSubmit={handleSubmit}>
          {data.questions && data.questions.length > 0 ? (
            data.questions.map((question, i) => (
              <div key={question.id} className="question">
                <p className="question-text">Question {i + 1}: {question.question_text}</p>
                {question.question_type === 'short answer' ? (
                  <textarea 
                    name={`question-${question.id}`}
                    rows="3"
                    className="w-full p-2 border rounded"
                    placeholder="Enter your answer here..."
                  />
                ) : question.options && question.options.length > 0 && (
                  <ul className="options">
                    {question.options.map((option, j) => (
                      <li key={j} className="option">
                        <label>
                          <input
                            type={question.question_type === 'multiple choice' ? "checkbox" : "radio"}
                            name={`question-${question.id}`}
                            value={option.option_text}
                          />
                          {option.option_text}
                          {question.question_type === 'multiple choice' && option.option_text === 'Snapchat' && (
                            <span style={{ marginLeft: '4px' }}><FaSnapchat /></span>
                          )}
                          {question.question_type === 'multiple choice' && option.option_text === 'Instagram' && (
                            <span style={{ marginLeft: '4px' }}><FaInstagram /></span>
                          )}
                          {question.question_type === 'multiple choice' && option.option_text === 'X' && (
                            <span style={{ marginLeft: '4px' }}><FaTwitter /></span>
                          )}
                        </label>
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            ))
          ) : (
            <p>No questions available</p>
          )}
          <button type="submit" className="submit-button">Submit</button>
        </form>
      </div>
    );
}

export default ViewQuestionnaire;