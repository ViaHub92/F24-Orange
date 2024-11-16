export default function PeerPhishingTemplate() {
    return (
      <div>
          <meta charSet="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure - Contact</title>
          <link rel="stylesheet" href="styles.css" />
          {/* Main Content */}
          <main>
          <section className="section">
            <h2>Peer Phishing Template Fill-In</h2>
            <form>
                <label for="Title">Title:</label><br></br>
                <input type="text" id="Title" name="Title" style={{width:'500px'}}></input><br></br><br></br>

                <label for="Body">Body:</label><br></br>
                <input type="Body" id="Body" name="Body" style={{width: '500px', height:"300px"}}></input><br></br><br></br>

                <label for="FillIn1">Fill-In 1:</label><br></br>
                <input type="text" id="FillIn1" name="FillIn1" style={{width:'500px'}}></input><br></br><br></br>
                
                <label for="FillIn2">Fill-In 2:</label><br></br>
                <input type="text" id="FillIn2" name="FillIn2" style={{width:'500px'}}></input><br></br><br></br>

                <h4>NOTE: I AM FULLY AWARE OF THE CONSEQUENCES OF USING PHISECURE TO PERFORM ACTUAL PHISHING ATTACKS AGAINST PEERS.<br></br>
                    PUNISHMENTS CAN INCLUDE TEMPORARY AND/OR PERMENANT SUSPENSION OF ACCOUNT AND POTENTIAL REPORTING TO LOCAL AUTHORITIES.<br></br>
                    PHISECURE IS TO BE USED FOR PHISHING EDUCATION ONLY. BY CLICKING SUBMIT, YOU ARE AGREEING TO BE RESPONSIBLE AND USE
                    PHISEUCRE FOR ITS INTENDED PURPOSE.
                </h4>
                <input type="submit" value="Submit"></input>
            </form>
          </section>
          </main>
          {/* Footer */}
          <footer>
          <p>© 2024 Phisecure. All rights reserved.</p>
          </footer>
      </div>
    )
}
  