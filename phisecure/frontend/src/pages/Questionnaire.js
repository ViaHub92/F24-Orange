// Desc: Questionnaire page for Phisecure
import ViewQuestionnaire from "./components/ViewQuestionnaire";

export default function Questionnaire() {
    return(
        <div>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Phisecure - About</title>
        <link rel="stylesheet" href="styles.css" />

        {/* Main Content */}
        <main>
         
            <section className="section">
            
            <ViewQuestionnaire />
            </section>
        </main>
        {/* Footer */}
        <footer>
            <p>© 2024 Phisecure. All rights reserved.</p>
        </footer>
        </div>
    );
}
