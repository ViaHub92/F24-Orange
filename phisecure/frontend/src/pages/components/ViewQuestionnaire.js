import React, { useState, useEffect } from "react";
import '../../styles/styles.css'; 




const ViewQuestionnaire = () => { 
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch("/questionnaire/2")
          .then(res => res.json())
          .then(data => {
            setData(data);
            console.log(data);
          })
          .catch(error => console.error("Error fetching data: ", error));
      }, []);

      const handleSubmit = (event) => {
        event.preventDefault();
        // handle form submission logic here
        console.log("Form submitted");
      };
 
      return (
        <div className="container">
          <h1 className="title">{data.name}</h1>
          <p className="description">{data.description}</p>
          <form onSubmit={handleSubmit}>
          {data.questions && data.questions.length > 0 ? (
            data.questions.map((question, i) => (
              <div key={i} className="question">
                <p className="question-text">Question: {question.question_text}</p>
                {question.options && question.options.length > 0 && (
                  <ul className="options">
                    {question.options.map((option, j) => (
                      <li key={j} className="option">
                        <label>
                          <input
                            type="radio"
                            name={`question-${i}`}
                            value={option.option_text}
                          />
                          {option.option_text}
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
          <button type="submit"  className="submit-button">Submit</button>
          </form>
        </div>
      );
}

export default ViewQuestionnaire;