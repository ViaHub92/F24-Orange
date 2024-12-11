
import React, { useState, useEffect } from "react";
import { FaSnapchat, FaInstagram, FaTwitter } from "react-icons/fa";
import { Mosaic } from "react-loading-indicators";
import '../../styles/styles.css';

const ViewQuestionnaire = () => {
    const [data, setData] = useState([]);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [answers, setAnswers] = useState({});
    const [unansweredQuestion, setUnansweredQuestion] = useState(null);
    const studentId = localStorage.getItem('student_id');

    useEffect(() => {
        fetch("/questionnaire/3")
            .then(res => res.json())
            .then(data => {
                setData(data);
                console.log(data);
            })
            .catch(error => console.error("Error fetching data: ", error));
    }, []);

    const handleAnswerChange = (questionId, answerText, isMultipleChoice) => {
        if (isMultipleChoice) {
            setAnswers(prevAnswers => {
                const currentAnswers = prevAnswers[questionId] || [];
                if (currentAnswers.includes(answerText)) {
                    return {
                        ...prevAnswers,
                        [questionId]: currentAnswers.filter(answer => answer !== answerText)
                    };
                } else {
                    return {
                        ...prevAnswers,
                        [questionId]: [...currentAnswers, answerText]
                    };
                }
            });
        } else {
            setAnswers(prevAnswers => ({
                ...prevAnswers,
                [questionId]: answerText // Store the answer as-is
            }));
        }
        setUnansweredQuestion(null); // Reset the unanswered question state
    };

    const handleNextQuestion = () => {
        // Ensure an answer has been provided for the current question
        const currentQuestion = data.questions[currentQuestionIndex];
        
        // Check answer based on question type
        const hasAnswer = currentQuestion.question_type === 'short answer' 
            ? answers[currentQuestion.id] && answers[currentQuestion.id].trim() !== ''
            : answers[currentQuestion.id];

        if (!hasAnswer) {
            setUnansweredQuestion(currentQuestion.id);
            return;
        }
        
        // Move to the next question
        setCurrentQuestionIndex(currentQuestionIndex + 1);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Validate that all questions have been answered
        const unansweredQuestions = data.questions.filter(q => {
            // For short answer, check if the trimmed answer exists
            if (q.question_type === 'short answer') {
                return !answers[q.id] || answers[q.id].trim() === '';
            }
            // For other types, check if answer exists
            return !answers[q.id];
        });

        if (unansweredQuestions.length > 0) {
            setUnansweredQuestion(unansweredQuestions[0].id);
            return;
        }

        const formattedAnswers = Object.keys(answers).map(questionId => ({
            question_id: parseInt(questionId, 10), // Ensure question_id is an integer
            answer_text: Array.isArray(answers[questionId]) ? answers[questionId].join(', ') : answers[questionId]
        }));

        console.log('Answers:', formattedAnswers);
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
                    answers: formattedAnswers,
                }),
            });

            if (!response.ok) {
                const errorText = await response.text();
                console.error('Error:', response.status, errorText);
                alert(`Error: ${response.status} - ${errorText}`);
            } else {
                const result = await response.json();
                console.log('Success:', result);
                alert(result.message);
            }
        } catch (error) {
            console.error('Fetch error:', error);
            alert(`Fetch error: ${error.message}`);
        }
    };

    if (!data.questions || data.questions.length === 0) {
        return <p><Mosaic color="#231D6C" size="small" text="" textColor="" /></p>;
    }

    const currentQuestion = data.questions[currentQuestionIndex];

    return (
        <div className="container">
            <h1 className="title">{data.name}</h1>
            <p className="description">{data.description}</p>
            <form onSubmit={handleSubmit}>
                <div className="question">
                    <p className="question-text">Question {currentQuestionIndex + 1}: {currentQuestion.question_text}</p>
                    {currentQuestion.question_type === 'short answer' ? (
                        <textarea
                            name={`question-${currentQuestion.id}`}
                            rows="3"
                            className={`w-full p-2 border rounded ${unansweredQuestion === currentQuestion.id ? 'border-red-500' : ''}`}
                            placeholder="Enter your answer here..."
                            value={answers[currentQuestion.id] || ''}
                            onChange={(e) => handleAnswerChange(currentQuestion.id, e.target.value, false)}
                        />
                    ) : currentQuestion.options && currentQuestion.options.length > 0 && (
                        <ul className="options">
                            {currentQuestion.options.map((option, j) => (
                                <li key={j} className="option">
                                    <label>
                                        <input
                                            type={currentQuestion.question_type === 'multiple choice' ? "checkbox" : "radio"}
                                            name={`question-${currentQuestion.id}`}
                                            value={option.option_text}
                                            checked={currentQuestion.question_type === 'multiple choice' ? (answers[currentQuestion.id] || []).includes(option.option_text) : answers[currentQuestion.id] === option.option_text}
                                            onChange={(e) => handleAnswerChange(currentQuestion.id, e.target.value, currentQuestion.question_type === 'multiple choice')}
                                        />
                                        {option.option_text}
                                        {currentQuestion.question_type === 'multiple choice' && option.option_text === 'Snapchat' && (
                                            <span style={{ marginLeft: '4px' }}><FaSnapchat /></span>
                                        )}
                                        {currentQuestion.question_type === 'multiple choice' && option.option_text === 'Instagram' && (
                                            <span style={{ marginLeft: '4px' }}><FaInstagram /></span>
                                        )}
                                        {currentQuestion.question_type === 'multiple choice' && option.option_text === 'X' && (
                                            <span style={{ marginLeft: '4px' }}><FaTwitter /></span>
                                        )}
                                    </label>
                                </li>
                            ))}
                        </ul>
                    )}
                </div>
                {currentQuestionIndex < data.questions.length - 1 ? (
                    <button type="button" className="submit-button" onClick={handleNextQuestion}>Next</button>
                ) : (
                    <button type="submit" className="submit-button">Submit</button>
                )}
            </form>
        </div>
    );
}

export default ViewQuestionnaire;