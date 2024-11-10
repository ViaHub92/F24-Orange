import React, { useState, useEffect } from "react";

function FetchInbox() {
    const [data, setData] = useState([]);

    useEffect(() => {
    fetch('messaging/inbox?student_id=${4}')
        .then(res => res.json())
        .then(data => {
        setData(data);
        console.log(data);
        })
        .catch(error => console.error("Error fetching data: ", error));
    }, []);

    return (
    <div>
        {data.length === 0 ? (
        <p>Waiting...</p>
        ) : (
        <div>
            <p>id: {data.email_id} </p>
        </div> 
        )}    
    </div>
    )
};

export default FetchInbox;
        
