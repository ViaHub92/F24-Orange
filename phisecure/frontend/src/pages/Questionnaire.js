import CreateQuestionnaire from "./components/CreateQuestionnaire";

export default function Questionnaire() {
    return(
        <div>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Phisecure - About</title>
        <link rel="stylesheet" href="styles.css" />

        {/* Main Content */}
        <main>
            <CreateQuestionnaire />
            <section className="section">
            <form action="/questionnaire_page.php">
                <p>
                Hello! This is a questionnaire for new users to better know you and
                customize our faux phishing attempts to best train you. Below are a
                list of questions and fill-ins. Respond to them and when you're done,
                submit.
                <br />
                <br />
                Please, be as honest and direct as possible. It will give you the best
                results with our service.
                </p>
                <p>First Name:</p>
                <input type="text" id="fname" name="fname" />
                <br />
                <p>Last Name:</p>
                <input type="text" id="lname" name="lname" />
                <br />
                <p>Username:</p>
                <input type="text" id="uname" name="uname" />
                <br />
                <p>Email:</p>
                <input type="text" id="email" name="email" />
                <br />
                <p>Are you currently employed?</p>
                <input
                type="radio"
                id="empstat1"
                name="yes"
                defaultValue="empstatyes"
                />
                <label htmlFor="empstat1">Yes</label>
                <input
                type="radio"
                id="empstat2"
                name="empstatno"
                defaultValue="empstatno"
                />
                <label htmlFor="empstat2">No</label>
                <br />
                <p>If so, name your place of employment and experience:</p>
                <input type="text" id="employmentdetails" name="empdet" />
                <br />
                {/*Too specific, comment out
                <p>Have you recently moved from your hometown to your selected college?</p>
                    <input type="radio" id="movecoll1" name="yes" value="movecollyes">
                    <label for="movecoll1">Yes</label>
                    <input type="radio" id="movecoll2" name="no" value="movecollno">
                    <label for="movecoll2">Yes</label><br>
                
                */}
                <p>Do you not have any problems financially at the moment?</p>
                <input type="radio" id="financialyes" name="financialyes" />
                <label htmlFor="financialyes">Yes</label>
                <input type="radio" name="financialno" />
                <label htmlFor="financialno">No</label>
                <br />
                {/* Too Vague: Comment it Out f or now
                <p>How well versed are you in computer technology and web safety?</p>
                    <input type="radio" id="knowledgewellversed" name="knowledgewellversed">
                    <label for="knowledgewellversed">Well Versed</label>
                    <input type="radio" id="knowledgedecentlyversed" name="knowledgedecentlyvversed">
                    <label for="knowledgedecentlyversed">Decently Versed</label>
                    <input type="radio" id="knowledgesso" name="knowledgesoso">
                    <label for="knowledgesoso">Alright</label>
                    <input type="radio" id="knowledgenotwellversed" name="knowledgenotwellversed">
                    <label for="knowledgenotwellversed">Not Well Versed</label>
                    <input type="radio" id="knowledgenonex" name="knowledgenonex">
                    <label for="knowledgenonex">Nonexistent Knowledge Base</label><br>
                */}
                <p>Do you often change your password?</p>
                <input type="radio" id="passyes" name="passyes" />
                <label htmlFor="passyes">Yes</label>
                <input type="radio" id="passno" name="passno" />
                <label htmlFor="passno">No</label>
                <br />
                <p>Do you reuse password for multiple accounts?</p>
                <input type="radio" id="reuseyes" name="reuseyes" />
                <label htmlFor="reuseyes">Yes</label>
                <input type="radio" id="reuseno" name="reuseno" />
                <label htmlFor="reuseno">No</label>
                <br />
                <p>
                Has your college and/or place of employment recently suffered a
                wide-scale spear phishing attack?
                </p>
                <input type="radio" id="empphishyes" name="phishyes" />
                <label htmlFor="empphishyes">Yes</label>
                <input type="radio" id="empphishno" name="phishno" />
                <label htmlFor="empphishno">No</label>
                <br />
                <p>If so, describe the attack:</p>
                <input type="text" id="empattdetails" name="ead" />
                <br />
                <br />
                <input type="submit" defaultValue="Submit" />
            </form>
            </section>
        </main>
        {/* Footer */}
        <footer>
            <p>© 2024 Phisecure. All rights reserved.</p>
        </footer>
        </div>
    );
}
